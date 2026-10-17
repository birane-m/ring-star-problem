"""CLI orchestration; algorithms and persistence live in dedicated modules."""
from __future__ import annotations

import argparse
from dataclasses import replace
import json
from pathlib import Path
import sys
import tempfile
from typing import Sequence

from ring_star.artifacts import load_saved_solution, run_data, save_run, write_json
from ring_star.benchmark import (
    BENCHMARK_METHODS, build_comparison_csv, run_benchmark,
    save_benchmark_comparison_plots, save_benchmark_csv, save_solution_plots_from_benchmark_csv,
)
from ring_star.distances import build_distance_matrix
from ring_star.execution import METHOD_LABELS, RunConfig, execute
from ring_star.experiments import replot_campaign, run_campaign
from ring_star.instance import RingStarProblem
from ring_star.io import load_tsplib_instance
from ring_star.paths import (
    default_point_cloud_output_path, default_benchmark_output_path,
    default_benchmark_solution_figures_directory, default_comparison_figures_directory,
    default_comparison_output_path, default_exact_result_output_path, default_exact_solution_output_path,
    default_tabu_result_output_path, default_tabu_solution_output_path,
    default_local_search_result_output_path, default_local_search_solution_output_path,
    default_greedy_result_markdown_output_path, default_greedy_result_output_path, default_greedy_solution_output_path,
)
from ring_star.results import solution_result_markdown
from ring_star.visualization import save_point_cloud_png, save_solution_png

RUN_METHOD_ALIASES = {
    "greedy": "greedy", "gloutonne": "greedy", "heuristique": "greedy",
    "local": "local_search", "locale": "local_search", "local-search": "local_search", "local_search": "local_search",
    "tabu": "tabu_search", "tabou": "tabu_search", "tabu-search": "tabu_search", "tabu_search": "tabu_search",
    "meta": "tabu_search", "metaheuristique": "tabu_search",
    "exact": "exact_plne", "plne": "exact_plne", "exact_plne": "exact_plne",
}


