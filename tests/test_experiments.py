import csv
from dataclasses import replace
import json
import tempfile
import unittest
from pathlib import Path

from ring_star.benchmark import BenchmarkRecord,build_comparison_csv,run_benchmark,save_benchmark_csv,save_solution_plots_from_benchmark_csv
from ring_star.experiments import run_campaign,summarize_records,load_campaign_config,replot_campaign
from ring_star.artifacts import load_saved_solution

def read_rows(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


TSP="""NAME: tiny
TYPE: TSP
DIMENSION: 4
EDGE_WEIGHT_TYPE: EUC_2D
NODE_COORD_SECTION
1 0 0
2 3 0
3 3 4
4 0 4
EOF
"""


class ExperimentTests(unittest.TestCase):
    def test_alpha_cases_are_not_merged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            records=[BenchmarkRecord("tiny",4,3,alpha,"greedy","ok",cost,cost,0,.01,(1,2,3)) for alpha,cost in ((0.,1.),(2.,9.))]
            save_benchmark_csv(records,root/"raw.csv")
            build_comparison_csv(root/"raw.csv",root/"missing.csv",None,root/"comparison.csv")
            rows=read_rows(root/"comparison.csv")
            self.assertEqual(len(rows),2)
            self.assertEqual({(float(r["alpha"]),float(r["greedy_cost"])) for r in rows},{(0.,1.),(2.,9.)})

    def test_seed_summary_uses_mean_and_sample_standard_deviation(self):
        records=[BenchmarkRecord("tiny",4,3,1.,"tabu_search","ok",value,value,0,.1,(1,2,3),seed=seed) for seed,value in enumerate((10.,12.,14.))]
        row,=summarize_records(records)
        self.assertEqual(row["runs"],3)
        self.assertEqual(row["mean_cost"],12.)
        self.assertEqual(row["std_cost"],2.)
        self.assertEqual(row["best_cost"],10.)
        self.assertIsNone(row["proven_optimum"])
        self.assertIsNone(row["mean_gap_to_optimum_percent"])

    def test_gap_is_only_computed_against_a_proven_optimum(self):
        heuristic=BenchmarkRecord("tiny",4,3,1.,"greedy","ok",12.,12.,0,.1,(1,2,3))
        feasible=replace(heuristic,method="exact_plne",status="feasible_time_limited",total_cost=10.)
        self.assertTrue(all(r["proven_optimum"] is None for r in summarize_records([heuristic,feasible])))
        exact=replace(feasible,optimal=True,status="optimal")
        rows=summarize_records([heuristic,exact])
        self.assertAlmostEqual(next(r for r in rows if r["method"]=="greedy")["mean_gap_to_optimum_percent"],20.)

    def test_conflicting_proven_optimum_is_reported(self):
        exact=BenchmarkRecord("tiny",4,3,1.,"exact_plne","optimal",10.,10.,0,.1,(1,2,3),optimal=True)
        bad=replace(exact,method="greedy",total_cost=8.,optimal=False)
        with self.assertRaises(ValueError):summarize_records([exact,bad])

    def test_generator_p_values_apply_to_all_instances(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"a.tsp").write_text(TSP)
            (root/"b.tsp").write_text(TSP.replace("tiny","second"))
            records=run_benchmark([root/"a.tsp",root/"b.tsp"],methods=("greedy",),p_values=(p for p in (3,4)))
            self.assertEqual(len(records),4)

    def test_old_csv_cannot_silently_reconstruct_a_different_solution(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"tiny.tsp").write_text(TSP)
            record=BenchmarkRecord("tiny",4,3,1.,"greedy","ok",10.,6.,4.,.1,(1,2,3))
            save_benchmark_csv([record],root/"old.csv")
            with self.assertRaisesRegex(ValueError,"saved cycle"):
                save_solution_plots_from_benchmark_csv(root/"old.csv",root,root/"plots")

    def test_campaign_outputs_match_all_saved_solutions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"tiny.tsp").write_text(TSP)
            config={"name":"test","instances":["tiny.tsp"],"p_values":[3],"alphas":[0.,2.],"seeds":[0,1],
                    "methods":["greedy","local_search","tabu_search"],"local_iterations":3,"tabu_iterations":3,"candidates_per_iteration":2}
            path=root/"config.json";path.write_text(json.dumps(config))
            folder=run_campaign(path,root/"outputs",make_plots=False)
            rows=read_rows(folder/"runs.csv")
            self.assertEqual(len(rows),10)
            for row in rows:
                problem,solution,data=load_saved_solution(folder/row["solution_file"])
                self.assertAlmostEqual(float(row["total_cost"]),data["costs"]["total"],places=7)
                self.assertEqual(tuple(int(x) for x in row["cycle"].split()),tuple(s+1 for s in solution.cycle))
            self.assertTrue((folder/"index.md").exists())
            self.assertEqual(json.loads((folder/"completion.json").read_text())["status"],"completed")
            self.assertEqual(len(read_rows(folder/"summary.csv")),6)

    def test_exact_skips_are_explicit_and_not_plotted_as_zero_cost(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/"tiny.tsp").write_text(TSP)
            config={"instances":["tiny.tsp"],"p_values":[3],"methods":["exact_plne"],"exact_max_n":3}
            path=root/"config.json";path.write_text(json.dumps(config))
            folder=run_campaign(path,root/"outputs",make_plots=False)
            row,=read_rows(folder/"summary.csv")
            self.assertEqual(row["mean_cost"],"")
            self.assertEqual(row["successful_runs"],"0")
            self.assertIn("skipped",row["statuses"])

    def test_unknown_config_and_invalid_p_fail_before_running(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/"tiny.tsp").write_text(TSP)
            path=root/"config.json";path.write_text(json.dumps({"instances":["tiny.tsp"],"p_values":[5]}))
            with self.assertRaises(ValueError):run_campaign(path,root/"outputs",make_plots=False)
            self.assertFalse((root/"outputs").exists())
            path.write_text(json.dumps({"instances":["tiny.tsp"],"iterationz":5}))
            with self.assertRaises(ValueError):load_campaign_config(path)

    def test_duplicate_comparison_rows_are_not_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            row=BenchmarkRecord("tiny",4,3,1.,"greedy","ok",10.,10.,0,.1,(1,2,3))
            save_benchmark_csv([row,row],root/"raw.csv")
            with self.assertRaises(ValueError):build_comparison_csv(root/"raw.csv",root/"none.csv",None,root/"out.csv")

    def test_campaign_can_be_replotted_after_removing_the_original_instance(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/"tiny.tsp";source.write_text(TSP)
            path=root/"config.json"
            path.write_text(json.dumps({"instances":["tiny.tsp"],"p_values":[3],"methods":["greedy"]}))
            folder=run_campaign(path,root/"outputs",make_plots=False)
            source.unlink()
            with patch("ring_star.experiments.execute",side_effect=AssertionError("Must not solve")):
                paths=replot_campaign(folder)
            self.assertGreater(len(paths),0)
            self.assertTrue((folder/"figures/by_instance/tiny_alpha_1.png").exists())


if __name__=="__main__":unittest.main()
