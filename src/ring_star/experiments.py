"""Configuration-driven campaigns, complete run archives and seed summaries."""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from dataclasses import asdict, replace
from datetime import datetime, timezone
from math import isclose
from pathlib import Path
from statistics import mean, median, stdev

from ring_star.artifacts import environment_data, save_run, slug, unique_directory, update_index, write_json
from ring_star.benchmark import BenchmarkRecord, record_from_run, save_benchmark_csv, SUCCESS
from ring_star.execution import METHODS, METHOD_LABELS, RunConfig, execute
from ring_star.instance import RingStarProblem
from ring_star.io import load_tsplib_instance

ALLOWED = {"name", "instances", "p_values", "p_values_by_instance", "alphas", "seeds", "methods",
           "local_iterations", "tabu_iterations", "tabu_tenure", "candidates_per_iteration",
           "search_time_limit", "exact_time_limit", "exact_max_n", "exact_max_p"}


def load_campaign_config(path: str | Path) -> dict:
    config = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(config, dict) or set(config) - ALLOWED:
        raise ValueError(f"Unknown campaign keys: {set(config) - ALLOWED if isinstance(config, dict) else 'not an object'}.")
    if not config.get("instances") or not isinstance(config["instances"], list):
        raise ValueError("instances must be a nonempty list of paths relative to the configuration file.")
    for key in ("instances", "seeds", "alphas", "methods", "p_values"):
        if key in config and (not isinstance(config[key], list) or not config[key] or len(set(config[key])) != len(config[key])):
            raise ValueError(f"{key} must be a nonempty list without duplicates.")
    methods = config.get("methods", list(METHODS))
    if set(methods) - set(METHODS):
        raise ValueError("Unsupported campaign method.")
    for key in ("exact_max_n", "exact_max_p"):
        value = config.get(key)
        if value is not None and (type(value) is not int or value < 3):
            raise ValueError(f"{key} must be an integer >= 3, or null.")
    for seed in config.get("seeds", [0, 1, 2]):
        for method in methods:
            RunConfig(method, seed, config.get("local_iterations", 100) if method == "local_search" else config.get("tabu_iterations", 100),
                      config.get("tabu_tenure", 20), config.get("candidates_per_iteration", 15),
                      config.get("exact_time_limit", 10), config.get("search_time_limit"))
    return config


def summarize_records(records: list[BenchmarkRecord]) -> list[dict]:
    groups = defaultdict(list)
    optima = {}
    for row in records:
        groups[(row.instance, row.n, row.p, row.alpha, row.method)].append(row)
        if row.optimal and row.total_cost is not None:
            key = (row.instance, row.p, row.alpha)
            if key in optima and not isclose(optima[key], row.total_cost, rel_tol=1e-7, abs_tol=1e-7):
                raise ValueError("Conflicting proven optima for the same case.")
            optima[key] = row.total_cost
    summaries = []
    for (instance, n, p, alpha, method), runs in sorted(groups.items(), key=lambda x: (x[0][1], x[0][0], x[0][3], x[0][2], x[0][4])):
        valid = [r for r in runs if r.total_cost is not None and r.status in SUCCESS]
        costs = [r.total_cost for r in valid]
        times = [r.elapsed_seconds for r in runs if r.status != "skipped"]
        best = min(valid, key=lambda r: (r.total_cost, r.seed)) if valid else None
        optimum = optima.get((instance, p, alpha))
        if optimum is not None and costs and min(costs) < optimum - 1e-6 * max(1., abs(optimum)):
            raise ValueError("Heuristic result is better than a claimed proven optimum; inspect the solver/model.")
        summaries.append({
            "instance": instance.removesuffix(".tsp"), "n": n, "p": p, "alpha": alpha,
            "method": method, "runs": len(runs), "successful_runs": len(valid),
            "statuses": json.dumps(dict(Counter(r.status for r in runs)), sort_keys=True),
            "mean_cost": mean(costs) if costs else None, "median_cost": median(costs) if costs else None,
            "best_cost": min(costs) if costs else None, "worst_cost": max(costs) if costs else None,
            "std_cost": stdev(costs) if len(costs) > 1 else None,
            "mean_seconds": mean(times) if times else None, "std_seconds": stdev(times) if len(times) > 1 else None,
            "mean_evaluations": mean(r.run_result.details.get("evaluated_moves", 0) if r.run_result else 0 for r in valid) if valid else None,
            "proven_optimum": optimum,
            "mean_gap_to_optimum_percent": 100 * (mean(costs) - optimum) / optimum if costs and optimum is not None and optimum > 0 else None,
            "best_seed": best.seed if best else None, "representative_solution": best.solution_file if best else "",
        })
    return summaries


