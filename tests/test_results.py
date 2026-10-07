import json
import tempfile
import unittest
from pathlib import Path

from ring_star.distances import build_distance_matrix
from ring_star.instance import RingStarInstance, RingStarProblem
from ring_star.results import (
    save_solution_result_json,
    save_solution_result_markdown,
    solution_result_data,
    solution_result_markdown,
)
from ring_star.solution import RingStarSolution


class ResultExportTests(unittest.TestCase):
    def setUp(self):
        instance = RingStarInstance(
            name="toy",
            points=((0, 0), (3, 0), (3, 4), (0, 4)),
            edge_weight_type="EUC_2D",
        )
        self.problem = RingStarProblem(instance=instance, p=3, alpha=2.0)
        self.distances = build_distance_matrix(instance.points)
        self.solution = RingStarSolution(
            stations={0, 1, 2},
            cycle=(0, 1, 2),
            assignments=(0, 1, 2, 0),
        )

    def test_solution_result_data_uses_tsplib_numbering(self):
        data = solution_result_data(
            self.problem,
            self.solution,
            self.distances,
            method="greedy",
            plot_path="plot.png",
        )

        self.assertEqual(data["required_station"], 1)
        self.assertEqual(data["stations"], [1, 2, 3])
        self.assertEqual(data["cycle"], [1, 2, 3])
        self.assertEqual(data["assignments"][3], {"point": 4, "station": 1})
        self.assertEqual(data["costs"]["total"], 28.0)
        self.assertEqual(data["plot"], "plot.png")

    def test_save_solution_result_json_writes_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "result.json"

            result = save_solution_result_json(
                self.problem,
                self.solution,
                self.distances,
                method="greedy",
                output_path=path,
            )

            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(result, path)
            self.assertEqual(data["instance"], "toy")
            self.assertEqual(data["method"], "greedy")

    def test_solution_result_markdown_is_human_readable(self):
        markdown = solution_result_markdown(
            self.problem,
            self.solution,
            self.distances,
            method="greedy",
            plot_path="plot.png",
        )

        self.assertIn("# Résultat greedy - toy", markdown)
        self.assertIn("## Coûts", markdown)
        self.assertIn("1 -> 2 -> 3 -> 1", markdown)
        self.assertIn("## Affectations par station", markdown)
        self.assertIn("| 1 | 1, 4 | 2 |", markdown)
        self.assertIn("## Affectations détaillées par point", markdown)
        self.assertIn("| Point | Station |", markdown)
        self.assertIn("plot.png", markdown)

    def test_save_solution_result_markdown_writes_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "result.md"

            result = save_solution_result_markdown(
                self.problem,
                self.solution,
                self.distances,
                method="greedy",
                output_path=path,
            )

            self.assertEqual(result, path)
            self.assertIn("Résultat greedy - toy", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
