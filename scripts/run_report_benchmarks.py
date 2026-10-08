"""Generate benchmark CSV files used in the report."""

from __future__ import annotations

import argparse
from pathlib import Path

from ring_star.benchmark import run_benchmark, save_benchmark_csv

INSTANCE_PATHS = (
    Path("data/instances/ulysses16.tsp"),
    Path("data/instances/ulysses22.tsp"),
    Path("data/instances/att48.tsp"),
    Path("data/instances/eil51.tsp"),
    Path("data/instances/berlin52.tsp"),
    Path("data/instances/st70.tsp"),
    Path("data/instances/kroA100.tsp"),
    Path("data/instances/rd100.tsp"),
)

P_VALUES_BY_INSTANCE = {
    "ulysses16.tsp": (3, 4, 5, 8, 10, 12),
    "ulysses22.tsp": (3, 4, 5, 8, 10, 15),
    "att48.tsp": (3, 5, 8, 10, 15, 20),
    "eil51.tsp": (3, 5, 8, 10, 15, 20),
    "berlin52.tsp": (3, 5, 8, 10, 15, 20),
    "st70.tsp": (3, 5, 8, 10, 15, 20, 30),
    "kroA100.tsp": (3, 5, 8, 10, 15, 20, 30, 40),
    "rd100.tsp": (3, 5, 8, 10, 15, 20, 30, 40),
}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate report benchmark CSV files.",
    )
    parser.add_argument(
        "mode",
        choices=("greedy", "meta", "all"),
        help="Benchmark group to generate.",
    )
    parser.add_argument("--local-iterations", type=int, default=100)
    parser.add_argument("--tabu-iterations", type=int, default=100)
    parser.add_argument("--candidates-per-iteration", type=int, default=15)
    args = parser.parse_args()

    if args.mode in {"greedy", "all"}:
        greedy_records = []
        for instance_path in INSTANCE_PATHS:
            greedy_records.extend(
                run_benchmark(
                    [instance_path],
                    methods=("greedy",),
                    p_values=P_VALUES_BY_INSTANCE[instance_path.name],
                )
            )
        path = save_benchmark_csv(
            greedy_records,
            "outputs/results/benchmarks/heuristique_gloutonne.csv",
        )
        print(f"{path}: {len(greedy_records)} runs")

    if args.mode in {"meta", "all"}:
        meta_records = []
        for instance_path in INSTANCE_PATHS:
            meta_records.extend(
                run_benchmark(
                    [instance_path],
                    methods=("local_search", "tabu_search"),
                    p_values=P_VALUES_BY_INSTANCE[instance_path.name],
                    local_iterations=args.local_iterations,
                    tabu_iterations=args.tabu_iterations,
                    candidates_per_iteration=args.candidates_per_iteration,
                )
            )
        path = save_benchmark_csv(
            meta_records,
            "outputs/results/benchmarks/metaheuristiques.csv",
        )
        print(f"{path}: {len(meta_records)} runs")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
