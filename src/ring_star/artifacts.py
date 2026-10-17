"""Self-contained, collision-free experiment folders and verified result loading."""
from __future__ import annotations

import csv
import hashlib
import json
import platform
import re
from math import isfinite
from dataclasses import asdict
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path
from uuid import uuid4

from ring_star.distances import build_distance_matrix
from ring_star.execution import METHOD_LABELS, RunResult
from ring_star.instance import RingStarInstance, RingStarProblem
from ring_star.results import solution_result_data, solution_result_markdown
from ring_star.solution import RingStarSolution
from ring_star.validation import validate_solution

SCHEMA_VERSION = 2


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")


def slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", value).strip("._")[:100] or "experiment"


def unique_directory(parent: Path, label: str) -> Path:
    parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    path = parent / f"{stamp}_{slug(label)}_{uuid4().hex[:6]}"
    path.mkdir()
    return path


def environment_data() -> dict:
    versions = {}
    for package in ("pulp", "matplotlib"):
        try:
            versions[package] = metadata.version(package)
        except metadata.PackageNotFoundError:
            versions[package] = None
    digest = hashlib.sha256()
    for path in sorted(Path(__file__).parent.glob("*.py")):
        digest.update(path.name.encode())
        digest.update(path.read_bytes())
    return {"python": platform.python_version(), "platform": platform.platform(),
            "packages": versions, "source_sha256": digest.hexdigest()}


def problem_data(problem: RingStarProblem) -> dict:
    instance = problem.instance
    return {"name": instance.name, "points": instance.points,
            "required_station": instance.required_station,
            "edge_weight_type": instance.edge_weight_type,
            "distance_metric": "euclidean_unrounded", "p": problem.p, "alpha": problem.alpha}


def run_data(problem: RingStarProblem, result: RunResult) -> dict:
    if result.solution is None:
        data = {"instance": problem.instance.name, "n": problem.instance.n,
                "p": problem.p, "alpha": problem.alpha, "method": result.config.method}
    else:
        data = solution_result_data(problem, result.solution,
                                    build_distance_matrix(problem.instance.points), result.config.method,
                                    plot_path="figures/solution.png")
    data.update({"schema_version": SCHEMA_VERSION, "problem": problem_data(problem),
                 "configuration": asdict(result.config), "status": result.status,
                 "elapsed_seconds": result.elapsed_seconds, "optimal": result.optimal,
                 "lower_bound": result.lower_bound, "relative_gap": result.relative_gap,
                 "details": result.details, "history": result.history, "error": result.error})
    return data


