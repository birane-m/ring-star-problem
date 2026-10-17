"""Consistent, exportable plots drawn from actual saved Ring-Star solutions."""
from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
import os

from ring_star.distances import build_distance_matrix
from ring_star.instance import RingStarInstance, RingStarProblem
from ring_star.solution import RingStarSolution

COLORS = {"greedy": "#2563eb", "local_search": "#d97706", "tabu_search": "#0f766e", "exact_plne": "#7c3aed"}
MARKERS = {"greedy": "o", "local_search": "s", "tabu_search": "^", "exact_plne": "D"}
STYLES = {"greedy": "--", "local_search": "-.", "tabu_search": "-", "exact_plne": ":"}


@contextmanager
def plot_style():
    os.environ.setdefault("MPLCONFIGDIR", ".matplotlib-cache")
    import matplotlib
    # Always produce files; no GUI or interactive backend is required.
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    with plt.rc_context({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.titlesize": 12, "axes.labelsize": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.edgecolor": "#cbd5e1", "text.color": "#172033",
                         "axes.labelcolor": "#475569", "xtick.color": "#64748b",
                         "ytick.color": "#64748b", "pdf.fonttype": 42,
                         "svg.fonttype": "none", "savefig.facecolor": "white"}):
        yield plt


def _save(fig, path: str | Path, formats: tuple[str, ...] | None = None) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    for extension in formats or (path.suffix.lstrip(".") or "png",):
        fig.savefig(path.with_suffix(f".{extension}"), dpi=180, bbox_inches="tight")
    return path


def _bounds(instance: RingStarInstance) -> tuple[float, float, float, float]:
    xs, ys = zip(*instance.points)
    span = max(max(xs) - min(xs), max(ys) - min(ys), 1.0)
    pad = span * 0.05
    return min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad


def _axes(ax, instance: RingStarInstance) -> None:
    xmin, xmax, ymin, ymax = _bounds(instance)
    ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax), xlabel="Coordonnée x", ylabel="Coordonnée y")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, color="#e2e8f0", linewidth=0.5, alpha=0.55)
    ax.set_axisbelow(True)
    ax.tick_params(length=0)


def _draw_solution(ax, instance: RingStarInstance, solution: RingStarSolution, show_labels: bool = False) -> None:
    from matplotlib.collections import LineCollection
    points = instance.points
    attachments = [[points[i], points[s]] for i, s in enumerate(solution.assignments) if i != s]
    ax.add_collection(LineCollection(attachments, colors="#94a3b8", linewidths=0.8,
                                     linestyles="dashed", alpha=0.55, zorder=1))
    ring = [points[i] for i in (*solution.cycle, solution.cycle[0])]
    ax.plot([p[0] for p in ring], [p[1] for p in ring], color="#1e3a5f", lw=2.0, zorder=2)
    non_stations = sorted(set(range(instance.n)) - solution.stations)
    if non_stations:
        ax.scatter([points[i][0] for i in non_stations], [points[i][1] for i in non_stations],
                   s=23, color="#cbd5e1", edgecolors="#64748b", lw=0.5, zorder=3)
    stations = sorted(solution.stations)
    ax.scatter([points[i][0] for i in stations], [points[i][1] for i in stations],
               s=60, color="#0f766e", edgecolors="white", lw=0.9, zorder=4)
    root = points[instance.required_station]
    ax.scatter([root[0]], [root[1]], marker="*", s=220, color="#fbbf24",
               edgecolors="#172033", lw=0.9, zorder=5)
    if show_labels:
        for index, point in enumerate(points, 1):
            ax.annotate(str(index), point, xytext=(5, 5), textcoords="offset points",
                        fontsize=7, color="#475569", zorder=6)
    _axes(ax, instance)


def _legend():
    from matplotlib.lines import Line2D
    return [
        Line2D([], [], marker="o", ls="none", color="#94a3b8", label="Point non-station", markersize=5),
        Line2D([], [], marker="o", ls="none", color="#0f766e", label="Station", markersize=7),
        Line2D([], [], marker="*", ls="none", color="#fbbf24", markeredgecolor="#172033", label="Station imposée", markersize=12),
        Line2D([], [], color="#1e3a5f", lw=2, label="Cycle"),
        Line2D([], [], color="#94a3b8", ls="--", lw=0.8, label="Affectation"),
    ]


def save_point_cloud_png(instance: RingStarInstance, output_path: str | Path,
                         show_labels: bool = False, dpi: int = 180) -> Path:
    with plot_style() as plt:
        fig, ax = plt.subplots(figsize=(9, 6), layout="constrained")
        ax.scatter(*zip(*instance.points), s=27, color="#64748b", zorder=3)
        point = instance.points[instance.required_station]
        ax.scatter(*point, marker="*", s=180, color="#fbbf24", edgecolors="#172033", zorder=4)
        if show_labels:
            for i, point in enumerate(instance.points, 1):
                ax.annotate(str(i), point, xytext=(4, 4), textcoords="offset points", fontsize=7)
        _axes(ax, instance)
        ax.set_title(f"{instance.name.removesuffix('.tsp')} · {instance.n} points", loc="left", pad=16)
        result = _save(fig, output_path)
        plt.close(fig)
        return result


