"""Seeded station-swap descent and tabu search with measurable work budgets."""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from random import Random
from time import perf_counter

from ring_star.distances import DistanceMatrix, build_distance_matrix
from ring_star.heuristics import (
    assign_to_nearest_station, build_greedy_solution, nearest_neighbor_cycle, two_opt_cycle,
)
from ring_star.instance import RingStarProblem
from ring_star.solution import RingStarSolution
from ring_star.validation import validate_solution


@dataclass(frozen=True)
class SearchStep:
    iteration: int
    evaluations: int
    elapsed_seconds: float
    current_cost: float
    best_cost: float


@dataclass(frozen=True)
class LocalSearchResult:
    initial_solution: RingStarSolution
    best_solution: RingStarSolution
    iterations: int
    accepted_moves: int
    initial_cost: float
    best_cost: float
    evaluated_moves: int = 0
    iteration_budget: int = 0
    stop_reason: str = "iteration_budget"
    history: tuple[SearchStep, ...] = ()


@dataclass(frozen=True)
class TabuSearchResult:
    initial_solution: RingStarSolution
    best_solution: RingStarSolution
    iterations: int
    performed_moves: int
    initial_cost: float
    best_cost: float
    tabu_tenure: int
    candidates_per_iteration: int
    evaluated_moves: int = 0
    iteration_budget: int = 0
    stop_reason: str = "iteration_budget"
    history: tuple[SearchStep, ...] = ()


def _integer(value: int, name: str, minimum: int = 0) -> None:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}.")


def _budget(iterations: int, seed: int, time_limit: float | None) -> None:
    _integer(iterations, "iterations")
    if type(seed) is not int:
        raise ValueError("seed must be an integer.")
    if time_limit is not None and (
        isinstance(time_limit, bool) or not isfinite(time_limit) or time_limit <= 0
    ):
        raise ValueError("Search time limit must be finite and strictly positive.")


def build_solution_from_stations(
    problem: RingStarProblem, distances: DistanceMatrix, stations: frozenset[int],
) -> RingStarSolution:
    solution = RingStarSolution(
        stations,
        two_opt_cycle(nearest_neighbor_cycle(stations, distances, problem.required_station), distances),
        assign_to_nearest_station(stations, distances),
    )
    validate_solution(problem, solution)
    return solution


def improve_with_station_swaps(
    problem: RingStarProblem, initial_solution: RingStarSolution,
    distances: DistanceMatrix, iterations: int, seed: int = 0,
    *, time_limit: float | None = None,
) -> LocalSearchResult:
    """Sample one swap per iteration; accept only strict improvements.

    A sampled descent does not certify a local optimum over the full neighborhood.
    The time budget concerns the improvement phase, not parsing or plotting.
    """
    _budget(iterations, seed, time_limit)
    validate_solution(problem, initial_solution)
    rng = Random(seed)
    current = initial_solution
    initial_cost = current.costs(distances, problem.alpha).total
    current_cost = initial_cost
    start = perf_counter()
    history = [SearchStep(0, 0, 0.0, current_cost, current_cost)]
    done = accepted = 0
    reason = "iteration_budget"
    for _ in range(iterations):
        if time_limit is not None and perf_counter() - start >= time_limit:
            reason = "time_budget"
            break
        removable = sorted(current.stations - {problem.required_station})
        non_stations = sorted(set(range(problem.instance.n)) - current.stations)
        if not removable or not non_stations:
            reason = "empty_neighborhood"
            break
        remove, add = rng.choice(removable), rng.choice(non_stations)
        candidate = build_solution_from_stations(
            problem, distances, (current.stations - {remove}) | {add},
        )
        value = candidate.costs(distances, problem.alpha).total
        done += 1
        if value < current_cost - 1e-10:
            current, current_cost = candidate, value
            accepted += 1
        history.append(SearchStep(done, done, perf_counter() - start, current_cost, current_cost))
    return LocalSearchResult(
        initial_solution, current, done, accepted, initial_cost, current_cost,
        done, iterations, reason, tuple(history),
    )