def load_saved_solution(path: str | Path) -> tuple[RingStarProblem, RingStarSolution, dict]:
    """Reload the exact saved cycle and verify feasibility and costs before plotting."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("A schema v2 solution with its input coordinates is required.")
    raw = data["problem"]
    instance = RingStarInstance(raw["name"], raw["points"], raw["required_station"], raw.get("edge_weight_type"))
    problem = RingStarProblem(instance, raw["p"], raw["alpha"])
    if "cycle" not in data:
        raise ValueError("This run has no feasible solution to plot.")
    if (data["instance"], data["n"], data["p"], data["alpha"]) != (instance.name, instance.n, problem.p, problem.alpha):
        raise ValueError("Saved metadata disagrees with the embedded problem.")
    assignments = data["assignments"]
    if [a["point"] for a in assignments] != list(range(1, instance.n + 1)):
        raise ValueError("Saved assignments are missing, duplicated or reordered.")
    solution = RingStarSolution([x - 1 for x in data["stations"]],
                                [x - 1 for x in data["cycle"]],
                                [a["station"] - 1 for a in assignments])
    validate_solution(problem, solution)
    costs = solution.costs(build_distance_matrix(instance.points), problem.alpha)
    for key, value in asdict(costs).items():
        saved = data["costs"][key]
        if type(saved) not in (float, int) or not isfinite(saved) or abs(value - saved) > 1e-7 * max(1.0, abs(value)):
            raise ValueError(f"Saved {key} cost does not match the saved solution.")
    return problem, solution, data


def save_run(
    problem: RingStarProblem, result: RunResult, *, output_root: str | Path = "outputs",
    directory: Path | None = None, make_plots: bool = True, show_labels: bool = False,
    source_path: str | Path | None = None,
) -> Path:
    root = Path(output_root)
    folder = directory or unique_directory(root / "runs", f"{problem.instance.name}_{result.config.method}_p{problem.p}")
    folder.mkdir(parents=True, exist_ok=True)
    config = {"schema_version": SCHEMA_VERSION, "created_at_utc": datetime.now(timezone.utc).isoformat(),
              "problem": problem_data(problem), "algorithm": asdict(result.config),
              "timing_scope": "distances + initialization + optimization; excludes loading and exports",
              "search_budget_scope": "improvement phase only",
              "source_file": str(source_path) if source_path else None}
    if source_path is not None:
        config["source_file_sha256"] = hashlib.sha256(Path(source_path).read_bytes()).hexdigest()
    write_json(folder / "configuration.json", config)
    write_json(folder / "environment.json", environment_data())
    data = run_data(problem, result)
    if not make_plots:
        data["plot"] = None
    write_json(folder / "solution.json", data)
    with (folder / "history.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["iteration", "evaluations", "elapsed_seconds", "current_cost", "best_cost"])
        writer.writeheader()
        writer.writerows(result.history)
    if result.solver_log:
        (folder / "solver.log").write_text(result.solver_log, encoding="utf-8")
    if result.initial_solution is not None:
        initial = solution_result_data(problem, result.initial_solution,
                                       build_distance_matrix(problem.instance.points), "initial_greedy")
        write_json(folder / "initial_solution.json", initial)
    if result.solution is not None:
        summary = solution_result_markdown(problem, result.solution,
                                           build_distance_matrix(problem.instance.points),
                                           result.config.method, plot_path="figures/solution.png" if make_plots else None)
        if make_plots:
            replot_run(folder, show_labels=show_labels)

    else:
        summary = f"# Exécution {result.config.method} - {problem.instance.name}\n\nAucune solution exportable.\n"
    summary += (f"\n## Exécution\n\n- Statut : {result.status}\n- Optimalité prouvée : {result.optimal}\n"
                f"- Temps de calcul : {result.elapsed_seconds:.6f} s\n- Graine : {result.config.seed}\n"
                f"- Détails : {json.dumps(result.details, ensure_ascii=False)}\n"
                f"- Borne inférieure : {result.lower_bound}\n- Écart relatif solveur : {result.relative_gap}\n")
    if result.error:
        summary += f"- Erreur : {result.error}\n"
    summary += "\n[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)\n"
    (folder / "summary.md").write_text(summary, encoding="utf-8")
    if directory is None:
        update_index(root)
    return folder


def update_index(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    lines = ["# Résultats Ring-Star", "", "Ouvrir le résumé d'une exécution ou d'une campagne.", "",
             "Les coûts utilisent les distances euclidiennes non arrondies, dans les unités des coordonnées.", ""]
    for category, label in (("runs", "Résolutions individuelles"), ("benchmarks", "Campagnes")):
        lines.extend([f"## {label}", ""])
        entries = sorted((root / category).glob("*"), reverse=True) if (root / category).exists() else []
        for entry in entries:
            target = entry / ("summary.md" if category == "runs" else "index.md")
            if target.exists():
                lines.append(f"- [{entry.name}]({target.relative_to(root).as_posix()})")
        if not entries:
            lines.append("Aucune exécution pour le moment.")
        lines.append("")
    (root / "index.md").write_text("\n".join(lines), encoding="utf-8")


def replot_run(folder: str | Path, *, show_labels: bool = False) -> Path:
    """Regenerate all plots without calling an optimization method or input file."""
    from ring_star.visualization import save_convergence, save_solution_comparison, save_solution_png
    folder = Path(folder)
    problem, solution, data = load_saved_solution(folder / "solution.json")
    target = folder / "figures/solution.png"
    save_solution_png(problem.instance, solution, target,
                      title=METHOD_LABELS[data["method"]], show_labels=show_labels,
                      problem=problem, status=data["status"], elapsed_seconds=data["elapsed_seconds"],
                      seed=data["configuration"]["seed"], formats=("png", "pdf", "svg"))
    initial_path = folder / "initial_solution.json"
    if initial_path.exists():
        initial_data = json.loads(initial_path.read_text(encoding="utf-8"))
        initial = RingStarSolution([s-1 for s in initial_data["stations"]],
                                   [s-1 for s in initial_data["cycle"]],
                                   [a["station"]-1 for a in initial_data["assignments"]])
        validate_solution(problem, initial)
        initial_cost = initial.costs(build_distance_matrix(problem.instance.points), problem.alpha).total
        if abs(initial_cost - initial_data["costs"]["total"]) > 1e-7 * max(1., abs(initial_cost)):
            raise ValueError("Initial solution cost does not match its saved cycle.")
        save_solution_comparison(problem, initial, solution, folder / "figures/before_after.png")
    if len(data["history"]) > 1:
        save_convergence(data["history"], folder / "figures/convergence.png")
    return target