def _algorithm_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("instance", type=Path)
    parser.add_argument("p", type=int)
    parser.add_argument("--alpha", type=float, default=1.0)
    parser.add_argument("--iterations", type=int)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--tabu-tenure", type=int, default=20)
    parser.add_argument("--candidates-per-iteration", type=int)
    parser.add_argument("--time-limit", type=float, default=30, help="CBC seconds; 0 means no exact limit.")
    parser.add_argument("--search-time-limit", type=float, help="Improvement phase seconds; excludes initialization and plotting.")
    parser.add_argument("--solver-message", action="store_true")
    parser.add_argument("--labels", action="store_true")
    parser.add_argument("--output-root", type=Path, default=Path("outputs"))
    parser.add_argument("--no-plots", action="store_true")
    parser.add_argument("--plot", action="store_true", help="For compatibility with solve-* aliases.")
    parser.add_argument("--plot-output", type=Path)
    parser.add_argument("--save-result", action="store_true")
    parser.add_argument("--result-output", type=Path)
    parser.set_defaults(func=_solve)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ring-star", description="Ring-Star: solve, compare and reproduce experiments.")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run", help="Solve and save a complete experiment in outputs/runs/.")
    run.add_argument("method", choices=sorted(RUN_METHOD_ALIASES))
    _algorithm_options(run)
    for command, method in (("solve-greedy", "greedy"), ("solve-local-search", "local_search"),
                            ("solve-tabu", "tabu_search"), ("solve-exact", "exact_plne")):
        alias = sub.add_parser(command, help="Compatibility alias; prefer run.")
        _algorithm_options(alias)
        alias.set_defaults(method=method)
    point = sub.add_parser("plot-instance")
    point.add_argument("instance", type=Path)
    point.add_argument("--output", "-o", type=Path)
    point.add_argument("--labels", action="store_true")
    point.set_defaults(func=_plot_instance)
    replot = sub.add_parser("plot-saved", help="Plot the exact saved solution, verifying its costs.")
    replot.add_argument("solution", type=Path)
    replot.add_argument("--output", "-o", type=Path, required=True)
    replot.add_argument("--labels", action="store_true")
    replot.set_defaults(func=_plot_saved)
    redraw = sub.add_parser("plot-campaign", help="Regenerate figures from an existing campaign without solving.")
    redraw.add_argument("directory", type=Path)
    redraw.set_defaults(func=_plot_campaign)
    bench = sub.add_parser("benchmark", help="Run a JSON campaign, including exact methods when configured.")
    bench.add_argument("instances", nargs="*", type=Path)
    bench.add_argument("--config", type=Path)
    bench.add_argument("--methods", nargs="+", choices=BENCHMARK_METHODS, default=list(BENCHMARK_METHODS))
    bench.add_argument("--p-values", nargs="+", type=int)
    bench.add_argument("--alpha", type=float, default=1.0)
    bench.add_argument("--seed", type=int, default=0)
    bench.add_argument("--seeds", nargs="+", type=int)
    bench.add_argument("--local-iterations", type=int, default=100)
    bench.add_argument("--tabu-iterations", type=int, default=100)
    bench.add_argument("--tabu-tenure", type=int, default=20)
    bench.add_argument("--candidates-per-iteration", type=int, default=15)
    bench.add_argument("--exact-time-limit", type=float, default=10)
    bench.add_argument("--exact-max-n", type=int, default=22)
    bench.add_argument("--search-time-limit", type=float)
    bench.add_argument("--output-root", type=Path, default=Path("outputs"))
    bench.add_argument("--output", "-o", type=Path, help="Optional additional CSV export.")
    bench.add_argument("--no-plots", action="store_true")
    bench.set_defaults(func=_benchmark)
    compare = sub.add_parser("compare-benchmarks", help="Import legacy CSVs; new campaigns export summaries directly.")
    compare.add_argument("--greedy-csv", type=Path, default=Path("outputs/results/benchmarks/heuristique_gloutonne.csv"))
    compare.add_argument("--meta-csv", type=Path, default=Path("outputs/results/benchmarks/metaheuristiques.csv"))
    compare.add_argument("--exact-csv", type=Path, default=Path("outputs/results/benchmarks/resolution_exacte.csv"))
    compare.add_argument("--output", "-o", type=Path)
    compare.add_argument("--figures-dir", type=Path)
    compare.set_defaults(func=_compare)
    plots = sub.add_parser("plot-benchmark-solutions", help="Import CSVs containing complete saved cycles.")
    plots.add_argument("--csv", action="append", type=Path, required=True)
    plots.add_argument("--instances-dir", type=Path, default=Path("data/instances"))
    plots.add_argument("--output-dir", "-o", type=Path, default=Path("outputs/imported_figures"))
    plots.add_argument("--tsp-exact-cycle-limit", type=int, default=18, help=argparse.SUPPRESS)
    plots.set_defaults(func=_plot_benchmark)
    return parser


def _normalize_time_limit(value: float | None) -> float | None:
    if value == 0:
        return None
    return value


