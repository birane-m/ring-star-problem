"""Measured runs, lossless CSV export and alpha-aware legacy comparisons."""
from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from pathlib import Path
from statistics import mean
from typing import Iterable

from ring_star.distances import build_distance_matrix
from ring_star.execution import METHODS, RunConfig, RunResult, execute
from ring_star.instance import RingStarProblem
from ring_star.io import load_tsplib_instance
from ring_star.solution import RingStarSolution
from ring_star.validation import validate_solution

BENCHMARK_METHODS = METHODS
COMPARISON_METHODS = METHODS
SUCCESS = {"ok", "optimal", "Optimal", "feasible_time_limited", "feasible"}


@dataclass(frozen=True)
class BenchmarkRecord:
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
    seed: int = 0
    cycle: tuple[int, ...] = ()
    assignments: tuple[int, ...] = ()
    optimal: bool = False
    lower_bound: float | None = None
    relative_gap: float | None = None
    configuration: dict = field(default_factory=dict)
    solution_file: str = ""
    run_result: RunResult | None = field(default=None, repr=False, compare=False)


def default_benchmark_p_values(n: int) -> tuple[int, ...]:
    return tuple(sorted({p for p in (3, max(3, round(.15*n)), max(3, round(.30*n))) if p <= n}))


def record_from_run(problem: RingStarProblem, result: RunResult, solution_file: str = "") -> BenchmarkRecord:
    from dataclasses import asdict
    solution = result.solution
    costs = solution.costs(build_distance_matrix(problem.instance.points), problem.alpha) if solution else None
    return BenchmarkRecord(
        problem.instance.name, problem.instance.n, problem.p, problem.alpha,
        result.config.method, result.status, costs.total if costs else None,
        costs.metro if costs else None, costs.walking if costs else None,
        result.elapsed_seconds, tuple(s+1 for s in sorted(solution.stations)) if solution else (),
        result.error, result.config.seed,
        tuple(s+1 for s in solution.cycle) if solution else (),
        tuple(s+1 for s in solution.assignments) if solution else (), result.optimal,
        result.lower_bound, result.relative_gap, asdict(result.config), solution_file, result,
    )


def run_benchmark(
    instance_paths: Iterable[str | Path], *, methods: Iterable[str] = BENCHMARK_METHODS,
    p_values: Iterable[int] | None = None, alpha: float = 1.0, seed: int = 0,
    seeds: Iterable[int] | None = None, local_iterations: int | None = None,
    tabu_iterations: int | None = None, tabu_tenure: int = 20,
    candidates_per_iteration: int | None = None, exact_time_limit: float | None = 10,
    exact_max_n: int | None = 22, search_time_limit: float | None = None,
) -> list[BenchmarkRecord]:
    selected_methods = tuple(methods)
    if not selected_methods or set(selected_methods) - set(METHODS):
        raise ValueError("Benchmark methods must be nonempty and supported.")
    ps = tuple(p_values) if p_values is not None else None
    selected_seeds = tuple(seeds) if seeds is not None else (seed,)
    if not selected_seeds or len(set(selected_seeds)) != len(selected_seeds):
        raise ValueError("Seeds must be nonempty and unique.")
    records = []
    for path in instance_paths:
        instance = load_tsplib_instance(path)
        for p in ps if ps is not None else default_benchmark_p_values(instance.n):
            if type(p) is not int or not 3 <= p <= instance.n:
                records.append(BenchmarkRecord(instance.name, instance.n, p, alpha, "input", "skipped",
                                               None, None, None, 0.0, (), "p must satisfy 3 <= p <= n"))
                continue
            problem = RingStarProblem(instance, p, alpha)
            for method in selected_methods:
                if method == "exact_plne" and exact_max_n is not None and instance.n > exact_max_n:
                    records.append(BenchmarkRecord(instance.name, instance.n, p, alpha, method, "skipped",
                                                   None, None, None, 0.0, (), f"n > exact_max_n={exact_max_n}"))
                    continue
                for current_seed in selected_seeds if method in {"local_search", "tabu_search"} else selected_seeds[:1]:
                    config = RunConfig(method=method, seed=current_seed,
                                       iterations=local_iterations if method == "local_search" else tabu_iterations if method == "tabu_search" else None,
                                       tabu_tenure=tabu_tenure, candidates_per_iteration=candidates_per_iteration,
                                       time_limit=exact_time_limit if method == "exact_plne" else None,
                                       search_time_limit=search_time_limit if method in {"local_search", "tabu_search"} else None)
                    records.append(record_from_run(problem, execute(problem, config)))
    return records


CSV_FIELDS = ["instance", "n", "p", "alpha", "method", "status", "total_cost", "metro_cost",
              "walking_cost", "elapsed_seconds", "stations", "error", "seed", "cycle", "assignments",
              "optimal", "lower_bound", "relative_gap", "configuration", "solution_file"]


