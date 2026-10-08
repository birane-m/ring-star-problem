"""Command line interface for the Ring-Star project."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from ring_star.benchmark import (
    BENCHMARK_METHODS,
    build_comparison_csv,
    run_benchmark,
    save_benchmark_csv,
    save_benchmark_comparison_plots,
    save_solution_plots_from_benchmark_csv,
)
from ring_star.distances import build_distance_matrix
from ring_star.exact import (
    ExactSolveError,
    ExactSolverUnavailableError,
    solve_exact_solution,
)
from ring_star.heuristics import build_greedy_solution
from ring_star.instance import RingStarProblem
from ring_star.io import load_tsplib_instance
from ring_star.metaheuristics import build_local_search_solution, build_tabu_search_solution
from ring_star.results import save_solution_result_json, save_solution_result_markdown
from ring_star.visualization import save_point_cloud_png, save_solution_png

RUN_METHOD_ALIASES = {
    "greedy": "greedy",
    "gloutonne": "greedy",
    "heuristique": "greedy",
    "local": "local_search",
    "local-search": "local_search",
    "local_search": "local_search",
    "locale": "local_search",
    "meta": "tabu_search",
    "metaheuristique": "tabu_search",
    "tabou": "tabu_search",
    "tabu": "tabu_search",
    "tabu-search": "tabu_search",
    "tabu_search": "tabu_search",
    "exact": "exact_plne",
    "plne": "exact_plne",
    "exact_plne": "exact_plne",
}


def default_point_cloud_output_path(instance_path: str | Path) -> Path:
    """Return the default PNG path for an instance point cloud."""

    return Path("outputs") / "figures" / "instances" / f"{Path(instance_path).stem}.png"


def default_greedy_solution_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default PNG path for a greedy solution plot."""

    return (
        Path("outputs")
        / "figures"
        / "heuristics"
        / f"{Path(instance_path).stem}_greedy_p{p}.png"
    )


def default_greedy_result_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default JSON path for a greedy solution result."""

    return (
        Path("outputs")
        / "results"
        / "heuristics"
        / f"{Path(instance_path).stem}_greedy_p{p}.json"
    )


def default_greedy_result_markdown_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default Markdown path for a greedy solution result."""

    return default_greedy_result_output_path(instance_path, p).with_suffix(".md")


def default_local_search_solution_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default PNG path for a local search solution plot."""

    return (
        Path("outputs")
        / "figures"
        / "metaheuristics"
        / f"{Path(instance_path).stem}_local_search_p{p}.png"
    )


def default_local_search_result_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default JSON path for a local search result."""

    return (
        Path("outputs")
        / "results"
        / "metaheuristics"
        / f"{Path(instance_path).stem}_local_search_p{p}.json"
    )


def default_tabu_solution_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default PNG path for a tabu search solution plot."""

    return (
        Path("outputs")
        / "figures"
        / "metaheuristics"
        / f"{Path(instance_path).stem}_tabu_p{p}.png"
    )


def default_tabu_result_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default JSON path for a tabu search result."""

    return (
        Path("outputs")
        / "results"
        / "metaheuristics"
        / f"{Path(instance_path).stem}_tabu_p{p}.json"
    )


def default_exact_solution_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default PNG path for an exact PLNE solution plot."""

    return (
        Path("outputs")
        / "figures"
        / "exact"
        / f"{Path(instance_path).stem}_exact_p{p}.png"
    )


def default_exact_result_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default JSON path for an exact PLNE result."""

    return (
        Path("outputs")
        / "results"
        / "exact"
        / f"{Path(instance_path).stem}_exact_p{p}.json"
    )


def default_benchmark_output_path() -> Path:
    """Return the default CSV path for benchmark results."""

    return Path("outputs") / "results" / "benchmarks" / "robustness.csv"


def default_comparison_output_path() -> Path:
    """Return the default CSV path for benchmark comparisons."""

    return Path("outputs") / "results" / "benchmarks" / "comparaison_methodes.csv"


def default_comparison_figures_directory() -> Path:
    """Return the default directory for benchmark comparison PNG figures."""

    return Path("outputs") / "figures" / "benchmarks"


