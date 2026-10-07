import tempfile
import unittest
from importlib.util import find_spec
from pathlib import Path

from ring_star.instance import RingStarInstance
from ring_star.solution import RingStarSolution
from ring_star.visualization import save_point_cloud_png, save_solution_png


class VisualizationTests(unittest.TestCase):
    @unittest.skipIf(find_spec("matplotlib") is None, "matplotlib is not installed")
    def test_save_point_cloud_png_writes_file(self):
        instance = RingStarInstance(
            name="toy",
            points=((0, 0), (3, 0), (3, 4), (0, 4)),
        )

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "toy.png"

            result = save_point_cloud_png(instance, path)

            self.assertEqual(result, path)
            self.assertTrue(path.exists())
            self.assertGreater(path.stat().st_size, 0)

    @unittest.skipIf(find_spec("matplotlib") is None, "matplotlib is not installed")
    def test_save_solution_png_writes_file(self):
        instance = RingStarInstance(
            name="toy",
            points=((0, 0), (3, 0), (3, 4), (0, 4)),
        )
        solution = RingStarSolution(
            stations={0, 1, 2},
            cycle=(0, 1, 2),
            assignments=(0, 1, 2, 0),
        )

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "solution.png"

            result = save_solution_png(instance, solution, path)

            self.assertEqual(result, path)
            self.assertTrue(path.exists())
            self.assertGreater(path.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