def save_solution_png(
    instance: RingStarInstance, solution: RingStarSolution, output_path: str | Path,
    title: str | None = None, show_labels: bool = False, dpi: int = 180, *,
    problem: RingStarProblem | None = None, status: str | None = None,
    elapsed_seconds: float | None = None, seed: int | None = None,
    formats: tuple[str, ...] | None = None,
) -> Path:
    xs, ys = zip(*instance.points)
    ratio = (max(xs)-min(xs)) / max(max(ys)-min(ys), 1e-12)
    portrait = ratio < .65
    with plot_style() as plt:
        fig, ax = plt.subplots(figsize=(7.0, 7.5) if portrait else (9.5, 6.5))
        _draw_solution(ax, instance, solution, show_labels)
        label = instance.name.removesuffix(".tsp")
        fig.suptitle(f"{title or 'Solution Ring-Star'}  |  {label}", x=0.08, ha="left", y=0.98, fontsize=14, weight="bold")
        parameters = f"n = {instance.n}   ·   p = {len(solution.stations)}"
        if problem is not None:
            parameters += f"   ·   α = {problem.alpha:g}"
        fig.text(.08, .925, parameters, fontsize=10, color="#475569")
        costs = solution.costs(build_distance_matrix(instance.points), problem.alpha) if problem is not None else None
        if portrait:
            if costs:
                fig.text(.63, .825, "COÛT TOTAL\n" + f"{costs.total:,.2f}", fontsize=12, weight="bold", linespacing=1.7)
                fig.text(.63, .71, f"Cycle : {costs.metro:,.2f}\nAffectations : {costs.walking:,.2f}", fontsize=9, color="#475569", linespacing=1.7)
            fig.legend(handles=_legend(), loc="upper left", bbox_to_anchor=(.60, .60), frameon=False, fontsize=8, labelspacing=1.3)
            notes = []
            if status:
                notes.append(f"Statut : {status}")
            if elapsed_seconds is not None:
                notes.append(f"Calcul : {elapsed_seconds:.4f} s")
            if seed is not None:
                notes.append(f"Graine : {seed}")
            fig.text(.63, .27, "\n".join(notes), fontsize=8, color="#64748b", linespacing=1.8)
            fig.subplots_adjust(top=.86, bottom=.12, left=.1, right=.57)
            fig.text(.08, .035, "Distances euclidiennes non arrondies\nUnités des coordonnées", fontsize=8, color="#64748b")
        else:
            if costs:
                fig.text(.08, .88, f"Coût total = {costs.total:,.2f}   ·   cycle = {costs.metro:,.2f}   ·   affectations = {costs.walking:,.2f}", fontsize=9, color="#475569")
            footer = ["Distances euclidiennes non arrondies · unités des coordonnées"]
            if status:
                footer.append(f"statut : {status}")
            if elapsed_seconds is not None:
                footer.append(f"calcul : {elapsed_seconds:.4f} s")
            if seed is not None:
                footer.append(f"graine : {seed}")
            fig.text(.08, .025, "  |  ".join(footer), fontsize=7.5, color="#64748b")
            fig.legend(handles=_legend(), loc="lower center", ncol=5, bbox_to_anchor=(.5, .055), frameon=False, fontsize=8)
            fig.subplots_adjust(top=.82, bottom=.16, left=.08, right=.98)
        result = _save(fig, output_path, formats)
        plt.close(fig)
        return result


def save_solution_comparison(problem: RingStarProblem, before: RingStarSolution,
                              after: RingStarSolution, output_path: str | Path) -> Path:
    distances = build_distance_matrix(problem.instance.points)
    first, last = before.costs(distances, problem.alpha).total, after.costs(distances, problem.alpha).total
    gain = 100 * (first - last) / first if first > 0 else 0.0
    xs, ys = zip(*problem.instance.points)
    portrait = (max(xs)-min(xs)) / max(max(ys)-min(ys), 1e-12) < .65
    with plot_style() as plt:
        fig, axes = plt.subplots(1, 2, figsize=(7.2, 7.8) if portrait else (12, 5.1))
        for ax, solution, title in zip(axes, (before, after), ("Construction initiale", "Meilleure solution")):
            _draw_solution(ax, problem.instance, solution)
            cost = solution.costs(distances, problem.alpha).total
            ax.set_title(f"{title}\nCoût = {cost:,.2f}", loc="left", pad=12, fontsize=10 if portrait else 12)
        fig.suptitle(f"{problem.instance.name.removesuffix('.tsp')} · p={problem.p} · α={problem.alpha:g} · gain={gain:.1f} %", y=0.99, weight="bold")
        fig.legend(handles=_legend(), ncol=3 if portrait else 5, loc="lower center", frameon=False, fontsize=8)
        fig.tight_layout(rect=(0, 0.09 if portrait else 0.07, 1, 0.94))
        result = _save(fig, output_path, ("png", "pdf", "svg"))
        plt.close(fig)
        return result


def save_convergence(history, output_path: str | Path) -> Path:
    with plot_style() as plt:
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), layout="constrained")
        for ax, field, label in zip(axes, ("evaluations", "elapsed_seconds"),
                                    ("Mouvements évalués", "Temps d'amélioration (s)")):
            xs = [step[field] for step in history]
            ax.plot(xs, [s["current_cost"] for s in history], color="#94a3b8", lw=1, alpha=.7, label="Solution courante")
            ax.step(xs, [s["best_cost"] for s in history], where="post", color="#0f766e", lw=2, label="Meilleur coût")
            ax.set(xlabel=label, ylabel="Coût total")
            ax.grid(axis="y", alpha=.2)
        axes[0].legend(frameon=False, fontsize=8)
        fig.suptitle("Progression de la recherche", weight="bold")
        result = _save(fig, output_path, ("png", "pdf", "svg"))
        plt.close(fig)
        return result