def default_benchmark_solution_figures_directory() -> Path:
    """Return the default directory for benchmark solution PNG figures."""

    return Path("outputs") / "figures" / "benchmark_solutions"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ring-star",
        description="Tools for the Ring-Star optimization problem.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    plot_parser = subparsers.add_parser(
        "plot-instance",
        help="Generate a PNG point-cloud visualization from a TSPLIB instance.",
    )
    plot_parser.add_argument(
        "instance",
        type=Path,
        help="Path to a TSPLIB .tsp instance.",
    )
    plot_parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output PNG path. Defaults to outputs/figures/instances/<instance>.png.",
    )
    plot_parser.add_argument(
        "--labels",
        action="store_true",
        help="Show TSPLIB node numbers on the plot.",
    )
    plot_parser.set_defaults(func=_plot_instance)

    solve_parser = subparsers.add_parser(
        "solve-greedy",
        help="Build a first feasible solution with the greedy heuristic.",
    )
    solve_parser.add_argument(
        "instance",
        type=Path,
        help="Path to a TSPLIB .tsp instance.",
    )
    solve_parser.add_argument(
        "p",
        type=int,
        help="Number of stations to select.",
    )
    solve_parser.add_argument(
        "--alpha",
        type=float,
        default=1.0,
        help="Weight of the metro cycle cost in the objective.",
    )
    solve_parser.add_argument(
        "--plot",
        action="store_true",
        help="Generate a PNG visualization of the greedy solution.",
    )
    solve_parser.add_argument(
        "--plot-output",
        type=Path,
        default=None,
        help="Output PNG path for --plot. Defaults to outputs/figures/heuristics/<instance>_greedy_p<p>.png.",
    )
    solve_parser.add_argument(
        "--labels",
        action="store_true",
        help="Show TSPLIB node numbers on the solution plot.",
    )
    solve_parser.add_argument(
        "--save-result",
        action="store_true",
        help="Save the solution summary as JSON and Markdown files.",
    )
    solve_parser.add_argument(
        "--result-output",
        type=Path,
        default=None,
        help="Output JSON path for --save-result. A Markdown file is also written next to it.",
    )
    solve_parser.set_defaults(func=_solve_greedy)

    local_search_parser = subparsers.add_parser(
        "solve-local-search",
        help="Improve the greedy solution with stochastic station swaps.",
    )
    local_search_parser.add_argument(
        "instance",
        type=Path,
        help="Path to a TSPLIB .tsp instance.",
    )
    local_search_parser.add_argument(
        "p",
        type=int,
        help="Number of stations to select.",
    )
    local_search_parser.add_argument(
        "--alpha",
        type=float,
        default=1.0,
        help="Weight of the metro cycle cost in the objective.",
    )
    local_search_parser.add_argument(
        "--iterations",
        type=int,
        default=None,
        help="Number of sampled swaps. Defaults to max(500, 10*n).",
    )
    local_search_parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Random seed used by the stochastic local search.",
    )
    local_search_parser.add_argument(
        "--plot",
        action="store_true",
        help="Generate a PNG visualization of the local search solution.",
    )
    local_search_parser.add_argument(
        "--plot-output",
        type=Path,
        default=None,
        help="Output PNG path for --plot. Defaults to outputs/figures/metaheuristics/<instance>_local_search_p<p>.png.",
    )
    local_search_parser.add_argument(
        "--labels",
        action="store_true",
        help="Show TSPLIB node numbers on the solution plot.",
    )
    local_search_parser.add_argument(
        "--save-result",
        action="store_true",
        help="Save the solution summary as JSON and Markdown files.",
    )
    local_search_parser.add_argument(
        "--result-output",
        type=Path,
        default=None,
        help="Output JSON path for --save-result. A Markdown file is also written next to it.",
    )
    local_search_parser.set_defaults(func=_solve_local_search)

    tabu_parser = subparsers.add_parser(
        "solve-tabu",
        help="Improve the greedy solution with tabu search.",
    )
    tabu_parser.add_argument(
        "instance",
        type=Path,
        help="Path to a TSPLIB .tsp instance.",
    )
    tabu_parser.add_argument(
        "p",
        type=int,
        help="Number of stations to select.",
    )
    tabu_parser.add_argument(
        "--alpha",
        type=float,
        default=1.0,
        help="Weight of the metro cycle cost in the objective.",
    )
    tabu_parser.add_argument(
        "--iterations",
        type=int,
        default=None,
        help="Number of tabu iterations. Defaults to max(500, 10*n).",
    )
    tabu_parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Random seed used by tabu search.",
    )
    tabu_parser.add_argument(
        "--tabu-tenure",
        type=int,
        default=20,
        help="Number of iterations during which a removed station is tabu.",
    )
    tabu_parser.add_argument(
        "--candidates-per-iteration",
        type=int,
        default=None,
        help="Number of sampled swaps per iteration. Defaults to max(20, n).",
    )
    tabu_parser.add_argument(
        "--plot",
        action="store_true",
        help="Generate a PNG visualization of the tabu solution.",
    )
    tabu_parser.add_argument(
        "--plot-output",
        type=Path,
        default=None,
        help="Output PNG path for --plot. Defaults to outputs/figures/metaheuristics/<instance>_tabu_p<p>.png.",
    )
    tabu_parser.add_argument(
        "--labels",
        action="store_true",
        help="Show TSPLIB node numbers on the solution plot.",
    )
    tabu_parser.add_argument(
        "--save-result",
        action="store_true",
        help="Save the solution summary as JSON and Markdown files.",
    )
    tabu_parser.add_argument(
        "--result-output",
        type=Path,
        default=None,
        help="Output JSON path for --save-result. A Markdown file is also written next to it.",
    )
    tabu_parser.set_defaults(func=_solve_tabu)

    exact_parser = subparsers.add_parser(
        "solve-exact",
        help="Solve the Ring-Star problem exactly with a PLNE model.",
    )
    exact_parser.add_argument(
        "instance",
        type=Path,
        help="Path to a TSPLIB .tsp instance.",
    )
    exact_parser.add_argument(
        "p",
        type=int,
        help="Number of stations to select.",
    )
    exact_parser.add_argument(
        "--alpha",
        type=float,
        default=1.0,
        help="Weight of the metro cycle cost in the objective.",
    )
    exact_parser.add_argument(
        "--time-limit",
        type=int,
        default=None,
        help="CBC time limit in seconds.",
    )
    exact_parser.add_argument(
        "--solver-message",
        action="store_true",
        help="Show solver logs.",
    )
    exact_parser.add_argument(
        "--plot",
        action="store_true",
        help="Generate a PNG visualization of the exact solution.",
    )
    exact_parser.add_argument(
        "--plot-output",
        type=Path,
        default=None,
        help="Output PNG path for --plot. Defaults to outputs/figures/exact/<instance>_exact_p<p>.png.",
    )
    exact_parser.add_argument(
        "--labels",
        action="store_true",
        help="Show TSPLIB node numbers on the solution plot.",
    )
    exact_parser.add_argument(
        "--save-result",
        action="store_true",
        help="Save the solution summary as JSON and Markdown files.",
    )
    exact_parser.add_argument(
        "--result-output",
        type=Path,
        default=None,
        help="Output JSON path for --save-result. A Markdown file is also written next to it.",
    )
    exact_parser.set_defaults(func=_solve_exact)

    run_parser = subparsers.add_parser(
        "run",
        help="Run one method and automatically write JSON, Markdown and PNG outputs.",
    )
    run_parser.add_argument(
        "method",
        choices=sorted(RUN_METHOD_ALIASES),
        help="Method to run: greedy/gloutonne, local, tabu/tabou or exact/plne.",
    )
    run_parser.add_argument(
        "instance",
        type=Path,
        help="Path to a TSPLIB .tsp instance.",
    )
    run_parser.add_argument(
        "p",
        type=int,
        help="Number of stations to select.",
    )
    run_parser.add_argument(
        "--alpha",
        type=float,
        default=1.0,
        help="Weight of the metro cycle cost in the objective.",
    )
    run_parser.add_argument(
        "--iterations",
        type=int,
        default=None,
        help="Iteration budget for local search or tabu search.",
    )
    run_parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Random seed used by stochastic methods.",
    )
    run_parser.add_argument(
        "--tabu-tenure",
        type=int,
        default=20,
        help="Number of iterations during which a removed station is tabu.",
    )
    run_parser.add_argument(
        "--candidates-per-iteration",
        type=int,
        default=None,
        help="Number of sampled tabu moves per iteration.",
    )
    run_parser.add_argument(
        "--time-limit",
        type=int,
        default=None,
        help="CBC time limit in seconds for the exact method.",
    )
    run_parser.add_argument(
        "--solver-message",
        action="store_true",
        help="Show exact solver logs.",
    )
    run_parser.add_argument(
        "--labels",
        action="store_true",
        help="Show TSPLIB node numbers on the solution plot.",
    )
    run_parser.set_defaults(func=_run_method)

    benchmark_parser = subparsers.add_parser(
        "benchmark",
        help="Compare methods on several instances and p values.",
    )
    benchmark_parser.add_argument(
        "instances",
        type=Path,
        nargs="*",
        help="TSPLIB instances. Defaults to data/instances/*.tsp.",
    )
    benchmark_parser.add_argument(
        "--p-values",
        type=int,
        nargs="+",
        default=None,
        help="Values of p to test. Defaults to representative values per instance size.",
    )
    benchmark_parser.add_argument(
        "--methods",
        choices=BENCHMARK_METHODS,
        nargs="+",
        default=list(BENCHMARK_METHODS),
        help="Methods to compare.",
    )
    benchmark_parser.add_argument(
        "--alpha",
        type=float,
        default=1.0,
        help="Weight of the metro cycle cost in the objective.",
    )
    benchmark_parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Random seed used by stochastic methods.",
    )
    benchmark_parser.add_argument(
        "--local-iterations",
        type=int,
        default=None,
        help="Iteration budget for local search.",
    )
    benchmark_parser.add_argument(
        "--tabu-iterations",
        type=int,
        default=None,
        help="Iteration budget for tabu search.",
    )
    benchmark_parser.add_argument(
        "--tabu-tenure",
        type=int,
        default=20,
        help="Number of iterations during which a removed station is tabu.",
    )
    benchmark_parser.add_argument(
        "--candidates-per-iteration",
        type=int,
        default=None,
        help="Number of sampled tabu moves per iteration.",
    )
    benchmark_parser.add_argument(
        "--exact-time-limit",
        type=int,
        default=10,
        help="CBC time limit in seconds for each exact run. Use 0 for no limit.",
    )
    benchmark_parser.add_argument(
        "--exact-max-n",
        type=int,
        default=22,
        help="Skip exact runs for instances larger than this size.",
    )
    benchmark_parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output CSV path. Defaults to outputs/results/benchmarks/robustness.csv.",
    )
    benchmark_parser.set_defaults(func=_benchmark)

    comparison_parser = subparsers.add_parser(
        "compare-benchmarks",
        help="Merge benchmark CSV files and generate comparison plots.",
    )
    comparison_parser.add_argument(
        "--greedy-csv",
        type=Path,
        default=Path("outputs/results/benchmarks/heuristique_gloutonne.csv"),
        help="CSV produced for the greedy heuristic.",
    )
    comparison_parser.add_argument(
        "--meta-csv",
        type=Path,
        default=Path("outputs/results/benchmarks/metaheuristiques.csv"),
        help="CSV produced for local search and tabu search.",
    )
    comparison_parser.add_argument(
        "--exact-csv",
        type=Path,
        default=Path("outputs/results/benchmarks/resolution_exacte.csv"),
        help="CSV produced for exact PLNE runs.",
    )
    comparison_parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output comparison CSV path. Defaults to outputs/results/benchmarks/comparaison_methodes.csv.",
    )
    comparison_parser.add_argument(
        "--figures-dir",
        type=Path,
        default=None,
        help="Output directory for PNG plots. Defaults to outputs/figures/benchmarks.",
    )
    comparison_parser.set_defaults(func=_compare_benchmarks)

    solution_plots_parser = subparsers.add_parser(
        "plot-benchmark-solutions",
        help="Generate solution PNG files from benchmark CSV files.",
    )
    solution_plots_parser.add_argument(
        "--csv",
        type=Path,
        action="append",
        default=None,
        help="Benchmark CSV to plot. Can be repeated. Defaults to the three benchmark CSV files.",
    )
    solution_plots_parser.add_argument(
        "--instances-dir",
        type=Path,
        default=Path("data/instances"),
        help="Directory containing TSPLIB .tsp instances.",
    )
    solution_plots_parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory for PNG plots. Defaults to outputs/figures/benchmark_solutions.",
    )
    solution_plots_parser.add_argument(
        "--tsp-exact-cycle-limit",
        type=int,
        default=18,
        help="Maximum number of stations for exact TSP cycle reconstruction in plots.",
    )
    solution_plots_parser.set_defaults(func=_plot_benchmark_solutions)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


