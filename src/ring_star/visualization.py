"""Visualizations for Ring-Star instances."""

from __future__ import annotations

import os
from pathlib import Path

from ring_star.instance import RingStarInstance
from ring_star.solution import RingStarSolution


def save_point_cloud_png(
    instance: RingStarInstance,
    output_path: str | Path,
    show_labels: bool = False,
    dpi: int = 180,
) -> Path:
    """Write a point-cloud PNG with axes and grid using matplotlib."""

    os.environ.setdefault("MPLCONFIGDIR", ".matplotlib-cache")

    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as error:
        raise RuntimeError(
            "matplotlib is required to generate PNG visualizations."
        ) from error

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    xs = [point[0] for point in instance.points]
    ys = [point[1] for point in instance.points]

    fig, ax = plt.subplots(figsize=(9, 7))
    ax.scatter(xs, ys, s=28, color="#2563eb", edgecolors="#1e3a8a", linewidths=0.7)

    if show_labels:
        for index, (x, y) in enumerate(instance.points, start=1):
            ax.annotate(
                str(index),
                (x, y),
                textcoords="offset points",
                xytext=(4, 4),
                fontsize=7,
                color="#334155",
            )

    ax.set_title(f"Nuage de points TSPLIB - {instance.name}")
    ax.set_xlabel("Coordonnée x de l'instance")
    ax.set_ylabel("Coordonnée y de l'instance")
    ax.axis("equal")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.4)
    fig.tight_layout()
    fig.savefig(output_path, dpi=dpi)
    plt.close(fig)
    return output_path


def save_solution_png(
    instance: RingStarInstance,
    solution: RingStarSolution,
    output_path: str | Path,
    title: str | None = None,
    show_labels: bool = False,
    dpi: int = 180,
) -> Path:
    """Write a PNG visualization of a Ring-Star solution."""

    os.environ.setdefault("MPLCONFIGDIR", ".matplotlib-cache")

    try:
        import matplotlib.pyplot as plt
        from matplotlib.lines import Line2D
    except ModuleNotFoundError as error:
        raise RuntimeError(
            "matplotlib is required to generate PNG visualizations."
        ) from error

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    points = instance.points
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    station_indices = sorted(solution.stations)
    station_xs = [points[index][0] for index in station_indices]
    station_ys = [points[index][1] for index in station_indices]

    fig, ax = plt.subplots(figsize=(10, 7.5))

    for point, station in enumerate(solution.assignments):
        if point == station:
            continue
        point_x, point_y = points[point]
        station_x, station_y = points[station]
        ax.plot(
            [point_x, station_x],
            [point_y, station_y],
            color="#94a3b8",
            linestyle="--",
            linewidth=0.7,
            alpha=0.55,
            zorder=1,
        )

    cycle = solution.cycle
    for station_a, station_b in zip(cycle, cycle[1:] + cycle[:1]):
        ax.plot(
            [points[station_a][0], points[station_b][0]],
            [points[station_a][1], points[station_b][1]],
            color="#111827",
            linewidth=2.0,
            alpha=0.9,
            zorder=2,
        )

    ax.scatter(
        xs,
        ys,
        s=24,
        color="#2563eb",
        edgecolors="#1e3a8a",
        linewidths=0.6,
        zorder=3,
    )
    ax.scatter(
        station_xs,
        station_ys,
        s=70,
        color="#dc2626",
        edgecolors="#7f1d1d",
        linewidths=0.9,
        zorder=4,
    )

    if show_labels:
        for index, (x, y) in enumerate(points, start=1):
            ax.annotate(
                str(index),
                (x, y),
                textcoords="offset points",
                xytext=(4, 4),
                fontsize=7,
                color="#334155",
                zorder=5,
            )

    ax.set_title(title or f"Solution Ring-Star - {instance.name}")
    ax.set_xlabel("Coordonnée x de l'instance")
    ax.set_ylabel("Coordonnée y de l'instance")
    ax.axis("equal")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.35)
    ax.legend(
        handles=[
            Line2D([0], [0], marker="o", color="none", markerfacecolor="#2563eb", markeredgecolor="#1e3a8a", label="Points"),
            Line2D([0], [0], marker="o", color="none", markerfacecolor="#dc2626", markeredgecolor="#7f1d1d", label="Stations"),
            Line2D([0], [0], color="#111827", linewidth=2.0, label="Cycle métro"),
            Line2D([0], [0], color="#94a3b8", linestyle="--", linewidth=1.0, label="Affectations"),
        ],
        loc="best",
    )
    fig.tight_layout()
    fig.savefig(output_path, dpi=dpi)
    plt.close(fig)
    return output_path
