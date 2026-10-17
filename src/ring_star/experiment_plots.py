"""Readable per-instance comparisons and compact, dimensionless gain matrices."""
from __future__ import annotations

from collections import defaultdict
import json
from math import ceil
from pathlib import Path

from ring_star.execution import METHODS, METHOD_LABELS
from ring_star.visualization import COLORS, MARKERS, STYLES, _save, plot_style


def _method_series(ax, rows: list[dict], method: str, field: str, spread: str | None = None) -> None:
    selected = sorted([r for r in rows if r["method"] == method and r.get(field) is not None], key=lambda r: r["p"])
    if not selected:
        return
    ax.errorbar([r["p"] for r in selected], [r[field] for r in selected],
                yerr=[r.get(spread) or 0 for r in selected] if spread else None,
                color=COLORS[method], marker=MARKERS[method], linestyle=STYLES[method],
                markersize=5, markerfacecolor="white" if method == "exact_plne" else COLORS[method],
                linewidth=1.6, capsize=3, label=METHOD_LABELS[method], zorder=4 if method == "exact_plne" else 3)
    if method == "exact_plne":
        for row in selected:
            if json.loads(row.get("statuses", "{}" )).get("optimal", 0):
                ax.plot(row["p"], row[field], marker="D", ms=5, color=COLORS[method], ls="none", zorder=5)


def plot_campaign(rows: list[dict], output_dir: Path) -> list[Path]:
    from ring_star.artifacts import slug
    output_dir.mkdir(parents=True, exist_ok=True)
    grouped = defaultdict(list)
    for row in rows:
        grouped[(row["instance"], row["alpha"])].append(row)
    saved = []
    with plot_style() as plt:
        for (instance, alpha), case in sorted(grouped.items()):
            fig, axes = plt.subplots(1, 3, figsize=(13.6, 4.7))
            for method in METHODS:
                _method_series(axes[0], case, method, "mean_cost", "std_cost")
                _method_series(axes[1], case, method, "mean_seconds", "std_seconds")
            axes[0].set(title="Qualité des solutions", ylabel="Coût total moyen")
            axes[1].set(title="Effort de calcul", ylabel="Temps moyen (s, logarithmique)", yscale="log")
            baselines = {r["p"]: r["mean_cost"] for r in case if r["method"] == "greedy" and r["mean_cost"] is not None}
            for method in ("local_search", "tabu_search"):
                gains = []
                for row in case:
                    base = baselines.get(row["p"])
                    if row["method"] == method and row["mean_cost"] is not None and base is not None and base > 0:
                        gains.append({**row, "gain": 100*(base-row["mean_cost"])/base,
                                      "gain_std": None if row["std_cost"] is None else 100*row["std_cost"]/base})
                _method_series(axes[2], gains, method, "gain", "gain_std")
            axes[2].axhline(0, color="#94a3b8", linewidth=.8)
            axes[2].set(title="Gain sur la construction initiale", ylabel="Réduction moyenne du coût (%)")
            ps = sorted({r["p"] for r in case})
            for ax in axes:
                ax.set_xlabel("Nombre de stations p")
                if len(ps) <= 12:
                    ax.set_xticks(ps)
                ax.grid(axis="y", alpha=.2)
            handles, labels = axes[0].get_legend_handles_labels()
            fig.legend(handles, labels, loc="lower center", ncol=4, frameon=False, fontsize=9, bbox_to_anchor=(.5, .055))
            fig.suptitle(f"{instance} · n={case[0]['n']} · α={alpha:g}", x=.055, ha="left", weight="bold", fontsize=15)
            exact_rows = [r for r in case if r["method"] == "exact_plne"]
            if exact_rows and all(r["mean_cost"] is None for r in exact_rows):
                exact_note = "PLNE : aucun résultat réalisable dans le périmètre configuré."
            else:
                exact_note = "PLNE : diamant plein = optimum prouvé ; creux = solution réalisable sans preuve."
            fig.text(.055, .015, "Moyennes ± écarts-types observés. " + exact_note, color="#64748b", fontsize=8)
            fig.tight_layout(rect=(0, .13, 1, .92))
            path = output_dir / "by_instance" / f"{slug(instance)}_alpha_{alpha:g}.png"
            saved.append(_save(fig, path, ("png", "pdf", "svg")))
            plt.close(fig)
        for alpha in sorted({r["alpha"] for r in rows}):
            selected = [r for r in rows if r["alpha"] == alpha]
            instances = sorted({r["instance"] for r in selected}, key=lambda x: next(r["n"] for r in selected if r["instance"] == x))
            ps = sorted({r["p"] for r in selected})
            lookup = {(r["instance"], r["p"], r["method"]): r for r in selected}
            matrices = []
            values = []
            for method in ("local_search", "tabu_search"):
                matrix = []
                for instance in instances:
                    line = []
                    for p in ps:
                        base = lookup.get((instance, p, "greedy"), {}).get("mean_cost")
                        score = lookup.get((instance, p, method), {}).get("mean_cost")
                        value = 100*(base-score)/base if base is not None and base > 0 and score is not None else float("nan")
                        line.append(value)
                        if value == value:
                            values.append(value)
                    matrix.append(line)
                matrices.append(matrix)
            if not values:
                continue
            fig, axes = plt.subplots(1, 2, figsize=(max(8, len(ps)*.65+5), max(3.5, len(instances)*.48+1.8)), layout="constrained")
            bound = max(1., max(abs(v) for v in values))
            for ax, method, matrix in zip(axes, ("local_search", "tabu_search"), matrices):
                negative = any(v < -1e-8 for v in values)
                cmap = plt.get_cmap("RdBu" if negative else "Blues").copy()
                cmap.set_bad("#f1f5f9")
                im = ax.imshow(matrix, vmin=-bound if negative else 0, vmax=bound, cmap=cmap, aspect="auto")
                ax.set_xticks(range(len(ps)), ps)
                ax.set_yticks(range(len(instances)), instances)
                ax.set(xlabel="Nombre de stations p", title=METHOD_LABELS[method])
                ax.tick_params(length=0)
                for i, line in enumerate(matrix):
                    for j, val in enumerate(line):
                        ax.text(j, i, "—" if val != val else f"{val:.1f}%", ha="center", va="center",
                                color="white" if val == val and abs(val) > bound*.60 else "#172033", fontsize=9)
            fig.colorbar(im, ax=list(axes), label="Réduction moyenne du coût vs construction initiale (%)", shrink=.8)
            fig.suptitle(f"Gains moyens par instance · α={alpha:g}\nCases grises : combinaison absente", weight="bold", fontsize=12)
            path = output_dir / f"gains_alpha_{alpha:g}.png"
            saved.append(_save(fig, path, ("png", "pdf", "svg")))
            plt.close(fig)
    return saved


def plot_legacy_comparison(rows: list[dict[str, str]], output_dir: Path) -> list[Path]:
    """Keep old compare commands usable, without a fixed eight-panel limit."""
    converted = []
    for row in rows:
        for method in METHODS:
            def optional(key):
                value = row.get(key, "")
                return float(value) if value else None
            converted.append({"instance": row["instance"], "n": int(row["n"]),
                              "p": int(row["p"]), "alpha": float(row["alpha"]), "method": method,
                              "mean_cost": optional(f"{method}_cost"), "std_cost": None,
                              "mean_seconds": optional(f"{method}_time"), "std_seconds": None,
                              "statuses": json.dumps({row.get("exact_status", ""): 1}) if method == "exact_plne" else "{}"})
    return plot_campaign(converted, output_dir)
