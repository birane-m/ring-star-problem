import unittest
from importlib.util import find_spec

from ring_star.distances import build_distance_matrix
from ring_star.exact import solve_exact_solution
from ring_star.instance import RingStarInstance, RingStarProblem
from ring_star.validation import validate_solution


@unittest.skipIf(find_spec("pulp") is None, "PuLP is not installed")
class ExactSolverTests(unittest.TestCase):
    def setUp(self):
        self.instance = RingStarInstance(
            name="tiny",
            points=(
                (0, 0),
                (1, 0),
                (1, 1),
                (0, 1),
            ),
        )
        self.problem = RingStarProblem(instance=self.instance, p=3, alpha=1.0)
        self.distances = build_distance_matrix(self.instance.points)

    def test_exact_solver_returns_valid_optimal_solution(self):
        result = solve_exact_solution(self.problem, solver_message=False)

        validate_solution(self.problem, result.solution)
        self.assertTrue(result.optimal)
        self.assertEqual(result.status, "Optimal")
        self.assertEqual(result.solver_name, "CBC")
        self.assertAlmostEqual(
            result.objective_value,
            result.solution.costs(self.distances, self.problem.alpha).total,
        )

    def test_exact_solver_keeps_required_station(self):
        result = solve_exact_solution(self.problem, solver_message=False)

        self.assertIn(self.problem.required_station, result.solution.stations)
        self.assertEqual(result.solution.cycle[0], self.problem.required_station)


if __name__ == "__main__":
    unittest.main()
