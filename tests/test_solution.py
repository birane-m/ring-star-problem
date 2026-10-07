import unittest

from ring_star.distances import build_distance_matrix
from ring_star.solution import RingStarSolution


class SolutionTests(unittest.TestCase):
    def test_costs_are_computed_from_cycle_and_assignments(self):
        points = ((0, 0), (3, 0), (3, 4), (0, 4))
        distances = build_distance_matrix(points)
        solution = RingStarSolution(
            stations={0, 1, 2},
            cycle=(0, 1, 2),
            assignments=(0, 1, 2, 0),
        )

        costs = solution.costs(distances, alpha=2.0)

        self.assertEqual(costs.metro, 12.0)
        self.assertEqual(costs.walking, 4.0)
        self.assertEqual(costs.total, 28.0)


if __name__ == "__main__":
    unittest.main()