def _sample_unique_swaps(
    removable: list[int], non_stations: list[int], sample_size: int, random: Random,
) -> list[tuple[int, int]]:
    """Sample without replacement, with stable ordering and no rejection loop."""
    width = len(non_stations)
    return [
        (removable[index // width], non_stations[index % width])
        for index in random.sample(range(len(removable) * width), sample_size)
    ]


def improve_with_tabu_search(
    problem: RingStarProblem, initial_solution: RingStarSolution,
    distances: DistanceMatrix, iterations: int, seed: int = 0,
    tabu_tenure: int = 20, candidates_per_iteration: int | None = None,
    *, time_limit: float | None = None,
) -> TabuSearchResult:
    """Allow worsening moves; forbid re-adding removed stations for tenure steps.

    Aspiration allows a tabu move if it strictly improves the global best.
    The best solution is kept separately from the current solution.
    """
    _budget(iterations, seed, time_limit)
    _integer(tabu_tenure, "tabu_tenure")
    candidates = max(20, problem.instance.n) if candidates_per_iteration is None else candidates_per_iteration
    _integer(candidates, "candidates_per_iteration", 1)
    validate_solution(problem, initial_solution)
    rng = Random(seed)
    current = best = initial_solution
    current_cost = best_cost = initial_cost = current.costs(distances, problem.alpha).total
    tabu_until: dict[int, int] = {}
    start = perf_counter()
    history = [SearchStep(0, 0, 0.0, current_cost, best_cost)]
    done = performed = evaluated = 0
    reason = "iteration_budget"
    for iteration in range(iterations):
        if time_limit is not None and perf_counter() - start >= time_limit:
            reason = "time_budget"
            break
        removable = sorted(current.stations - {problem.required_station})
        non_stations = sorted(set(range(problem.instance.n)) - current.stations)
        if not removable or not non_stations:
            reason = "empty_neighborhood"
            break
        swaps = _sample_unique_swaps(
            removable, non_stations, min(candidates, len(removable) * len(non_stations)), rng,
        )
        chosen = None
        for remove, add in swaps:
            if time_limit is not None and perf_counter() - start >= time_limit:
                reason = "time_budget"
                break
            solution = build_solution_from_stations(
                problem, distances, (current.stations - {remove}) | {add},
            )
            value = solution.costs(distances, problem.alpha).total
            evaluated += 1
            if iteration < tabu_until.get(add, -1) and value >= best_cost - 1e-10:
                continue
            if chosen is None or value < chosen[3] - 1e-10:
                chosen = (remove, add, solution, value)
        done += 1
        if chosen is not None:
            remove, _, current, current_cost = chosen
            performed += 1
            # A tenure of one blocks re-entry on the next iteration.
            tabu_until[remove] = iteration + tabu_tenure + 1
            if current_cost < best_cost - 1e-10:
                best, best_cost = current, current_cost
        history.append(SearchStep(done, evaluated, perf_counter() - start, current_cost, best_cost))
        if reason == "time_budget":
            break
    return TabuSearchResult(
        initial_solution, best, done, performed, initial_cost, best_cost,
        tabu_tenure, candidates, evaluated, iterations, reason, tuple(history),
    )


def build_local_search_solution(
    problem: RingStarProblem, iterations: int | None = None, seed: int = 0,
    *, distances: DistanceMatrix | None = None, time_limit: float | None = None,
) -> LocalSearchResult:
    if distances is None:
        distances = build_distance_matrix(problem.instance.points)
    initial = build_greedy_solution(problem, distances=distances)
    return improve_with_station_swaps(
        problem, initial, distances,
        iterations if iterations is not None else max(500, 10 * problem.instance.n),
        seed, time_limit=time_limit,
    )


def build_tabu_search_solution(
    problem: RingStarProblem, iterations: int | None = None, seed: int = 0,
    tabu_tenure: int = 20, candidates_per_iteration: int | None = None,
    *, distances: DistanceMatrix | None = None, time_limit: float | None = None,
) -> TabuSearchResult:
    if distances is None:
        distances = build_distance_matrix(problem.instance.points)
    initial = build_greedy_solution(problem, distances=distances)
    return improve_with_tabu_search(
        problem, initial, distances,
        iterations if iterations is not None else max(500, 10 * problem.instance.n),
        seed, tabu_tenure, candidates_per_iteration, time_limit=time_limit,
    )
