import unittest

from ring_star.instance import RingStarInstance, RingStarProblem
from ring_star.solution import RingStarSolution
from ring_star.validation import SolutionValidationError, validate_solution


class ValidationTests(unittest.TestCase):
    def setUp(self):
        instance = RingStarInstance(
            name="toy",
            points=((0, 0), (3, 0), (3, 4), (0, 4)),
        )
        self.problem = RingStarProblem(instance=instance, p=3, alpha=1.0)

    def test_valid_solution_passes(self):
        solution = RingStarSolution(
            stations={0, 1, 2},
            cycle=(0, 1, 2),
            assignments=(0, 1, 2, 0),
        )

        validate_solution(self.problem, solution)

    def test_missing_required_station_fails(self):
        solution = RingStarSolution(
            stations={1, 2, 3},
            cycle=(1, 2, 3),
            assignments=(1, 1, 2, 3),
        )

        with self.assertRaises(SolutionValidationError):
            validate_solution(self.problem, solution)

    def test_assignment_to_non_station_fails(self):
        solution = RingStarSolution(
            stations={0, 1, 2},
            cycle=(0, 1, 2),
            assignments=(0, 1, 2, 3),
        )

        with self.assertRaises(SolutionValidationError):
            validate_solution(self.problem, solution)

    def test_incomplete_cycle_fails(self):
        solution = RingStarSolution(
            stations={0, 1, 2},
            cycle=(0, 1),
            assignments=(0, 1, 2, 0),
        )

        with self.assertRaises(SolutionValidationError):
            validate_solution(self.problem, solution)


if __name__ == "__main__":
    unittest.main()
