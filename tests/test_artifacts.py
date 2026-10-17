import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from ring_star.artifacts import load_saved_solution, save_run, replot_run
from ring_star.execution import RunConfig, execute
from ring_star.instance import RingStarInstance,RingStarProblem
from ring_star.cli import main


class ArtifactTests(unittest.TestCase):
    def setUp(self):
        self.problem=RingStarProblem(RingStarInstance("tiny",((0,0),(2,0),(2,2),(0,2))),3)

    def test_repeated_runs_do_not_overwrite_and_are_self_contained(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=execute(self.problem,RunConfig("local_search",iterations=5,seed=4))
            a=save_run(self.problem,result,output_root=tmp,make_plots=False)
            b=save_run(self.problem,result,output_root=tmp,make_plots=False)
            self.assertNotEqual(a,b)
            for folder in (a,b):
                for filename in ("configuration.json","environment.json","solution.json","summary.md","history.csv","initial_solution.json"):
                    self.assertTrue((folder/filename).exists())
                problem,solution,data=load_saved_solution(folder/"solution.json")
                self.assertEqual(problem,self.problem)
                self.assertEqual(solution,result.solution)
                self.assertEqual(data["configuration"]["seed"],4)
                self.assertIsNone(data["plot"])
            self.assertIn(a.name,(Path(tmp)/"index.md").read_text())

    def test_tampered_cost_is_rejected_before_plotting(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=execute(self.problem,RunConfig("greedy"))
            folder=save_run(self.problem,result,output_root=tmp,make_plots=False)
            path=folder/"solution.json"
            data=json.loads(path.read_text())
            for value in (999.,float("nan")):
                data["costs"]["total"]=value
                path.write_text(json.dumps(data))
                with self.assertRaises(ValueError):load_saved_solution(path)

    def test_reordered_assignments_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=save_run(self.problem,execute(self.problem,RunConfig("greedy")),output_root=tmp,make_plots=False)
            path=folder/"solution.json"
            data=json.loads(path.read_text())
            data["assignments"].reverse()
            path.write_text(json.dumps(data))
            with self.assertRaises(ValueError):load_saved_solution(path)

    def test_no_solution_run_keeps_diagnostics_without_a_fake_cycle(self):
        from ring_star.execution import RunResult
        result=RunResult(RunConfig("exact_plne"),None,"no_solution_time_limit",.01,
                         solver_log="Stopped on time limit",error="No incumbent")
        with tempfile.TemporaryDirectory() as tmp:
            folder=save_run(self.problem,result,output_root=tmp,make_plots=True)
            data=json.loads((folder/"solution.json").read_text())
            self.assertNotIn("cycle",data)
            self.assertEqual(data["status"],"no_solution_time_limit")
            self.assertTrue((folder/"solver.log").exists())
            with self.assertRaises(ValueError):load_saved_solution(folder/"solution.json")

    def test_plot_saved_keeps_the_saved_cycle(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=execute(self.problem,RunConfig("greedy"))
            folder=save_run(self.problem,result,output_root=tmp,make_plots=False)
            with patch("ring_star.cli.save_solution_png") as plotted:
                status=main(["plot-saved",str(folder/"solution.json"),"-o",str(Path(tmp)/"plot.png")])
            self.assertEqual(status,0)
            self.assertEqual(plotted.call_args.args[1].cycle,result.solution.cycle)

    def test_png_pdf_svg_and_convergence_are_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            result=execute(self.problem,RunConfig("tabu_search",iterations=3,candidates_per_iteration=2))
            folder=save_run(self.problem,result,output_root=tmp)
            for stem in ("solution","before_after","convergence"):
                for extension in ("png","pdf","svg"):
                    self.assertGreater((folder/"figures"/f"{stem}.{extension}").stat().st_size,0)

    def test_replot_has_no_dependency_on_original_input_file(self):
        import shutil
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            folder=save_run(self.problem,execute(self.problem,RunConfig("greedy")),output_root=root,make_plots=False)
            moved=root/"moved"
            shutil.move(str(folder),str(moved))
            with patch("ring_star.execution.execute",side_effect=AssertionError("Must not solve again")):
                replot_run(moved)
            self.assertTrue((moved/"figures/solution.png").exists())


if __name__=="__main__":unittest.main()
