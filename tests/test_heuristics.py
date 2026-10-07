import unittest

from ring_star.distances import build_distance_matrix
from ring_star.heuristics import (
    assign_to_nearest_station,
    build_greedy_solution,
    nearest_neighbor_cycle,
    select_stations_farthest_first,
    select_stations_grid_then_complete,
)
from ring_star.instance import RingStarInstance, RingStarProblem
from ring_star.validation import validate_solution


class HeuristicTests(unittest.TestCase):
    def setUp(self):
        self.instance = RingStarInstance(
            name="line",
            points=((0, 0), (1, 0), (2, 0), (10, 0), (11, 0)),
        )
        self.problem = RingStarProblem(self.instance, p=3, alpha=1.0)
        self.distances = build_distance_matrix(self.instance.points)

    def test_select_stations_farthest_first_keeps_required_station(self):
        stations = select_stations_farthest_first(self.problem, self.distances)

        self.assertEqual(len(stations), 3)
        self.assertIn(0, stations)
        self.assertEqual(stations, frozenset({0, 2, 4}))

    def test_select_stations_grid_then_complete_keeps_required_station(self):
        stations = select_stations_grid_then_complete(self.problem, self.distances)

        self.assertEqual(len(stations), 3)
        self.assertIn(0, stations)

    def test_assign_to_nearest_station_assigns_stations_to_themselves(self):
        assignments = assign_to_nearest_station(frozenset({0, 2, 4}), self.distances)

        self.assertEqual(assignments[0], 0)
        self.assertEqual(assignments[2], 2)
        self.assertEqual(assignments[4], 4)
        self.assertEqual(assignments[1], 0)
        self.assertEqual(assignments[3], 4)

    def test_nearest_neighbor_cycle_starts_at_required_station(self):
        cycle = nearest_neighbor_cycle(frozenset({0, 2, 4}), self.distances, start=0)

        self.assertEqual(cycle[0], 0)
        self.assertEqual(set(cycle), {0, 2, 4})
        self.assertEqual(len(cycle), 3)

    def test_build_greedy_solution_returns_valid_solution(self):
        solution = build_greedy_solution(self.problem)

        validate_solution(self.problem, solution)
        self.assertEqual(len(solution.stations), self.problem.p)
        self.assertIn(self.problem.required_station, solution.stations)


if __name__ == "__main__":
    unittest.main()
