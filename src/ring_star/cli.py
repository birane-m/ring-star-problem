"""Command line interface for the Ring-Star project."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from ring_star.distances import build_distance_matrix
from ring_star.heuristics import build_greedy_solution
from ring_star.instance import RingStarProblem
from ring_star.io import load_tsplib_instance
from ring_star.metaheuristics import build_local_search_solution, build_tabu_search_solution
from ring_star.results import save_solution_result_json, save_solution_result_markdown
from ring_star.visualization import save_point_cloud_png, save_solution_png


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


def _to_tsplib_numbers(indices: Sequence[int]) -> list[int]:
    return [index + 1 for index in indices]


if __name__ == "__main__":
    raise SystemExit(main())