def save_benchmark_csv(records: Iterable[BenchmarkRecord], output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for record in records:
            row = {key: getattr(record, key) for key in CSV_FIELDS}
            for key in ("stations", "cycle", "assignments"):
                row[key] = " ".join(str(x) for x in row[key])
            row["configuration"] = json.dumps(record.configuration, sort_keys=True)
            for key in ("total_cost", "metro_cost", "walking_cost", "elapsed_seconds", "lower_bound", "relative_gap"):
                row[key] = "" if row[key] is None else f"{row[key]:.12g}"
            writer.writerow(row)
    return path


def build_comparison_csv(greedy_csv: str | Path, metaheuristics_csv: str | Path,
                         exact_csv: str | Path | None, output_path: str | Path) -> Path:
    """Aggregate seeds per (instance, p, alpha); retain all runs in source CSVs.

    This importer is for older CSVs as well. New campaigns also export full
    distribution summaries; duplicate seed/method rows are rejected.
    """
    cases: dict[tuple[str, int, float], dict] = {}
    seen = set()
    for source in (greedy_csv, metaheuristics_csv, exact_csv):
        if source is None or not Path(source).exists():
            continue
        for row in _read_csv_rows(source):
            key = (row["instance"].removesuffix(".tsp"), int(row["p"]), float(row["alpha"]))
            case = cases.setdefault(key, {"instance": key[0], "n": row["n"], "p": key[1], "alpha": key[2], "exact_status": "", "samples": {}})
            method = row["method"]
            if method == "exact_plne":
                case["exact_status"] = row["status"]
            if method not in METHODS or row["status"] not in SUCCESS:
                continue
            run_key = (*key, method, row.get("seed", "0"))
            if run_key in seen:
                raise ValueError(f"Duplicate method/seed row in comparison: {run_key}.")
            seen.add(run_key)
            case["samples"].setdefault(method, []).append((float(row["total_cost"]), float(row["elapsed_seconds"])))
    rows = []
    for case in cases.values():
        samples = case.pop("samples")
        costs = {}
        for method, values in samples.items():
            costs[method] = mean(x[0] for x in values)
            case[f"{method}_cost"] = f"{costs[method]:.6f}"
            case[f"{method}_time"] = f"{mean(x[1] for x in values):.6f}"
        best_method = min(costs, key=costs.get) if costs else ""
        best = costs.get(best_method)
        greedy = costs.get("greedy")
        case.update(best_method=best_method, best_cost="" if best is None else f"{best:.6f}",
                    gain_best_vs_greedy_percent="" if best is None or greedy is None or greedy <= 0 else f"{(greedy-best)/greedy*100:.6f}")
        rows.append(case)
    fields = ["instance", "n", "p", "alpha", *(f"{m}_cost" for m in METHODS), *(f"{m}_time" for m in METHODS),
              "exact_status", "best_method", "best_cost", "gain_best_vs_greedy_percent"]
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: (int(r["n"]), r["instance"], r["alpha"], r["p"])))
    return path


def _read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def save_benchmark_comparison_plots(comparison_csv: str | Path, output_directory: str | Path) -> list[Path]:
    from ring_star.experiment_plots import plot_legacy_comparison
    return plot_legacy_comparison(_read_csv_rows(comparison_csv), Path(output_directory))


def save_solution_plots_from_benchmark_csv(
    benchmark_csv: str | Path, instances_directory: str | Path, output_directory: str | Path,
    *, tsp_exact_cycle_limit: int = 18,
) -> list[Path]:
    """Plot the saved cycle, never a reconstructed or re-optimized surrogate.

    Older CSVs without a cycle must first be regenerated with the revised code.
    The deprecated tsp_exact_cycle_limit argument is ignored for compatibility.
    """
    from ring_star.visualization import save_solution_png
    paths = {}
    for path in Path(instances_directory).glob("*.tsp"):
        instance = load_tsplib_instance(path)
        for key in (path.name, path.stem, instance.name):
            paths[key] = path
    saved = []
    for row in _read_csv_rows(benchmark_csv):
        if row["status"] not in SUCCESS:
            continue
        if not row.get("cycle") or not row.get("assignments"):
            raise ValueError("CSV has no saved cycle/assignments. Regenerate this benchmark before plotting.")
        if row["instance"] not in paths:
            raise ValueError(f"Missing instance: {row['instance']}.")
        instance = load_tsplib_instance(paths[row["instance"]])
        problem = RingStarProblem(instance, int(row["p"]), float(row["alpha"]))
        solution = RingStarSolution(*(tuple(int(x)-1 for x in row[key].split()) for key in ("stations", "cycle", "assignments")))
        validate_solution(problem, solution)
        value = solution.costs(build_distance_matrix(instance.points), problem.alpha).total
        if abs(value - float(row["total_cost"])) > 1e-7 * max(1., abs(value)):
            raise ValueError("CSV cost differs from the saved solution.")
        from ring_star.artifacts import slug
        name = f"{slug(instance.name)}_p{problem.p}_a{problem.alpha:g}_{row['method']}_seed{row.get('seed', '0')}.png"
        path = Path(output_directory) / row["method"] / name
        saved.append(save_solution_png(instance, solution, path, problem=problem, status=row["status"]))
    return saved
