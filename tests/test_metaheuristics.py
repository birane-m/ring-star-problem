import unittest

from ring_star.distances import build_distance_matrix
from ring_star.heuristics import build_greedy_solution
from ring_star.instance import RingStarInstance, RingStarProblem
from ring_star.metaheuristics import (
    build_local_search_solution,
    build_solution_from_stations,
    build_tabu_search_solution,
    improve_with_station_swaps,
    improve_with_tabu_search,
)
from ring_star.validation import validate_solution


class MetaheuristicTests(unittest.TestCase):
    def setUp(self):
        instance = RingStarInstance(
            name="toy",
            points=(
                (0, 0),
                (1, 0),
                (2, 0),
                (10, 0),
                (11, 0),
                (12, 0),
                (6, 4),
            ),
        )
        self.problem = RingStarProblem(instance=instance, p=3, alpha=1.0)
        self.distances = build_distance_matrix(instance.points)
        self.initial_solution = build_greedy_solution(self.problem)

    def test_build_solution_from_stations_returns_valid_solution(self):
        solution = build_solution_from_stations(
            self.problem,
            self.distances,
            frozenset({0, 3, 6}),
        )

        validate_solution(self.problem, solution)
        self.assertEqual(solution.stations, frozenset({0, 3, 6}))

    def test_station_swap_search_never_worsens_initial_solution(self):
        result = improve_with_station_swaps(
            self.problem,
            self.initial_solution,
            self.distances,
            iterations=50,
            seed=7,
        )

        validate_solution(self.problem, result.best_solution)
        self.assertLessEqual(result.best_cost, result.initial_cost)

    def test_station_swap_search_is_reproducible_with_seed(self):
        first = improve_with_station_swaps(
            self.problem,
            self.initial_solution,
            self.distances,
            iterations=50,
            seed=3,
        )
        second = improve_with_station_swaps(
            self.problem,
            self.initial_solution,
            self.distances,
            iterations=50,
            seed=3,
        )

        self.assertEqual(first.best_solution.stations, second.best_solution.stations)
        self.assertEqual(first.best_solution.cycle, second.best_solution.cycle)
        self.assertEqual(first.best_solution.assignments, second.best_solution.assignments)

    def test_build_local_search_solution_uses_default_iteration_budget(self):
        result = build_local_search_solution(self.problem, seed=0)

        validate_solution(self.problem, result.best_solution)
        self.assertEqual(result.iterations, max(500, 10 * self.problem.instance.n))

    def test_tabu_search_returns_valid_solution(self):
        result = improve_with_tabu_search(
            self.problem,
            self.initial_solution,
            self.distances,
            iterations=20,
            seed=0,
            tabu_tenure=3,
            candidates_per_iteration=5,
        )

        validate_solution(self.problem, result.best_solution)
        self.assertLessEqual(result.best_cost, result.initial_cost)
        self.assertEqual(result.tabu_tenure, 3)
        self.assertEqual(result.candidates_per_iteration, 5)

    def test_tabu_search_is_reproducible_with_seed(self):
        first = improve_with_tabu_search(
            self.problem,
            self.initial_solution,
            self.distances,
            iterations=20,
            seed=4,
            tabu_tenure=3,
            candidates_per_iteration=5,
        )
        second = improve_with_tabu_search(
            self.problem,
            self.initial_solution,
            self.distances,
            iterations=20,
            seed=4,
            tabu_tenure=3,
            candidates_per_iteration=5,
        )

        self.assertEqual(first.best_solution.stations, second.best_solution.stations)
        self.assertEqual(first.best_solution.cycle, second.best_solution.cycle)
        self.assertEqual(first.best_solution.assignments, second.best_solution.assignments)

    def test_build_tabu_search_solution_uses_default_iteration_budget(self):
        result = build_tabu_search_solution(
            self.problem,
            seed=0,
            tabu_tenure=3,
            candidates_per_iteration=5,
        )

        validate_solution(self.problem, result.best_solution)
        self.assertEqual(result.iterations, max(500, 10 * self.problem.instance.n))


if __name__ == "__main__":
    unittest.main()
