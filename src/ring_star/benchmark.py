"""Benchmark helpers for comparing Ring-Star solution methods."""

from __future__ import annotations

import csv
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from ring_star.distances import build_distance_matrix
from ring_star.exact import ExactSolveError, ExactSolverUnavailableError, solve_exact_solution
from ring_star.heuristics import (
    assign_to_nearest_station,
    build_greedy_solution,
    nearest_neighbor_cycle,
    two_opt_cycle,
)
from ring_star.instance import RingStarProblem
from ring_star.io import load_tsplib_instance
from ring_star.metaheuristics import build_local_search_solution, build_tabu_search_solution
from ring_star.solution import RingStarSolution
from ring_star.visualization import save_solution_png

BENCHMARK_METHODS = ("greedy", "local_search", "tabu_search", "exact_plne")
COMPARISON_METHODS = ("greedy", "local_search", "tabu_search", "exact_plne")


@dataclass(frozen=True)
class BenchmarkRecord:
    """One method run on one instance and one value of p."""

    instance: str
    n: int
    p: int
    alpha: float
    method: str
    status: str
    total_cost: float | None
    metro_cost: float | None
    walking_cost: float | None
    elapsed_seconds: float
    stations: tuple[int, ...]
    error: str | None = None


def default_benchmark_p_values(n: int) -> tuple[int, ...]:
    """Return increasing representative p values for an instance size."""

    candidates = {
        3,
        max(3, round(0.15 * n)),
        max(3, round(0.30 * n)),
    }
    return tuple(sorted(p for p in candidates if 3 <= p <= n))


def run_benchmark(
    instance_paths: Iterable[str | Path],
    *,
    methods: Iterable[str] = BENCHMARK_METHODS,
    p_values: Iterable[int] | None = None,
    alpha: float = 1.0,
    seed: int = 0,
    local_iterations: int | None = None,
    tabu_iterations: int | None = None,
    tabu_tenure: int = 20,
    candidates_per_iteration: int | None = None,
    exact_time_limit: int | None = 10,
    exact_max_n: int | None = 22,
) -> list[BenchmarkRecord]:
    """Run several methods on several instances and p values."""

    selected_methods = tuple(methods)
    _validate_methods(selected_methods)
    records: list[BenchmarkRecord] = []

    for instance_path in instance_paths:
        instance = load_tsplib_instance(instance_path)
        selected_p_values = (
            tuple(p_values)
            if p_values is not None
            else default_benchmark_p_values(instance.n)
        )

        for p in selected_p_values:
            if not 3 <= p <= instance.n:
                records.append(
                    BenchmarkRecord(
                        instance=instance.name,
                        n=instance.n,
                        p=p,
                        alpha=alpha,
                        method="input",
                        status="skipped",
                        total_cost=None,
                        metro_cost=None,
                        walking_cost=None,
                        elapsed_seconds=0.0,
                        stations=(),
                        error="p must satisfy 3 <= p <= n",
                    )
                )
                continue

            problem = RingStarProblem(instance=instance, p=p, alpha=alpha)
            for method in selected_methods:
                records.append(
                    _run_one_method(
                        problem,
                        method=method,
                        seed=seed,
                        local_iterations=local_iterations,
                        tabu_iterations=tabu_iterations,
                        tabu_tenure=tabu_tenure,
                        candidates_per_iteration=candidates_per_iteration,
                        exact_time_limit=exact_time_limit,
                        exact_max_n=exact_max_n,
                    )
                )

    return records