def _plot_instance(args: argparse.Namespace) -> int:
    instance = load_tsplib_instance(args.instance)
    output = args.output or default_point_cloud_output_path(args.instance)
    saved_path = save_point_cloud_png(
        instance,
        output,
        show_labels=args.labels,
    )
    print(saved_path)
    return 0


def _solve_greedy(args: argparse.Namespace) -> int:
    instance = load_tsplib_instance(args.instance)
    problem = RingStarProblem(instance=instance, p=args.p, alpha=args.alpha)
    distances = build_distance_matrix(instance.points)
    solution = build_greedy_solution(problem)
    costs = solution.costs(distances, problem.alpha)

    print(f"Instance: {instance.name}")
    print(f"n: {instance.n}")
    print(f"p: {problem.p}")
    print(f"alpha: {problem.alpha}")
    print(f"stations: {_to_tsplib_numbers(sorted(solution.stations))}")
    print(f"cycle: {_to_tsplib_numbers(solution.cycle)}")
    print(f"metro_cost: {costs.metro:.3f}")
    print(f"walking_cost: {costs.walking:.3f}")
    print(f"total_cost: {costs.total:.3f}")
    saved_plot_path = None
    if args.plot:
        plot_output = args.plot_output or default_greedy_solution_output_path(
            args.instance,
            args.p,
        )
        saved_path = save_solution_png(
            instance,
            solution,
            plot_output,
            title=f"Heuristique gloutonne - {instance.name} - p={problem.p}",
            show_labels=args.labels,
        )
        saved_plot_path = saved_path
        print(f"plot: {saved_path}")
    if args.save_result:
        result_output = args.result_output or default_greedy_result_output_path(
            args.instance,
            args.p,
        )
        saved_result_path = save_solution_result_json(
            problem,
            solution,
            distances,
            method="greedy",
            output_path=result_output,
            plot_path=saved_plot_path,
        )
        markdown_output = saved_result_path.with_suffix(".md")
        saved_markdown_path = save_solution_result_markdown(
            problem,
            solution,
            distances,
            method="greedy",
            output_path=markdown_output,
            plot_path=saved_plot_path,
        )
        print(f"result: {saved_result_path}")
        print(f"summary: {saved_markdown_path}")
    return 0


