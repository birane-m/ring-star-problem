"""Result export helpers for Ring-Star solutions."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ring_star.distances import DistanceMatrix
from ring_star.instance import RingStarProblem
from ring_star.solution import RingStarSolution


def solution_result_data(
    problem: RingStarProblem,
    solution: RingStarSolution,
    distances: DistanceMatrix,
    method: str,
    plot_path: str | Path | None = None,
) -> dict[str, Any]:
    """Build a JSON-serializable result summary for a solution."""

    costs = solution.costs(distances, problem.alpha)
    return {
        "instance": problem.instance.name,
        "n": problem.instance.n,
        "p": problem.p,
        "alpha": problem.alpha,
        "method": method,
        "edge_weight_type": problem.instance.edge_weight_type,
        "required_station": problem.required_station + 1,
        "stations": _to_tsplib_numbers(sorted(solution.stations)),
        "cycle": _to_tsplib_numbers(solution.cycle),
        "assignments": [
            {
                "point": point + 1,
                "station": station + 1,
            }
            for point, station in enumerate(solution.assignments)
        ],
        "costs": {
            "metro": costs.metro,
            "walking": costs.walking,
            "total": costs.total,
        },
        "plot": str(plot_path) if plot_path is not None else None,
    }


def save_solution_result_json(
    problem: RingStarProblem,
    solution: RingStarSolution,
    distances: DistanceMatrix,
    method: str,
    output_path: str | Path,
    plot_path: str | Path | None = None,
) -> Path:
    """Write a solution result summary as JSON."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(
            solution_result_data(
                problem,
                solution,
                distances,
                method,
                plot_path=plot_path,
            ),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return output_path


def save_solution_result_markdown(
    problem: RingStarProblem,
    solution: RingStarSolution,
    distances: DistanceMatrix,
    method: str,
    output_path: str | Path,
    plot_path: str | Path | None = None,
) -> Path:
    """Write a human-readable solution result summary as Markdown."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        solution_result_markdown(
            problem,
            solution,
            distances,
            method,
            plot_path=plot_path,
        ),
        encoding="utf-8",
    )
    return output_path


def solution_result_markdown(
    problem: RingStarProblem,
    solution: RingStarSolution,
    distances: DistanceMatrix,
    method: str,
    plot_path: str | Path | None = None,
) -> str:
    """Return a human-readable Markdown summary for a solution."""

    data = solution_result_data(
        problem,
        solution,
        distances,
        method,
        plot_path=plot_path,
    )
    cycle = data["cycle"]
    cycle_text = " -> ".join(str(station) for station in [*cycle, cycle[0]])
    assignments_by_station = _assignments_by_station(data["assignments"])
    lines = [
        f"# Résultat {method} - {data['instance']}",
        "",
        f"- Instance : {data['instance']}",
        f"- Nombre de points : {data['n']}",
        f"- Nombre de stations : {data['p']}",
        f"- Alpha : {data['alpha']}",
        f"- Station obligatoire : {data['required_station']}",
        f"- Type TSPLIB : {data['edge_weight_type'] or 'non renseigné'}",
        "",
        "## Coûts",
        "",
        f"- Coût métro : {data['costs']['metro']:.3f}",
        f"- Coût marche : {data['costs']['walking']:.3f}",
        f"- Coût total : {data['costs']['total']:.3f}",
        "",
        "## Stations choisies",
        "",
        ", ".join(str(station) for station in data["stations"]),
        "",
        "## Cycle métro",
        "",
        cycle_text,
        "",
        "## Affectations par station",
        "",
        "| Station | Points rattachés | Nombre de points |",
        "|---:|---|---:|",
    ]

    lines.extend(
        f"| {station} | {', '.join(str(point) for point in points)} | {len(points)} |"
        for station, points in assignments_by_station.items()
    )

    lines.extend(
        [
            "",
            "## Affectations détaillées par point",
            "",
            "| Point | Station |",
            "|---:|---:|",
        ]
    )

    lines.extend(
        f"| {assignment['point']} | {assignment['station']} |"
        for assignment in data["assignments"]
    )

    if data["plot"] is not None:
        lines.extend(["", "## Visualisation", "", str(data["plot"])])

    return "\n".join(lines) + "\n"


def _assignments_by_station(
    assignments: list[dict[str, int]],
) -> dict[int, list[int]]:
    grouped: dict[int, list[int]] = {}
    for assignment in assignments:
        grouped.setdefault(assignment["station"], []).append(assignment["point"])

    return {
        station: grouped[station]
        for station in sorted(grouped)
    }


def _to_tsplib_numbers(indices: tuple[int, ...] | list[int]) -> list[int]:
    return [index + 1 for index in indices]