def save_benchmark_csv(records: Iterable[BenchmarkRecord], output_path: str | Path) -> Path:
    """Write benchmark records as a CSV file."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "instance",
        "n",
        "p",
        "alpha",
        "method",
        "status",
        "total_cost",
        "metro_cost",
        "walking_cost",
        "elapsed_seconds",
        "stations",
        "error",
    ]
    with output_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    "instance": record.instance,
                    "n": record.n,
                    "p": record.p,
                    "alpha": record.alpha,
                    "method": record.method,
                    "status": record.status,
                    "total_cost": _format_optional_float(record.total_cost),
                    "metro_cost": _format_optional_float(record.metro_cost),
                    "walking_cost": _format_optional_float(record.walking_cost),
                    "elapsed_seconds": f"{record.elapsed_seconds:.6f}",
                    "stations": " ".join(str(station) for station in record.stations),
                    "error": record.error or "",
                }
            )
    return output_path


def build_comparison_csv(
    greedy_csv: str | Path,
    metaheuristics_csv: str | Path,
    exact_csv: str | Path | None,
    output_path: str | Path,
) -> Path:
    """Merge benchmark CSV files into one comparison table."""

    rows_by_case: dict[tuple[str, int], dict[str, str]] = {}
    for source_path in (greedy_csv, metaheuristics_csv, exact_csv):
        if source_path is None:
            continue
        path = Path(source_path)
        if not path.exists():
            continue
        for row in _read_csv_rows(path):
            if row["status"] not in {"ok", "optimal", "feasible_time_limited"}:
                _ensure_case(rows_by_case, row)
                rows_by_case[(row["instance"], int(row["p"]))]["exact_status"] = row["status"]
                continue

            case = _ensure_case(rows_by_case, row)
            method = row["method"]
            if method not in COMPARISON_METHODS:
                continue
            case[f"{method}_cost"] = row["total_cost"]
            case[f"{method}_time"] = row["elapsed_seconds"]
            if method == "exact_plne":
                case["exact_status"] = row["status"]

    comparison_rows = []
    for case in rows_by_case.values():
        costs = {
            method: _optional_float(case.get(f"{method}_cost"))
            for method in COMPARISON_METHODS
        }
        available_costs = {
            method: cost
            for method, cost in costs.items()
            if cost is not None
        }
        if available_costs:
            best_method = min(available_costs, key=available_costs.get)
            best_cost = available_costs[best_method]
        else:
            best_method = ""
            best_cost = None

        greedy_cost = costs["greedy"]
        gain = (
            (greedy_cost - best_cost) / greedy_cost * 100
            if greedy_cost is not None and best_cost is not None and greedy_cost > 0
            else None
        )
        comparison_rows.append(
            {
                **case,
                "best_method": best_method,
                "best_cost": _format_optional_float(best_cost),
                "gain_best_vs_greedy_percent": _format_optional_float(gain),
            }
        )

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "instance",
        "n",
        "p",
        "alpha",
        "greedy_cost",
        "local_search_cost",
        "tabu_search_cost",
        "exact_plne_cost",
        "greedy_time",
        "local_search_time",
        "tabu_search_time",
        "exact_plne_time",
        "exact_status",
        "best_method",
        "best_cost",
        "gain_best_vs_greedy_percent",
    ]
    with output_path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in sorted(
            comparison_rows,
            key=lambda item: (int(item["n"]), item["instance"], int(item["p"])),
        ):
            writer.writerow({field: row.get(field, "") for field in fieldnames})
    return output_path


def save_benchmark_comparison_plots(
    comparison_csv: str | Path,
    output_directory: str | Path,
) -> list[Path]:
    """Generate report-ready PNG plots from a comparison CSV file."""

    os.environ.setdefault("MPLCONFIGDIR", ".matplotlib-cache")

    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as error:
        raise RuntimeError(
            "matplotlib is required to generate benchmark comparison plots."
        ) from error

    rows = _read_csv_rows(comparison_csv)
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)

    saved_paths = [
        _plot_cost_by_p(rows, output_directory / "cout_total_par_p.png", plt),
        _plot_runtime_by_p(rows, output_directory / "temps_calcul_par_p.png", plt),
        _plot_gain_by_instance(rows, output_directory / "gain_meta_vs_glouton.png", plt),
    ]
    return saved_paths


def save_solution_plots_from_benchmark_csv(
    benchmark_csv: str | Path,
    instances_directory: str | Path,
    output_directory: str | Path,
    *,
    tsp_exact_cycle_limit: int = 18,
) -> list[Path]:
    """Generate one solution PNG per successful row in a benchmark CSV.

    Benchmark CSV files store the selected stations, not the complete cycle.
    For visualization, the assignments are rebuilt by nearest station and the
    metro cycle is rebuilt on the selected stations.  For small station sets,
    the cycle is the exact TSP cycle over those stations; otherwise it falls
    back to nearest-neighbor plus 2-opt.
    """

    instances_directory = Path(instances_directory)
    output_directory = Path(output_directory)
    rows = _read_csv_rows(benchmark_csv)
    instance_paths = {
        path.stem: path
        for path in instances_directory.glob("*.tsp")
    }
    instance_paths.update(
        {
            path.name: path
            for path in instances_directory.glob("*.tsp")
        }
    )
    saved_paths: list[Path] = []

    for row in rows:
        if row.get("status") not in {"ok", "optimal", "feasible_time_limited"}:
            continue
        if not row.get("stations"):
            continue

        instance_path = instance_paths.get(row["instance"])
        if instance_path is None:
            instance_path = instance_paths.get(Path(row["instance"]).stem)
        if instance_path is None:
            continue

        instance = load_tsplib_instance(instance_path)
        distances = build_distance_matrix(instance.points)
        stations = frozenset(int(station) - 1 for station in row["stations"].split())
        assignments = assign_to_nearest_station(stations, distances)
        cycle = _cycle_for_visualization(
            stations,
            distances,
            instance.required_station,
            tsp_exact_cycle_limit=tsp_exact_cycle_limit,
            use_exact_cycle=row["method"] == "exact_plne",
        )
        solution = RingStarSolution(stations, cycle, assignments)
        method = row["method"]
        output_path = (
            output_directory
            / method
            / f"{Path(row['instance']).stem}_p{row['p']}_{method}.png"
        )
        saved_paths.append(
            save_solution_png(
                instance,
                solution,
                output_path,
                title=f"{_method_label(method)} - {instance.name} - p={row['p']}",
            )
        )

    return saved_paths


def _run_one_method(
    problem: RingStarProblem,
    *,
    method: str,
    seed: int,
    local_iterations: int | None,
    tabu_iterations: int | None,
    tabu_tenure: int,
    candidates_per_iteration: int | None,
    exact_time_limit: int | None,
    exact_max_n: int | None,
) -> BenchmarkRecord:
    if method == "exact_plne" and exact_max_n is not None and problem.instance.n > exact_max_n:
        return BenchmarkRecord(
            instance=problem.instance.name,
            n=problem.instance.n,
            p=problem.p,
            alpha=problem.alpha,
            method=method,
            status="skipped",
            total_cost=None,
            metro_cost=None,
            walking_cost=None,
            elapsed_seconds=0.0,
            stations=(),
            error=f"n is greater than exact_max_n={exact_max_n}",
        )

    start = time.perf_counter()
    try:
        distances = build_distance_matrix(problem.instance.points)
        if method == "greedy":
            solution = build_greedy_solution(problem)
            status = "ok"
        elif method == "local_search":
            solution = build_local_search_solution(
                problem,
                iterations=local_iterations,
                seed=seed,
            ).best_solution
            status = "ok"
        elif method == "tabu_search":
            solution = build_tabu_search_solution(
                problem,
                iterations=tabu_iterations,
                seed=seed,
                tabu_tenure=tabu_tenure,
                candidates_per_iteration=candidates_per_iteration,
            ).best_solution
            status = "ok"
        elif method == "exact_plne":
            exact_result = solve_exact_solution(
                problem,
                time_limit=exact_time_limit,
                solver_message=False,
            )
            solution = exact_result.solution
            status = exact_result.status.lower()
        else:
            raise ValueError(f"Unsupported benchmark method: {method}")

        costs = solution.costs(distances, problem.alpha)
        elapsed = time.perf_counter() - start
        return BenchmarkRecord(
            instance=problem.instance.name,
            n=problem.instance.n,
            p=problem.p,
            alpha=problem.alpha,
            method=method,
            status=status,
            total_cost=costs.total,
            metro_cost=costs.metro,
            walking_cost=costs.walking,
            elapsed_seconds=elapsed,
            stations=tuple(station + 1 for station in sorted(solution.stations)),
        )
    except (ExactSolveError, ExactSolverUnavailableError, ValueError) as error:
        elapsed = time.perf_counter() - start
        return BenchmarkRecord(
            instance=problem.instance.name,
            n=problem.instance.n,
            p=problem.p,
            alpha=problem.alpha,
            method=method,
            status="error",
            total_cost=None,
            metro_cost=None,
            walking_cost=None,
            elapsed_seconds=elapsed,
            stations=(),
            error=str(error),
        )


def _validate_methods(methods: tuple[str, ...]) -> None:
    unknown_methods = sorted(set(methods) - set(BENCHMARK_METHODS))
    if unknown_methods:
        raise ValueError(f"Unsupported methods: {', '.join(unknown_methods)}")


def _format_optional_float(value: float | None) -> str:
    if value is None:
        return ""
    return f"{value:.6f}"


def _read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(encoding="utf-8", newline="") as csv_file:
        return list(csv.DictReader(csv_file))


def _ensure_case(
    rows_by_case: dict[tuple[str, int], dict[str, str]],
    source_row: dict[str, str],
) -> dict[str, str]:
    key = (source_row["instance"], int(source_row["p"]))
    if key not in rows_by_case:
        rows_by_case[key] = {
            "instance": source_row["instance"],
            "n": source_row["n"],
            "p": source_row["p"],
            "alpha": source_row["alpha"],
            "exact_status": "",
        }
    elif not rows_by_case[key].get("n") and source_row.get("n"):
        rows_by_case[key]["n"] = source_row["n"]
    return rows_by_case[key]


def _optional_float(value: str | None) -> float | None:
    if value in (None, ""):
        return None
    return float(value)


def _rows_by_instance(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["instance"], []).append(row)
    return {
        instance: sorted(instance_rows, key=lambda row: int(row["p"]))
        for instance, instance_rows in sorted(
            grouped.items(),
            key=lambda item: (int(item[1][0]["n"] or 0), item[0]),
        )
    }


def _plot_cost_by_p(rows: list[dict[str, str]], output_path: Path, plt) -> Path:
    methods = (
        ("greedy", "Gloutonne", "#2563eb"),
        ("local_search", "Recherche locale", "#16a34a"),
        ("tabu_search", "Recherche tabou", "#dc2626"),
        ("exact_plne", "PLNE exact", "#7c3aed"),
    )
    grouped = _rows_by_instance(rows)
    fig, axes = plt.subplots(2, 4, figsize=(18, 8.5), sharex=False, sharey=False)
    for ax, (instance, instance_rows) in zip(axes.flat, grouped.items()):
        ps = [int(row["p"]) for row in instance_rows]
        for method, label, color in methods:
            values = [_optional_float(row.get(f"{method}_cost")) for row in instance_rows]
            plotted = [(p, value) for p, value in zip(ps, values) if value is not None]
            if plotted:
                ax.plot(
                    [p for p, _ in plotted],
                    [value for _, value in plotted],
                    marker="o",
                    linewidth=1.7,
                    markersize=3.8,
                    label=label,
                    color=color,
                )
        ax.set_title(instance)
        ax.set_xlabel("Nombre de stations p")
        ax.set_ylabel("Coût total")
        ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.35)

    for ax in axes.flat[len(grouped):]:
        ax.axis("off")

    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=4, bbox_to_anchor=(0.5, 0.975))
    fig.suptitle("Comparaison des coûts totaux par méthode", y=0.93)
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def _plot_runtime_by_p(rows: list[dict[str, str]], output_path: Path, plt) -> Path:
    methods = (
        ("greedy", "Gloutonne", "#2563eb"),
        ("local_search", "Recherche locale", "#16a34a"),
        ("tabu_search", "Recherche tabou", "#dc2626"),
        ("exact_plne", "PLNE exact", "#7c3aed"),
    )
    grouped = _rows_by_instance(rows)
    fig, axes = plt.subplots(2, 4, figsize=(18, 8.5), sharex=False, sharey=False)
    for ax, (instance, instance_rows) in zip(axes.flat, grouped.items()):
        ps = [int(row["p"]) for row in instance_rows]
        for method, label, color in methods:
            values = [_optional_float(row.get(f"{method}_time")) for row in instance_rows]
            plotted = [(p, value) for p, value in zip(ps, values) if value is not None]
            if plotted:
                ax.plot(
                    [p for p, _ in plotted],
                    [max(value, 1e-4) for _, value in plotted],
                    marker="o",
                    linewidth=1.7,
                    markersize=3.8,
                    label=label,
                    color=color,
                )
        ax.set_yscale("log")
        ax.set_title(instance)
        ax.set_xlabel("Nombre de stations p")
        ax.set_ylabel("Temps de calcul (s, log)")
        ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.35)

    for ax in axes.flat[len(grouped):]:
        ax.axis("off")

    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=4, bbox_to_anchor=(0.5, 0.975))
    fig.suptitle("Comparaison des temps de calcul", y=0.93)
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def _plot_gain_by_instance(rows: list[dict[str, str]], output_path: Path, plt) -> Path:
    labels = []
    gains = []
    for row in rows:
        greedy = _optional_float(row.get("greedy_cost"))
        local = _optional_float(row.get("local_search_cost"))
        tabu = _optional_float(row.get("tabu_search_cost"))
        meta_values = [value for value in (local, tabu) if value is not None]
        if greedy is None or not meta_values:
            continue
        labels.append(f"{row['instance']}\np={row['p']}")
        gains.append((greedy - min(meta_values)) / greedy * 100)

    fig, ax = plt.subplots(figsize=(18, 7))
    colors = ["#16a34a" if gain >= 0 else "#dc2626" for gain in gains]
    ax.bar(range(len(gains)), gains, color=colors)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=75, ha="right", fontsize=8)
    ax.set_ylabel("Gain du meilleur métaheuristique vs glouton (%)")
    ax.set_title("Amélioration apportée par les métaheuristiques")
    ax.grid(True, axis="y", linestyle="--", linewidth=0.5, alpha=0.35)
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    plt.close(fig)
    return output_path


def _cycle_for_visualization(
    stations: frozenset[int],
    distances,
    required_station: int,
    *,
    tsp_exact_cycle_limit: int,
    use_exact_cycle: bool,
) -> tuple[int, ...]:
    if use_exact_cycle and len(stations) <= tsp_exact_cycle_limit:
        return _exact_station_cycle(stations, distances, required_station)
    return two_opt_cycle(
        nearest_neighbor_cycle(stations, distances, required_station),
        distances,
    )


def _exact_station_cycle(
    stations: frozenset[int],
    distances,
    required_station: int,
) -> tuple[int, ...]:
    other_stations = tuple(sorted(stations - {required_station}))
    if not other_stations:
        return (required_station,)

    # Held-Karp dynamic programming over the selected stations only.
    costs: dict[tuple[int, int], tuple[float, int | None]] = {}
    for index, station in enumerate(other_stations):
        costs[(1 << index, index)] = (distances[required_station][station], None)

    for mask in range(1, 1 << len(other_stations)):
        for last_index, last_station in enumerate(other_stations):
            if not mask & (1 << last_index):
                continue
            previous_mask = mask ^ (1 << last_index)
            if previous_mask == 0:
                continue
            best_previous = min(
                (
                    (
                        costs[(previous_mask, previous_index)][0]
                        + distances[other_stations[previous_index]][last_station],
                        previous_index,
                    )
                    for previous_index in range(len(other_stations))
                    if previous_mask & (1 << previous_index)
                ),
                key=lambda item: (item[0], other_stations[item[1]]),
            )
            costs[(mask, last_index)] = best_previous

    full_mask = (1 << len(other_stations)) - 1
    best_total, last_index = min(
        (
            (
                costs[(full_mask, index)][0]
                + distances[other_stations[index]][required_station],
                index,
            )
            for index in range(len(other_stations))
        ),
        key=lambda item: (item[0], other_stations[item[1]]),
    )
    _ = best_total

    reversed_cycle = []
    mask = full_mask
    current_index: int | None = last_index
    while current_index is not None:
        reversed_cycle.append(other_stations[current_index])
        _, previous_index = costs[(mask, current_index)]
        mask ^= 1 << current_index
        current_index = previous_index

    return (required_station, *reversed(reversed_cycle))


def _method_label(method: str) -> str:
    return {
        "greedy": "Heuristique gloutonne",
        "local_search": "Recherche locale",
        "tabu_search": "Recherche tabou",
        "exact_plne": "PLNE exact",
    }.get(method, method)