def _solve_local_search(args: argparse.Namespace) -> int:
    instance = load_tsplib_instance(args.instance)
    problem = RingStarProblem(instance=instance, p=args.p, alpha=args.alpha)
    distances = build_distance_matrix(instance.points)
    result = build_local_search_solution(
        problem,
        iterations=args.iterations,
        seed=args.seed,
    )
    solution = result.best_solution
    costs = solution.costs(distances, problem.alpha)

    print(f"Instance: {instance.name}")
    print(f"n: {instance.n}")
    print(f"p: {problem.p}")
    print(f"alpha: {problem.alpha}")
    print(f"iterations: {result.iterations}")
    print(f"accepted_moves: {result.accepted_moves}")
    print(f"initial_cost: {result.initial_cost:.3f}")
    print(f"best_cost: {result.best_cost:.3f}")
    print(f"stations: {_to_tsplib_numbers(sorted(solution.stations))}")
    print(f"cycle: {_to_tsplib_numbers(solution.cycle)}")
    print(f"metro_cost: {costs.metro:.3f}")
    print(f"walking_cost: {costs.walking:.3f}")
    print(f"total_cost: {costs.total:.3f}")

    saved_plot_path = None
    if args.plot:
        plot_output = args.plot_output or default_local_search_solution_output_path(
            args.instance,
            args.p,
        )
        saved_path = save_solution_png(
            instance,
            solution,
            plot_output,
            title=f"Métaheuristique - {instance.name} - p={problem.p}",
            show_labels=args.labels,
        )
        saved_plot_path = saved_path
        print(f"plot: {saved_path}")

    if args.save_result:
        result_output = args.result_output or default_local_search_result_output_path(
            args.instance,
            args.p,
        )
        saved_result_path = save_solution_result_json(
            problem,
            solution,
            distances,
            method="local_search",
            output_path=result_output,
            plot_path=saved_plot_path,
        )
        saved_markdown_path = save_solution_result_markdown(
            problem,
            solution,
            distances,
            method="local_search",
            output_path=saved_result_path.with_suffix(".md"),
            plot_path=saved_plot_path,
        )
        print(f"result: {saved_result_path}")
        print(f"summary: {saved_markdown_path}")

    return 0


