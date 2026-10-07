import tempfile
import textwrap
import unittest
from pathlib import Path

from ring_star.io import TsplibFormatError, load_tsplib_instance


class TsplibLoadingTests(unittest.TestCase):
    def test_loads_coordinate_instance(self):
        path = self.write_tsp(
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
        )

        instance = load_tsplib_instance(path)

        self.assertEqual(instance.name, "tiny")
        self.assertEqual(instance.n, 3)
        self.assertEqual(instance.required_station, 0)
        self.assertEqual(instance.edge_weight_type, "EUC_2D")
        self.assertEqual(instance.points, ((0.0, 0.0), (3.0, 0.0), (3.0, 4.0)))

    def test_accepts_headers_without_spaces_around_colon(self):
        path = self.write_tsp(
            """
            NAME: compact
            DIMENSION: 3
            NODE_COORD_SECTION
            1 0 0
            2 1 0
            3 0 1
            EOF
            """
        )

        instance = load_tsplib_instance(path)

        self.assertEqual(instance.name, "compact")
        self.assertEqual(instance.points[2], (0.0, 1.0))

    def test_sorts_points_by_tsplib_node_id(self):
        path = self.write_tsp(
            """
            NAME : unsorted
            DIMENSION : 3
            NODE_COORD_SECTION
            2 3 0
            1 0 0
            3 3 4
            EOF
            """
        )

        instance = load_tsplib_instance(path)

        self.assertEqual(instance.points, ((0.0, 0.0), (3.0, 0.0), (3.0, 4.0)))

    def test_rejects_dimension_mismatch(self):
        path = self.write_tsp(
            """
            NAME : broken
            DIMENSION : 4
            NODE_COORD_SECTION
            1 0 0
            2 3 0
            3 3 4
            EOF
            """
        )

        with self.assertRaises(TsplibFormatError):
            load_tsplib_instance(path)

    def test_rejects_missing_coordinate_section(self):
        path = self.write_tsp(
            """
            NAME : broken
            DIMENSION : 3
            EDGE_WEIGHT_TYPE : EUC_2D
            EOF
            """
        )

        with self.assertRaises(TsplibFormatError):
            load_tsplib_instance(path)

    def write_tsp(self, content):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "instance.tsp"
        path.write_text(textwrap.dedent(content).strip(), encoding="utf-8")
        return path


if __name__ == "__main__":
    unittest.main()
