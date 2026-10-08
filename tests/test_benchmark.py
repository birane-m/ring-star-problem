import csv
import tempfile
import unittest
from pathlib import Path

from ring_star.benchmark import (
    build_comparison_csv,
    default_benchmark_p_values,
    run_benchmark,
    save_benchmark_csv,
)


class BenchmarkTests(unittest.TestCase):
    def test_default_benchmark_p_values_are_valid_and_increasing(self):
        p_values = default_benchmark_p_values(100)

        self.assertEqual(tuple(sorted(p_values)), p_values)
        self.assertTrue(all(3 <= p <= 100 for p in p_values))
        self.assertIn(3, p_values)

    def test_run_benchmark_compares_basic_methods(self):
        with tempfile.TemporaryDirectory() as directory:
            tsp_path = Path(directory) / "tiny.tsp"
            tsp_path.write_text(
                "\n".join(
                    [
                        "NAME : tiny",
                        "TYPE : TSP",
                        "DIMENSION : 4",
                        "EDGE_WEIGHT_TYPE : EUC_2D",
                        "NODE_COORD_SECTION",
                        "1 0 0",
                        "2 3 0",
                        "3 3 4",
                        "4 0 4",
                        "EOF",
                    ]
                ),
                encoding="utf-8",
            )

            records = run_benchmark(
                [tsp_path],
                methods=("greedy", "local_search", "tabu_search"),
                p_values=(3,),
                local_iterations=5,
                tabu_iterations=5,
                candidates_per_iteration=3,
            )

            self.assertEqual(len(records), 3)
            self.assertEqual({record.status for record in records}, {"ok"})
            self.assertEqual(
                {record.method for record in records},
                {"greedy", "local_search", "tabu_search"},
            )

    def test_save_benchmark_csv_writes_readable_file(self):
        with tempfile.TemporaryDirectory() as directory:
            tsp_path = Path(directory) / "tiny.tsp"
            output_path = Path(directory) / "benchmark.csv"
            tsp_path.write_text(
                "\n".join(
                    [
                        "NAME : tiny",
                        "TYPE : TSP",
                        "DIMENSION : 4",
                        "EDGE_WEIGHT_TYPE : EUC_2D",
                        "NODE_COORD_SECTION",
                        "1 0 0",
                        "2 3 0",
                        "3 3 4",
                        "4 0 4",
                        "EOF",
                    ]
                ),
                encoding="utf-8",
            )
            records = run_benchmark(
                [tsp_path],
                methods=("greedy",),
                p_values=(3,),
            )

            save_benchmark_csv(records, output_path)

            with output_path.open(encoding="utf-8") as csv_file:
                rows = list(csv.DictReader(csv_file))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["instance"], "tiny")
            self.assertEqual(rows[0]["method"], "greedy")
            self.assertEqual(rows[0]["status"], "ok")

    def test_build_comparison_csv_merges_method_results(self):
        with tempfile.TemporaryDirectory() as directory:
            directory_path = Path(directory)
            greedy_path = directory_path / "greedy.csv"
            meta_path = directory_path / "meta.csv"
            exact_path = directory_path / "exact.csv"
            output_path = directory_path / "comparison.csv"
            header = (
                "instance,n,p,alpha,method,status,total_cost,metro_cost,"
                "walking_cost,elapsed_seconds,stations,error\n"
            )
            greedy_path.write_text(
                header
                + "tiny,4,3,1.0,greedy,ok,10.0,6.0,4.0,0.1,1 2 3,\n",
                encoding="utf-8",
            )
            meta_path.write_text(
                header
                + "tiny,4,3,1.0,local_search,ok,8.0,5.0,3.0,0.2,1 2 4,\n"
                + "tiny,4,3,1.0,tabu_search,ok,7.0,4.0,3.0,0.3,1 3 4,\n",
                encoding="utf-8",
            )
            exact_path.write_text(
                header
                + "tiny,4,3,1.0,exact_plne,optimal,7.0,4.0,3.0,1.0,1 3 4,\n",
                encoding="utf-8",
            )

            build_comparison_csv(greedy_path, meta_path, exact_path, output_path)

            with output_path.open(encoding="utf-8") as csv_file:
                rows = list(csv.DictReader(csv_file))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["best_method"], "tabu_search")
            self.assertEqual(rows[0]["gain_best_vs_greedy_percent"], "30.000000")
            self.assertEqual(rows[0]["exact_status"], "optimal")


if __name__ == "__main__":
    unittest.main()