def _solve_tabu(args: argparse.Namespace) -> int:
    instance = load_tsplib_instance(args.instance)
    problem = RingStarProblem(instance=instance, p=args.p, alpha=args.alpha)
    distances = build_distance_matrix(instance.points)
    result = build_tabu_search_solution(
        problem,
        iterations=args.iterations,
        seed=args.seed,
        tabu_tenure=args.tabu_tenure,
        candidates_per_iteration=args.candidates_per_iteration,
    )
    solution = result.best_solution
    costs = solution.costs(distances, problem.alpha)

    print(f"Instance: {instance.name}")
    print(f"n: {instance.n}")
    print(f"p: {problem.p}")
    print(f"alpha: {problem.alpha}")
    print(f"iterations: {result.iterations}")
    print(f"performed_moves: {result.performed_moves}")
    print(f"tabu_tenure: {result.tabu_tenure}")
    print(f"candidates_per_iteration: {result.candidates_per_iteration}")
    print(f"initial_cost: {result.initial_cost:.3f}")
    print(f"best_cost: {result.best_cost:.3f}")
    print(f"stations: {_to_tsplib_numbers(sorted(solution.stations))}")
    print(f"cycle: {_to_tsplib_numbers(solution.cycle)}")
    print(f"metro_cost: {costs.metro:.3f}")
    print(f"walking_cost: {costs.walking:.3f}")
    print(f"total_cost: {costs.total:.3f}")

    saved_plot_path = None
    if args.plot:
        plot_output = args.plot_output or default_tabu_solution_output_path(
            args.instance,
            args.p,
        )
        saved_path = save_solution_png(
            instance,
            solution,
            plot_output,
            title=f"Recherche tabou - {instance.name} - p={problem.p}",
            show_labels=args.labels,
        )
        saved_plot_path = saved_path
        print(f"plot: {saved_path}")

    if args.save_result:
        result_output = args.result_output or default_tabu_result_output_path(
            args.instance,
            args.p,
        )
        saved_result_path = save_solution_result_json(
            problem,
            solution,
            distances,
            method="tabu_search",
            output_path=result_output,
            plot_path=saved_plot_path,
        )
        saved_markdown_path = save_solution_result_markdown(
            problem,
            solution,
            distances,
            method="tabu_search",
            output_path=saved_result_path.with_suffix(".md"),
            plot_path=saved_plot_path,
        )
        print(f"result: {saved_result_path}")
        print(f"summary: {saved_markdown_path}")

    return 0