def save_summary_csv(rows: list[dict], path: Path) -> None:
    if not rows:
        raise ValueError("No campaign cases were generated.")
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def run_campaign(config_path: str | Path, output_root: str | Path = "outputs", *, make_plots: bool = True) -> Path:
    """Resolve inputs relative to the config; save every run and plot representatives.

    Greedy and exact are deterministic baselines and run once per case. Stochastic
    methods run once per configured seed. Figure costs use seed means ± sample
    standard deviations; a representative is explicitly the best saved seed.
    """
    from ring_star.experiment_plots import plot_campaign
    config_path = Path(config_path).resolve()
    config = load_campaign_config(config_path)
    # Validate every case and budget before creating an output folder or running a solver.
    cases = []
    for raw_path in config["instances"]:
        source = (config_path.parent / raw_path).resolve()
        instance = load_tsplib_instance(source)
        by_instance = config.get("p_values_by_instance", {})
        ps = by_instance.get(source.stem, config.get("p_values", [3, max(3, round(instance.n*.15)), max(3, round(instance.n*.3))]))
        if not isinstance(ps, list) or not ps or len(set(ps)) != len(ps):
            raise ValueError("p values must be a nonempty list of unique integers.")
        for alpha in config.get("alphas", [1.0]):
            for p in ps:
                cases.append((source, RingStarProblem(instance, p, alpha)))
    if len({(str(path), problem.p, problem.alpha) for path, problem in cases}) != len(cases):
        raise ValueError("Duplicate campaign cases.")
    names = defaultdict(set)
    for path, problem in cases:
        names[problem.instance.name].add(path)
    if any(len(paths) > 1 for paths in names.values()):
        raise ValueError("Input instance NAMEs must be unique within a campaign.")
    root = Path(output_root)
    folder = unique_directory(root / "benchmarks", config.get("name", "campaign"))
    write_json(folder / "configuration.json", config)
    write_json(folder / "environment.json", environment_data())
    write_json(folder / "inputs.json", [{"source": str(source), "problem": {"name": p.instance.name, "n": p.instance.n, "p": p.p, "alpha": p.alpha}}
                                         for source, p in cases])
    records = []
    saved_runs = []
    methods = config.get("methods", list(METHODS))
    seeds = config.get("seeds", [0, 1, 2])
    try:
        for source, problem in cases:
            for method in methods:
                if method == "exact_plne" and (
                    (config.get("exact_max_n") is not None and problem.instance.n > config["exact_max_n"]) or
                    (config.get("exact_max_p") is not None and problem.p > config["exact_max_p"])
                ):
                    records.append(BenchmarkRecord(problem.instance.name, problem.instance.n, problem.p, problem.alpha,
                                                   method, "skipped", None, None, None, 0., (), "Configured exact size limit."))
                    continue
                for seed in seeds if method in {"local_search", "tabu_search"} else seeds[:1]:
                    run_config = RunConfig(
                        method=method, seed=seed,
                        iterations=config.get("local_iterations", 100) if method == "local_search" else config.get("tabu_iterations", 100) if method == "tabu_search" else None,
                        tabu_tenure=config.get("tabu_tenure", 20), candidates_per_iteration=config.get("candidates_per_iteration", 15),
                        time_limit=config.get("exact_time_limit", 10) if method == "exact_plne" else None,
                        search_time_limit=config.get("search_time_limit") if method in {"local_search", "tabu_search"} else None,
                    )
                    print(f"{problem.instance.name} p={problem.p} α={problem.alpha:g} {method} seed={seed}", flush=True)
                    result = execute(problem, run_config)
                    name = f"{slug(problem.instance.name)}_p{problem.p}_a{problem.alpha:g}_{method}_seed{seed}"
                    run_folder = folder / "runs" / name
                    save_run(problem, result, directory=run_folder, make_plots=False, source_path=source)
                    relative = (run_folder / "solution.json").relative_to(folder).as_posix()
                    records.append(record_from_run(problem, result, relative))
                    saved_runs.append((problem, result, run_folder, source))
                    save_benchmark_csv(records, folder / "runs.csv")
        rows = summarize_records(records)
        save_summary_csv(rows, folder / "summary.csv")
        if make_plots:
            representatives = {row["representative_solution"] for row in rows if row["representative_solution"]}
            for problem, result, run_folder, source in saved_runs:
                if (run_folder / "solution.json").relative_to(folder).as_posix() in representatives:
                    save_run(problem, result, directory=run_folder, make_plots=True, source_path=source)
            plot_campaign(rows, folder / "figures")
        lines = [f"# Campagne {config.get('name', 'Ring-Star')}", "",
                 f"- Créée le : {datetime.now(timezone.utc).isoformat()}",
                 f"- Cas : {len(cases)} ; résultats : {len(records)}", "",
                 "[Configuration](configuration.json) · [Résultats détaillés](runs.csv) · [Synthèse](summary.csv)", "",
                 "Les méthodes aléatoires sont répétées sur les graines configurées. Les méthodes déterministes ne sont exécutées qu'une fois.", "",
                 "Les graphiques comparent les moyennes et écarts-types observés. Les solutions illustrées sont les meilleures graines, signalées comme telles.", "",
                 "Les temps excluent les lectures et exports et incluent les tentatives sans solution. Les coûts moyens concernent les exécutions réussies, dont le nombre est indiqué. Le budget de recherche porte sur la phase d'amélioration et peut être dépassé du temps d'une évaluation en cours.", "",
                 "Les coûts portent sur les distances euclidiennes non arrondies. Ne pas comparer les coûts bruts entre instances dont les unités diffèrent.", "",
                 "## Résultats par cas", "", "| Instance | p | α | Méthode | Statuts | Succès | Coût moyen | Écart-type | Temps moyen (s) | Solution représentative |",
                 "|---|---:|---:|---|---|---:|---:|---:|---:|---|"]
        def number(value):
            return "n.d." if value is None else f"{value:.4f}"
        for row in rows:
            target = row["representative_solution"].replace("solution.json", "summary.md")
            link = f"[Meilleure graine {row['best_seed']}]({target})" if target else row["statuses"]
            lines.append(f"| {row['instance']} | {row['p']} | {row['alpha']:g} | {METHOD_LABELS[row['method']]} | {row['statuses']} | {row['successful_runs']}/{row['runs']} | {number(row['mean_cost'])} | {number(row['std_cost'])} | {number(row['mean_seconds'])} | {link} |")
        lines.extend(["", "## Figures", ""])
        for path in sorted((folder / "figures").rglob("*.png")):
            relative = path.relative_to(folder).as_posix()
            lines.append(f"- [{relative}]({relative})")
        (folder / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        write_json(folder / "completion.json", {"status": "completed", "runs": len(records), "statuses": dict(Counter(r.status for r in records))})
    except BaseException as error:
        save_benchmark_csv(records, folder / "runs.csv")
        write_json(folder / "completion.json", {"status": "interrupted", "error": str(error), "saved_runs": len(records)})
        (folder / "index.md").write_text("# Campagne interrompue\n\nConsulter completion.json et runs.csv.\n", encoding="utf-8")
        raise
    finally:
        update_index(root)
    return folder


def replot_campaign(folder: str | Path) -> list[Path]:
    """Redraw a completed campaign from saved solutions and summaries, without solving."""
    from ring_star.artifacts import load_saved_solution, replot_run
    from ring_star.experiment_plots import plot_campaign
    folder = Path(folder).resolve()
    completion = json.loads((folder / "completion.json").read_text(encoding="utf-8"))
    if completion["status"] != "completed":
        raise ValueError("Only completed campaigns can be replotted.")
    with (folder / "summary.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    integer_keys = {"n", "p", "runs", "successful_runs", "best_seed"}
    numeric_keys = integer_keys | {"alpha", "mean_cost", "median_cost", "best_cost", "worst_cost", "std_cost",
                                  "mean_seconds", "std_seconds", "mean_evaluations", "proven_optimum", "mean_gap_to_optimum_percent"}
    saved = []
    for row in rows:
        for key in numeric_keys:
            row[key] = None if row[key] == "" else int(row[key]) if key in integer_keys else float(row[key])
        relative = row["representative_solution"]
        if not relative:
            continue
        source = (folder / relative).resolve()
        if not source.is_relative_to(folder):
            raise ValueError("Saved solution path is outside this campaign.")
        problem, solution, data = load_saved_solution(source)
        if (problem.p, problem.alpha, data["method"], problem.instance.name.removesuffix(".tsp")) != (row["p"], row["alpha"], row["method"], row["instance"]):
            raise ValueError("Summary case differs from the saved representative.")
        if abs(data["costs"]["total"] - row["best_cost"]) > 1e-7 * max(1.,abs(row["best_cost"])):
            raise ValueError("Summary best cost differs from the saved representative.")
        saved.append(replot_run(source.parent))
    saved.extend(plot_campaign(rows, folder / "figures"))
    return saved
