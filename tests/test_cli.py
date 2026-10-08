import tempfile
import textwrap
import unittest
import json
from contextlib import redirect_stdout
from io import StringIO
from importlib.util import find_spec
from pathlib import Path

from ring_star.cli import (
    default_tabu_result_output_path,
    default_tabu_solution_output_path,
    default_local_search_result_output_path,
    default_local_search_solution_output_path,
    default_greedy_result_markdown_output_path,
    default_greedy_result_output_path,
    default_greedy_solution_output_path,
    default_point_cloud_output_path,
    main,
)


class CliTests(unittest.TestCase):
    def test_default_point_cloud_output_path(self):
        self.assertEqual(
            default_point_cloud_output_path("data/att48.tsp"),
            Path("outputs/figures/instances/att48.png"),
        )

    def test_default_greedy_solution_output_path(self):
        self.assertEqual(
            default_greedy_solution_output_path("data/att48.tsp", 10),
            Path("outputs/figures/heuristics/att48_greedy_p10.png"),
        )

    def test_default_greedy_result_output_path(self):
        self.assertEqual(
            default_greedy_result_output_path("data/att48.tsp", 10),
            Path("outputs/results/heuristics/att48_greedy_p10.json"),
        )

    def test_default_greedy_result_markdown_output_path(self):
        self.assertEqual(
            default_greedy_result_markdown_output_path("data/att48.tsp", 10),
            Path("outputs/results/heuristics/att48_greedy_p10.md"),
        )

    def test_default_local_search_solution_output_path(self):
        self.assertEqual(
            default_local_search_solution_output_path("data/att48.tsp", 10),
            Path("outputs/figures/metaheuristics/att48_local_search_p10.png"),
        )

    def test_default_local_search_result_output_path(self):
        self.assertEqual(
            default_local_search_result_output_path("data/att48.tsp", 10),
            Path("outputs/results/metaheuristics/att48_local_search_p10.json"),
        )

    def test_default_tabu_solution_output_path(self):
        self.assertEqual(
            default_tabu_solution_output_path("data/att48.tsp", 10),
            Path("outputs/figures/metaheuristics/att48_tabu_p10.png"),
        )

    def test_default_tabu_result_output_path(self):
        self.assertEqual(
            default_tabu_result_output_path("data/att48.tsp", 10),
            Path("outputs/results/metaheuristics/att48_tabu_p10.json"),
        )

    @unittest.skipIf(find_spec("matplotlib") is None, "matplotlib is not installed")
    def test_plot_instance_command_writes_png(self):
        with tempfile.TemporaryDirectory() as directory:
            tsp_path = Path(directory) / "tiny.tsp"
            output_path = Path(directory) / "tiny.png"
            tsp_path.write_text(
                textwrap.dedent(
                    """
                    NAME : tiny
                    TYPE : TSP
                    DIMENSION : 3
                    EDGE_WEIGHT_TYPE : EUC_2D
                    NODE_COORD_SECTION
                    1 0 0
                    2 3 0
                    3 3 4
                    EOF
                    """
                ).strip(),
                encoding="utf-8",
            )

            with redirect_stdout(StringIO()):
                exit_code = main(
                    [
                        "plot-instance",
                        str(tsp_path),
                        "--output",
                        str(output_path),
                    ]
                )

            self.assertEqual(exit_code, 0)
            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)

    def test_solve_greedy_command_prints_solution_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            tsp_path = Path(directory) / "tiny.tsp"
            tsp_path.write_text(
                textwrap.dedent(
                    """
                    NAME : tiny
                    TYPE : TSP
                    DIMENSION : 4
                    EDGE_WEIGHT_TYPE : EUC_2D
                    NODE_COORD_SECTION
                    1 0 0
                    2 3 0
                    3 3 4
                    4 0 4
                    EOF
                    """
                ).strip(),
                encoding="utf-8",
            )

            output = StringIO()
            with redirect_stdout(output):
                exit_code = main(["solve-greedy", str(tsp_path), "3"])

            self.assertEqual(exit_code, 0)
            self.assertIn("Instance: tiny", output.getvalue())
            self.assertIn("stations:", output.getvalue())
            self.assertIn("total_cost:", output.getvalue())

    @unittest.skipIf(find_spec("matplotlib") is None, "matplotlib is not installed")
    def test_solve_greedy_command_can_write_solution_plot(self):
        with tempfile.TemporaryDirectory() as directory:
            tsp_path = Path(directory) / "tiny.tsp"
            output_path = Path(directory) / "solution.png"
            tsp_path.write_text(
                textwrap.dedent(
                    """
                    NAME : tiny
                    TYPE : TSP
                    DIMENSION : 4
                    EDGE_WEIGHT_TYPE : EUC_2D
                    NODE_COORD_SECTION
                    1 0 0
                    2 3 0
                    3 3 4
                    4 0 4
                    EOF
                    """
                ).strip(),
                encoding="utf-8",
            )

            with redirect_stdout(StringIO()):
                exit_code = main(
                    [
                        "solve-greedy",
                        str(tsp_path),
                        "3",
                        "--plot",
                        "--plot-output",
                        str(output_path),
                    ]
                )

            self.assertEqual(exit_code, 0)
            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)

    def test_solve_greedy_command_can_write_result_json(self):
        with tempfile.TemporaryDirectory() as directory:
            tsp_path = Path(directory) / "tiny.tsp"
            output_path = Path(directory) / "result.json"
            markdown_path = Path(directory) / "result.md"
            tsp_path.write_text(
                textwrap.dedent(
                    """
                    NAME : tiny
                    TYPE : TSP
                    DIMENSION : 4
                    EDGE_WEIGHT_TYPE : EUC_2D
                    NODE_COORD_SECTION
                    1 0 0
                    2 3 0
                    3 3 4
                    4 0 4
                    EOF
                    """
                ).strip(),
                encoding="utf-8",
            )

            with redirect_stdout(StringIO()):
                exit_code = main(
                    [
                        "solve-greedy",
                        str(tsp_path),
                        "3",
                        "--save-result",
                        "--result-output",
                        str(output_path),
                    ]
                )

            data = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(exit_code, 0)
            self.assertTrue(markdown_path.exists())
            self.assertEqual(data["instance"], "tiny")
            self.assertEqual(data["method"], "greedy")
            self.assertIn("stations", data)
            self.assertIn("assignments", data)
            self.assertIn("costs", data)

    def test_solve_local_search_command_prints_solution_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            tsp_path = Path(directory) / "tiny.tsp"
            tsp_path.write_text(
                textwrap.dedent(
                    """
                    NAME : tiny
                    TYPE : TSP
                    DIMENSION : 4
                    EDGE_WEIGHT_TYPE : EUC_2D
                    NODE_COORD_SECTION
                    1 0 0
                    2 3 0
                    3 3 4
                    4 0 4
                    EOF
                    """
                ).strip(),
                encoding="utf-8",
            )

            output = StringIO()
            with redirect_stdout(output):
                exit_code = main(
                    [
                        "solve-local-search",
                        str(tsp_path),
                        "3",
                        "--iterations",
                        "5",
                        "--seed",
                        "0",
                    ]
                )

            self.assertEqual(exit_code, 0)
            self.assertIn("Instance: tiny", output.getvalue())
            self.assertIn("accepted_moves:", output.getvalue())
            self.assertIn("total_cost:", output.getvalue())

    def test_solve_local_search_command_can_write_result_json(self):
        with tempfile.TemporaryDirectory() as directory:
            tsp_path = Path(directory) / "tiny.tsp"
            output_path = Path(directory) / "result.json"
            tsp_path.write_text(
                textwrap.dedent(
                    """
                    NAME : tiny
                    TYPE : TSP
                    DIMENSION : 4
                    EDGE_WEIGHT_TYPE : EUC_2D
                    NODE_COORD_SECTION
                    1 0 0
                    2 3 0
                    3 3 4
                    4 0 4
                    EOF
                    """
                ).strip(),
                encoding="utf-8",
            )

            with redirect_stdout(StringIO()):
                exit_code = main(
                    [
                        "solve-local-search",
                        str(tsp_path),
                        "3",
                        "--iterations",
                        "5",
                        "--save-result",
                        "--result-output",
                        str(output_path),
                    ]
                )

            data = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(exit_code, 0)
            self.assertEqual(data["method"], "local_search")
            self.assertTrue(output_path.with_suffix(".md").exists())

    def test_solve_tabu_command_prints_solution_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            tsp_path = Path(directory) / "tiny.tsp"
            tsp_path.write_text(
                textwrap.dedent(
                    """
                    NAME : tiny
                    TYPE : TSP
                    DIMENSION : 4
                    EDGE_WEIGHT_TYPE : EUC_2D
                    NODE_COORD_SECTION
                    1 0 0
                    2 3 0
                    3 3 4
                    4 0 4
                    EOF
                    """
                ).strip(),
                encoding="utf-8",
            )

            output = StringIO()
            with redirect_stdout(output):
                exit_code = main(
                    [
                        "solve-tabu",
                        str(tsp_path),
                        "3",
                        "--iterations",
                        "5",
                        "--seed",
                        "0",
                        "--tabu-tenure",
                        "2",
                        "--candidates-per-iteration",
                        "3",
                    ]
                )

            self.assertEqual(exit_code, 0)
            self.assertIn("Instance: tiny", output.getvalue())
            self.assertIn("tabu_tenure:", output.getvalue())
            self.assertIn("total_cost:", output.getvalue())

    def test_solve_tabu_command_can_write_result_json(self):
        with tempfile.TemporaryDirectory() as directory:
            tsp_path = Path(directory) / "tiny.tsp"
            output_path = Path(directory) / "result.json"
            tsp_path.write_text(
                textwrap.dedent(
                    """
                    NAME : tiny
                    TYPE : TSP
                    DIMENSION : 4
                    EDGE_WEIGHT_TYPE : EUC_2D
                    NODE_COORD_SECTION
                    1 0 0
                    2 3 0
                    3 3 4
                    4 0 4
                    EOF
                    """
                ).strip(),
                encoding="utf-8",
            )

            with redirect_stdout(StringIO()):
                exit_code = main(
                    [
                        "solve-tabu",
                        str(tsp_path),
                        "3",
                        "--iterations",
                        "5",
                        "--save-result",
                        "--result-output",
                        str(output_path),
                    ]
                )

            data = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(exit_code, 0)
            self.assertEqual(data["method"], "tabu_search")
            self.assertTrue(output_path.with_suffix(".md").exists())


if __name__ == "__main__":
    unittest.main()