def _solve_exact(args: argparse.Namespace) -> int:
    instance = load_tsplib_instance(args.instance)
    problem = RingStarProblem(instance=instance, p=args.p, alpha=args.alpha)
    distances = build_distance_matrix(instance.points)

    try:
        result = solve_exact_solution(
            problem,
            time_limit=_normalize_time_limit(args.time_limit),
            solver_message=args.solver_message,
        )
    except (ExactSolverUnavailableError, ExactSolveError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    solution = result.solution
    costs = solution.costs(distances, problem.alpha)

    print(f"Instance: {instance.name}")
    print(f"n: {instance.n}")
    print(f"p: {problem.p}")
    print(f"alpha: {problem.alpha}")
    print(f"solver: {result.solver_name}")
    print(f"status: {result.status}")
    print(f"objective_value: {result.objective_value:.3f}")
    print(f"stations: {_to_tsplib_numbers(sorted(solution.stations))}")
    print(f"cycle: {_to_tsplib_numbers(solution.cycle)}")
    print(f"metro_cost: {costs.metro:.3f}")
    print(f"walking_cost: {costs.walking:.3f}")
    print(f"total_cost: {costs.total:.3f}")

    saved_plot_path = None
    if args.plot:
        plot_output = args.plot_output or default_exact_solution_output_path(
            args.instance,
            args.p,
        )
        saved_path = save_solution_png(
            instance,
            solution,
            plot_output,
            title=f"PLNE exact - {instance.name} - p={problem.p}",
            show_labels=args.labels,
        )
        saved_plot_path = saved_path
        print(f"plot: {saved_path}")

    if args.save_result:
        result_output = args.result_output or default_exact_result_output_path(
            args.instance,
            args.p,
        )
        saved_result_path = save_solution_result_json(
            problem,
            solution,
            distances,
            method="exact_plne",
            output_path=result_output,
            plot_path=saved_plot_path,
        )
        saved_markdown_path = save_solution_result_markdown(
            problem,
            solution,
            distances,
            method="exact_plne",
            output_path=saved_result_path.with_suffix(".md"),
            plot_path=saved_plot_path,
        )
        print(f"result: {saved_result_path}")
        print(f"summary: {saved_markdown_path}")

    return 0


def _run_method(args: argparse.Namespace) -> int:
    method = RUN_METHOD_ALIASES[args.method]
    instance = load_tsplib_instance(args.instance)
    problem = RingStarProblem(instance=instance, p=args.p, alpha=args.alpha)
    distances = build_distance_matrix(instance.points)

    try:
        solution, method_name, title, extra_lines = _build_run_solution(
            method,
            problem,
            args,
        )
    except (ExactSolverUnavailableError, ExactSolveError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    costs = solution.costs(distances, problem.alpha)
    plot_output = _default_run_plot_path(method, args.instance, args.p)
    result_output = _default_run_result_path(method, args.instance, args.p)
    saved_plot_path = save_solution_png(
        instance,
        solution,
        plot_output,
        title=title,
        show_labels=args.labels,
    )
    saved_result_path = save_solution_result_json(
        problem,
        solution,
        distances,
        method=method_name,
        output_path=result_output,
        plot_path=saved_plot_path,
    )
    saved_markdown_path = save_solution_result_markdown(
        problem,
        solution,
        distances,
        method=method_name,
        output_path=saved_result_path.with_suffix(".md"),
        plot_path=saved_plot_path,
    )

    print(f"Instance: {instance.name}")
    print(f"method: {method_name}")
    print(f"n: {instance.n}")
    print(f"p: {problem.p}")
    print(f"alpha: {problem.alpha}")
    for line in extra_lines:
        print(line)
    print(f"stations: {_to_tsplib_numbers(sorted(solution.stations))}")
    print(f"cycle: {_to_tsplib_numbers(solution.cycle)}")
    print(f"metro_cost: {costs.metro:.3f}")
    print(f"walking_cost: {costs.walking:.3f}")
    print(f"total_cost: {costs.total:.3f}")
    print(f"plot: {saved_plot_path}")
    print(f"result: {saved_result_path}")
    print(f"summary: {saved_markdown_path}")
    return 0


def _build_run_solution(
    method: str,
    problem: RingStarProblem,
    args: argparse.Namespace,
):
    if method == "greedy":
        solution = build_greedy_solution(problem)
        return (
            solution,
            "greedy",
            f"Heuristique gloutonne - {problem.instance.name} - p={problem.p}",
            [],
        )

    if method == "local_search":
        result = build_local_search_solution(
            problem,
            iterations=args.iterations,
            seed=args.seed,
        )
        return (
            result.best_solution,
            "local_search",
            f"Recherche locale - {problem.instance.name} - p={problem.p}",
            [
                f"iterations: {result.iterations}",
                f"accepted_moves: {result.accepted_moves}",
                f"initial_cost: {result.initial_cost:.3f}",
                f"best_cost: {result.best_cost:.3f}",
            ],
        )

    if method == "tabu_search":
        result = build_tabu_search_solution(
            problem,
            iterations=args.iterations,
            seed=args.seed,
            tabu_tenure=args.tabu_tenure,
            candidates_per_iteration=args.candidates_per_iteration,
        )
        return (
            result.best_solution,
            "tabu_search",
            f"Recherche tabou - {problem.instance.name} - p={problem.p}",
            [
                f"iterations: {result.iterations}",
                f"performed_moves: {result.performed_moves}",
                f"tabu_tenure: {result.tabu_tenure}",
                f"candidates_per_iteration: {result.candidates_per_iteration}",
                f"initial_cost: {result.initial_cost:.3f}",
                f"best_cost: {result.best_cost:.3f}",
            ],
        )

    result = solve_exact_solution(
        problem,
        time_limit=_normalize_time_limit(args.time_limit),
        solver_message=args.solver_message,
    )
    return (
        result.solution,
        "exact_plne",
        f"PLNE exact - {problem.instance.name} - p={problem.p}",
        [
            f"solver: {result.solver_name}",
            f"status: {result.status}",
            f"objective_value: {result.objective_value:.3f}",
        ],
    )


def _default_run_plot_path(method: str, instance_path: str | Path, p: int) -> Path:
    if method == "greedy":
        return default_greedy_solution_output_path(instance_path, p)
    if method == "local_search":
        return default_local_search_solution_output_path(instance_path, p)
    if method == "tabu_search":
        return default_tabu_solution_output_path(instance_path, p)
    return default_exact_solution_output_path(instance_path, p)


def _default_run_result_path(method: str, instance_path: str | Path, p: int) -> Path:
    if method == "greedy":
        return default_greedy_result_output_path(instance_path, p)
    if method == "local_search":
        return default_local_search_result_output_path(instance_path, p)
    if method == "tabu_search":
        return default_tabu_result_output_path(instance_path, p)
    return default_exact_result_output_path(instance_path, p)


def _normalize_time_limit(time_limit: int | None) -> int | None:
    if time_limit is not None and time_limit <= 0:
        return None
    return time_limit


def _benchmark(args: argparse.Namespace) -> int:
    instance_paths = args.instances or sorted(Path("data/instances").glob("*.tsp"))
    exact_time_limit = (
        None
        if args.exact_time_limit is not None and args.exact_time_limit <= 0
        else args.exact_time_limit
    )
    records = run_benchmark(
        instance_paths,
        methods=args.methods,
        p_values=args.p_values,
        alpha=args.alpha,
        seed=args.seed,
        local_iterations=args.local_iterations,
        tabu_iterations=args.tabu_iterations,
        tabu_tenure=args.tabu_tenure,
        candidates_per_iteration=args.candidates_per_iteration,
        exact_time_limit=exact_time_limit,
        exact_max_n=args.exact_max_n,
    )
    output = save_benchmark_csv(
        records,
        args.output or default_benchmark_output_path(),
    )
    status_counts: dict[str, int] = {}
    for record in records:
        status_counts[record.status] = status_counts.get(record.status, 0) + 1

    print(f"benchmark: {output}")
    print(f"runs: {len(records)}")
    for status, count in sorted(status_counts.items()):
        print(f"{status}: {count}")
    return 0


def _compare_benchmarks(args: argparse.Namespace) -> int:
    output = build_comparison_csv(
        args.greedy_csv,
        args.meta_csv,
        args.exact_csv,
        args.output or default_comparison_output_path(),
    )
    figure_paths = save_benchmark_comparison_plots(
        output,
        args.figures_dir or default_comparison_figures_directory(),
    )

    print(f"comparison: {output}")
    for figure_path in figure_paths:
        print(f"figure: {figure_path}")
    return 0


def _plot_benchmark_solutions(args: argparse.Namespace) -> int:
    csv_paths = args.csv or [
        Path("outputs/results/benchmarks/heuristique_gloutonne.csv"),
        Path("outputs/results/benchmarks/metaheuristiques.csv"),
        Path("outputs/results/benchmarks/resolution_exacte.csv"),
    ]
    output_dir = args.output_dir or default_benchmark_solution_figures_directory()
    saved_paths = []
    for csv_path in csv_paths:
        saved_paths.extend(
            save_solution_plots_from_benchmark_csv(
                csv_path,
                args.instances_dir,
                output_dir,
                tsp_exact_cycle_limit=args.tsp_exact_cycle_limit,
            )
        )

    print(f"solution_plots: {output_dir}")
    print(f"plots: {len(saved_paths)}")
    return 0


def _to_tsplib_numbers(indices: Sequence[int]) -> list[int]:
    return [index + 1 for index in indices]


if __name__ == "__main__":
    raise SystemExit(main())