def _solve(args: argparse.Namespace) -> int:
    method = RUN_METHOD_ALIASES[args.method]
    instance = load_tsplib_instance(args.instance)
    problem = RingStarProblem(instance, args.p, args.alpha)
    config = RunConfig(method, args.seed, args.iterations, args.tabu_tenure, args.candidates_per_iteration,
                       _normalize_time_limit(args.time_limit) if method == "exact_plne" else None,
                       args.search_time_limit)
    result = execute(problem, config)
    if args.solver_message and result.solver_log:
        print(result.solver_log)
    print(f"Instance: {instance.name}\nmethod: {method}\nn: {instance.n}\np: {problem.p}\nalpha: {problem.alpha}")
    print(f"status: {'Optimal' if result.optimal else result.status}\nelapsed_seconds: {result.elapsed_seconds:.6f}")
    for key, value in result.details.items():
        print(f"{key}: {value}")
    if result.solution is not None:
        solution = result.solution
        costs = solution.costs(build_distance_matrix(instance.points), problem.alpha)
        print(f"stations: {[s+1 for s in sorted(solution.stations)]}\ncycle: {[s+1 for s in solution.cycle]}")
        print(f"metro_cost: {costs.metro:.3f}\nwalking_cost: {costs.walking:.3f}\ntotal_cost: {costs.total:.3f}")
    if args.command == "run":
        folder = save_run(problem, result, output_root=args.output_root, make_plots=not args.no_plots,
                          show_labels=args.labels, source_path=args.instance)
        print(f"result: {folder/'solution.json'}\nsummary: {folder/'summary.md'}")
    if args.plot or args.plot_output:
        if result.solution is None:
            raise ValueError("No feasible solution to plot.")
        path = args.plot_output or args.output_root / "explicit_plot.png"
        save_solution_png(instance, result.solution, path, title=METHOD_LABELS[method],
                          show_labels=args.labels, problem=problem, status=result.status)
        print(f"plot: {path}")
    if args.save_result or args.result_output:
        path = args.result_output or args.output_root / "explicit_result.json"
        write_json(path, run_data(problem, result))
        text = solution_result_markdown(problem, result.solution, build_distance_matrix(instance.points), method) if result.solution else f"# {result.status}\n\n{result.error}\n"
        path.with_suffix(".md").write_text(text, encoding="utf-8")
        print(f"result: {path}\nsummary: {path.with_suffix('.md')}")
    if result.error:
        print(f"error: {result.error}", file=sys.stderr)
    return 0 if result.solution is not None else 2


def _plot_instance(args) -> int:
    instance = load_tsplib_instance(args.instance)
    path = save_point_cloud_png(instance, args.output or default_point_cloud_output_path(args.instance), args.labels)
    print(path)
    return 0


def _plot_saved(args) -> int:
    problem, solution, data = load_saved_solution(args.solution)
    save_solution_png(problem.instance, solution, args.output, title=METHOD_LABELS[data["method"]],
                      show_labels=args.labels, problem=problem, status=data["status"],
                      elapsed_seconds=data["elapsed_seconds"], seed=data["configuration"]["seed"],
                      formats=("png", "pdf", "svg"))
    print(args.output)
    return 0


def _benchmark(args) -> int:
    if args.config:
        folder = run_campaign(args.config, args.output_root, make_plots=not args.no_plots)
    else:
        paths = args.instances or sorted(Path("data/instances").glob("*.tsp"))
        config = {"name": "cli", "instances": [str(p.resolve()) for p in paths],
                  "methods": args.methods, "alphas": [args.alpha], "seeds": args.seeds or [args.seed],
                  "local_iterations": args.local_iterations, "tabu_iterations": args.tabu_iterations,
                  "tabu_tenure": args.tabu_tenure, "candidates_per_iteration": args.candidates_per_iteration,
                  "search_time_limit": args.search_time_limit,
                  "exact_time_limit": _normalize_time_limit(args.exact_time_limit), "exact_max_n": args.exact_max_n}
        if args.p_values is not None:
            config["p_values"] = args.p_values
        with tempfile.TemporaryDirectory(prefix="ring-star-config-") as tmp:
            path = Path(tmp)/"campaign.json"
            write_json(path, config)
            folder = run_campaign(path, args.output_root, make_plots=not args.no_plots)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes((folder/"runs.csv").read_bytes())
    print(f"benchmark: {folder/'runs.csv'}\nsummary: {folder/'index.md'}")
    return 0


def _plot_campaign(args) -> int:
    paths = replot_campaign(args.directory)
    print(f"figures: {len(paths)}")
    return 0


def _compare(args) -> int:
    path = build_comparison_csv(args.greedy_csv, args.meta_csv, args.exact_csv,
                                args.output or default_comparison_output_path())
    save_benchmark_comparison_plots(path, args.figures_dir or default_comparison_figures_directory())
    print(f"comparison: {path}")
    return 0


def _plot_benchmark(args) -> int:
    paths = []
    for source in args.csv:
        paths.extend(save_solution_plots_from_benchmark_csv(source, args.instances_dir, args.output_dir))
    print(f"plots: {len(paths)}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
