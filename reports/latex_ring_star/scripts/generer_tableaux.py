"""Rebuild report tables from archived data, without running an optimizer."""
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[1]
CAMP = ROOT / "resultats/campagne"


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def number(value, digits=2):
    if value in (None, ""):
        return r"\textemdash"
    return f"{float(value):,.{digits}f}".replace(",", r"\,").replace(".", "{,}")


def table(name, spec, header, rows):
    text = r"\begin{tabular}{" + spec + "}\n\\toprule\n"
    text += " & ".join(header) + r" \\" + "\n\\midrule\n"
    for row in rows:
        text += " & ".join(str(x) for x in row) + r" \\" + "\n"
    text += "\\bottomrule\n\\end{tabular}\n"
    (ROOT / "tableaux" / (name + ".tex")).write_text(text, encoding="utf-8")


def main():
    rows = read_csv(CAMP / "summary.csv")
    lookup = {(x["instance"], int(x["p"]), x["method"]): x for x in rows}
    assert len(lookup) == 96
    config = json.loads((CAMP / "configuration.json").read_text())
    assert config["alphas"] == [1.0] and config["seeds"] == [0, 1, 2]
    assert sum(int(x["runs"]) for x in rows) == 192
    original = read_csv(CAMP / "runs.csv")
    # Preserve the source export. Make a separate corrected copy of the known
    # terminal SKIPPED case, backed by configuration, summary and completion.
    records = list(original)
    missing = []
    for row in rows:
        key = (row["instance"], int(row["p"]), row["method"])
        matching = [r for r in original if
                    (r["instance"].removesuffix(".tsp"), int(r["p"]), r["method"]) == key]
        if len(matching) != int(row["runs"]):
            assert key == ("rd100", 10, "exact_plne")
            assert json.loads(row["statuses"]) == {"skipped": 1}
            sample = next(r for r in original if r["instance"] == "rd100" and r["method"] == "exact_plne")
            new = dict(sample, p="10")
            assert not new["total_cost"] and not new["solution_file"]
            records.append(new)
            missing.append(list(key))
    assert len(records) == 192
    with (ROOT / "resultats/runs_reconcilies.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(original[0])); w.writeheader(); w.writerows(records)
    assert Counter(r["status"] for r in records) == {"ok": 168, "optimal": 3, "feasible_time_limited": 1, "skipped": 20}

    checked = 0
    for source in sorted((CAMP / "runs").glob("*/solution.json")):
        data = json.loads(source.read_text())
        pts = data["problem"]["points"]
        cycle = [i - 1 for i in data["cycle"]]
        stations = {i - 1 for i in data["stations"]}
        assert len(stations) == data["p"] and set(cycle) == stations
        assert data["problem"]["required_station"] in stations
        dist = lambda i, j: math.dist(pts[i], pts[j])
        ring = sum(dist(cycle[i], cycle[(i+1) % len(cycle)]) for i in range(len(cycle)))
        walk = 0.
        for a in data["assignments"]:
            i, s = a["point"]-1, a["station"]-1
            assert s in stations
            assert i not in stations or s == i
            assert abs(dist(i, s) - min(dist(i, t) for t in stations)) < 1e-7
            walk += dist(i, s)
        for key, expected in [("metro", ring), ("walking", walk), ("total", data["alpha"]*ring+walk)]:
            assert math.isclose(data["costs"][key], expected, rel_tol=1e-10, abs_tol=1e-7)
        checked += 1
    assert checked == 172
    for row in rows:
        costs = [float(x["total_cost"]) for x in records if x["total_cost"] and
                 x["instance"].removesuffix(".tsp") == row["instance"] and
                 int(x["p"]) == int(row["p"]) and x["method"] == row["method"]]
        assert len(costs) == int(row["successful_runs"])
        if costs:
            assert math.isclose(mean(costs), float(row["mean_cost"]), rel_tol=1e-9)

    names = [Path(x).stem for x in config["instances"]]
    metrics = {"att48":"ATT", "ulysses16":"GEO", "ulysses22":"GEO"}
    table("instances", "lrrl", ["Instance", "$n$", "$p$ étudiés", "Type source"],
          [(n, lookup[(n,3,"greedy")]["n"], "3, 5, 10", r"\code{"+metrics.get(n,"EUC_2D")+"}") for n in names])
    local_gains, tabu_gains = [], []
    complete = []
    wins = ties = 0
    for name in names:
        for p in (3,5,10):
            g,l,t = [lookup[(name,p,m)] for m in ("greedy","local_search","tabu_search")]
            cg,cl,ct = [float(x["mean_cost"]) for x in (g,l,t)]
            gl,gt = [100*(cg-c)/cg for c in (cl,ct)]
            local_gains.append(gl);tabu_gains.append(gt)
            wins += cl > ct + 1e-8;ties += abs(cl-ct) < 1e-8
            complete.append((name,p,number(cg),number(cl)+" $\\pm$ "+number(l["std_cost"]),number(ct)+" $\\pm$ "+number(t["std_cost"])))
    table("resultats_complets", "lrrrr", ["Instance", "$p$", "Construction", "Locale : moyenne $\\pm s$", "Tabou : moyenne $\\pm s$"], complete)
    table("gains_synthese", "lrrr", ["Méthode", "Minimum", "Médiane", "Maximum"],
          [(label,number(min(v))+r"\,\%",number(median(v))+r"\,\%",number(max(v))+r"\,\%")
           for label,v in [("Recherche locale",local_gains),("Recherche tabou",tabu_gains)]])
    table("ulysses16_p5", "lrrrr", ["Méthode", "Coût moyen", "$s$", "Écart à l'optimum", "Temps (ms)"],
          [(label,number(x["mean_cost"],4),number(x["std_cost"],4),number(x["mean_gap_to_optimum_percent"],3)+r"\,\%",number(1000*float(x["mean_seconds"]),2))
           for m,label in [("greedy","Construction"),("local_search","Locale"),("tabu_search","Tabou"),("exact_plne","PLNE / CBC")]
           for x in [lookup[("ulysses16",5,m)]]])
    exact = []
    for source in sorted((CAMP / "runs").glob("*exact*/solution.json")):
        d=json.loads(source.read_text())
        exact.append((d["instance"].removesuffix(".tsp"),d["p"],number(d["costs"]["total"],4),number(d["lower_bound"],4),number(100*d["relative_gap"],2)+r"\,\%",number(d["elapsed_seconds"],3),"Prouvé" if d["optimal"] else "Non prouvé"))
    table("resultats_exacts", "lrrrrrl", ["Instance","$p$","Coût","Borne inf.","Écart$^*$","Temps (s)","Optimum"],exact)
    table("temps_p5", "lrrr", ["Instance", "Construction (ms)", "Locale (ms)", "Tabou (ms)"],
          [(n,*[number(1000*float(lookup[(n,5,m)]["mean_seconds"]),2) for m in ("greedy","local_search","tabu_search")]) for n in names])
    run=json.loads((ROOT/'resultats/exemple_att48/solution.json').read_text())
    init=json.loads((ROOT/'resultats/exemple_att48/initial_solution.json').read_text())
    table("decomposition_att48","lrrr",["Composante","Construction","Meilleure tabou","Baisse relative"],
          [(label,number(init["costs"][key]),number(run["costs"][key]),number(100*(init["costs"][key]-run["costs"][key])/init["costs"][key])+r"\,\%")
           for key,label in [("metro","Longueur de l'anneau"),("walking","Somme des accès"),("total","Coût total ($\\alpha=1$)")]])
    proof=[]
    for n,p in [("ulysses16",3),("ulysses16",5),("ulysses22",3)]:
        proof.append((n,p,*[number(lookup[(n,p,m)]["mean_gap_to_optimum_percent"],3)+r"\,\%" for m in ("greedy","local_search","tabu_search")]))
    table("ecarts_optimum","lrrrr",["Instance","$p$","Construction","Locale","Tabou"],proof)
    provenance={"report_date":"2026-10-17", "code_commit_published":"8761003",
                "experiment_source_sha256":json.loads((CAMP/'environment.json').read_text())["source_sha256"],
                "campaign_directory":"20261017T184415046891Z_demo_multi_graines_7cc051",
                "source_csv_records":len(original),"reconciled_csv_records":len(records),
                "reconciled_skipped_cases":missing,"campaign_solutions_recomputed":checked,
                "tabu_lower_mean_cost_cases":wins,"tied_mean_cost_cases":ties,
                "reported_gains":{"local_median":median(local_gains),"tabu_median":median(tabu_gains)},
                "individual_run_cost":run['costs']['total'],
                "fix_scope":"Final CSV flush plus assertion in an existing regression test; no optimizer change.",
                "files_sha256":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in sorted((ROOT/'resultats').rglob('*'))
                                if p.is_file() and p.name != 'provenance_rapport.json'}}
    (ROOT/'resultats/provenance_rapport.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
    print(f"Tables generated; {checked} campaign solutions checked; {len(records)} cases reconciled.")


if __name__ == "__main__":
    main()
