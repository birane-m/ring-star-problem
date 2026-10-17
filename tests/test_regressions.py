"""Counterexamples and independent mathematical checks, beyond feasibility tests."""
import itertools
import math
import unittest
from importlib.util import find_spec
from unittest.mock import patch

from ring_star.distances import build_distance_matrix
from ring_star.exact import ExactSolveError, solve_exact_solution
from ring_star.execution import RunConfig
from ring_star.heuristics import two_opt_cycle
from ring_star.instance import RingStarInstance, RingStarProblem
from ring_star.metaheuristics import build_local_search_solution, build_tabu_search_solution, _sample_unique_swaps
from random import Random


def enumerate_optimum(problem):
    """Independent exhaustive reference for tiny instances, including a nonzero root."""
    distances = build_distance_matrix(problem.instance.points)
    root = problem.required_station
    best = math.inf
    for others in itertools.combinations(sorted(set(range(problem.instance.n)) - {root}), problem.p-1):
        stations = (root, *others)
        walking = sum(min(distances[i][s] for s in stations) for i in range(problem.instance.n))
        ring = min(sum(distances[a][b] for a, b in zip((root, *order), (*order, root))) for order in itertools.permutations(others))
        best = min(best, walking + problem.alpha * ring)
    return best


class AlgorithmRegressions(unittest.TestCase):
    def setUp(self):
        self.instance = RingStarInstance("square", ((0,0),(1,0),(1,1),(0,1)))
        self.distances = build_distance_matrix(self.instance.points)

    def test_two_opt_uncrosses_closing_edge(self):
        improved = two_opt_cycle((0,1,3,2), self.distances)
        cost = sum(self.distances[a][b] for a,b in zip(improved, improved[1:]+improved[:1]))
        self.assertAlmostEqual(cost, 4.0)
        self.assertEqual(improved[0], 0)

    def test_all_square_tours_are_improved_to_the_perimeter(self):
        for rest in itertools.permutations((1,2,3)):
            improved = two_opt_cycle((0,*rest), self.distances)
            self.assertAlmostEqual(sum(self.distances[a][b] for a,b in zip(improved, improved[1:]+improved[:1])),4.)

    def test_invalid_model_parameters_fail_early(self):
        for p in (3.5, True, 2, 5):
            with self.subTest(p=p), self.assertRaises(ValueError):
                RingStarProblem(self.instance, p)
        for alpha in (math.nan, math.inf, -1, True):
            with self.subTest(alpha=alpha), self.assertRaises(ValueError):
                RingStarProblem(self.instance,3,alpha)
        for coordinate in (math.nan, math.inf, -math.inf):
            with self.assertRaises(ValueError):
                RingStarInstance("bad",((coordinate,0),(1,1),(2,2)))

    def test_zero_tabu_candidates_are_not_a_default_value(self):
        with self.assertRaises(ValueError):
            build_tabu_search_solution(RingStarProblem(self.instance,3), candidates_per_iteration=0)

    def test_unique_sampling_can_cover_the_entire_neighborhood(self):
        swaps = _sample_unique_swaps([1,2],[3,4,5],6,Random(0))
        self.assertEqual(set(swaps), set(itertools.product([1,2],[3,4,5])))
        self.assertEqual(swaps, _sample_unique_swaps([1,2],[3,4,5],6,Random(0)))

    def test_p_equals_n_stops_without_fake_iterations(self):
        problem = RingStarProblem(self.instance,4)
        for builder in (build_local_search_solution,build_tabu_search_solution):
            result = builder(problem,iterations=50)
            self.assertEqual(result.iterations,0)
            self.assertEqual(result.evaluated_moves,0)
            self.assertEqual(result.stop_reason,"empty_neighborhood")

    def test_trace_best_cost_is_monotone_and_matches_final_cost(self):
        instance = RingStarInstance("toy",((0,0),(1,1),(3,1),(7,2),(2,6),(9,9),(4,7)))
        result = build_tabu_search_solution(RingStarProblem(instance,3),iterations=30,seed=4,candidates_per_iteration=5)
        values = [step.best_cost for step in result.history]
        self.assertTrue(all(a >= b for a,b in zip(values,values[1:])))
        self.assertAlmostEqual(values[-1],result.best_cost)
        self.assertEqual(result.evaluated_moves,result.history[-1].evaluations)
        self.assertEqual(result.evaluated_moves,150)

    def test_zero_iterations_does_no_improvement_work(self):
        for builder in (build_local_search_solution,build_tabu_search_solution):
            result=builder(RingStarProblem(self.instance,3),iterations=0)
            self.assertEqual(result.best_solution,result.initial_solution)
            self.assertEqual(result.evaluated_moves,0)

    def test_time_budget_stops_search_and_is_recorded(self):
        result=build_tabu_search_solution(RingStarProblem(self.instance,3),iterations=1000000,time_limit=.001)
        self.assertEqual(result.stop_reason,"time_budget")
        self.assertLess(result.iterations,1000000)

    def test_negative_and_nonfinite_budgets_are_rejected(self):
        for value in (-1,math.nan,math.inf):
            with self.assertRaises(ValueError):
                RunConfig(time_limit=value)


@unittest.skipIf(find_spec("pulp") is None,"PuLP unavailable")
class ExactRegressions(unittest.TestCase):
    def setUp(self):
        self.instance=RingStarInstance("tiny",((0,0),(2,0),(3,3),(1,5),(6,2)),required_station=2)

    def test_matches_independent_enumeration(self):
        for p,alpha in ((3,0.),(3,1.),(4,3.),(5,1.)):
            with self.subTest(p=p,alpha=alpha):
                problem=RingStarProblem(self.instance,p,alpha)
                result=solve_exact_solution(problem,time_limit=10)
                self.assertTrue(result.optimal)
                self.assertEqual(result.status,"Optimal")
                self.assertAlmostEqual(result.objective_value,enumerate_optimum(problem),places=6)
                self.assertAlmostEqual(result.relative_gap,0.)

    def test_zero_constant_objective_and_duplicate_points(self):
        problem=RingStarProblem(RingStarInstance("zeros",((0,0),)*4),3,0)
        result=solve_exact_solution(problem)
        self.assertEqual(result.objective_value,0.)
        self.assertTrue(result.optimal)

    def test_feasible_incumbent_is_not_an_optimality_certificate(self):
        import pulp
        original=pulp.LpProblem.solve
        def feasible(model,*args,**kwargs):
            outcome=original(model,*args,**kwargs)
            model.sol_status=pulp.LpSolutionIntegerFeasible
            return outcome
        with patch.object(pulp.LpProblem,"solve",feasible):
            result=solve_exact_solution(RingStarProblem(self.instance,3),time_limit=10)
        self.assertFalse(result.optimal)
        self.assertEqual(result.status,"feasible_time_limited")

    def test_no_incumbent_does_not_round_fractional_values(self):
        import pulp
        def unsolved(model,*args,**kwargs):
            model.status=pulp.LpStatusNotSolved
            model.sol_status=pulp.LpSolutionNoSolutionFound
            return model.status
        with patch.object(pulp.LpProblem,"solve",unsolved),self.assertRaises(ExactSolveError) as caught:
            solve_exact_solution(RingStarProblem(self.instance,3),time_limit=.01)
        self.assertEqual(caught.exception.status,"no_solution_time_limit")


if __name__=="__main__":
    unittest.main()
