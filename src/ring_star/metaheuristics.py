"""Metaheuristics for improving Ring-Star solutions.

The constructive greedy heuristic gives a fast feasible solution, but it fixes
the station set after one pass. This module improves such a solution with a
simple stochastic local search and a tabu search.

Neighborhood:

* remove one selected station, except the required station;
* add one non-station point;
* rebuild assignments and the station cycle;
* keep the move only if the total objective value decreases.

Both searches are stochastic because candidate swaps are sampled randomly, but
they are reproducible through an explicit random seed.
"""

from __future__ import annotations

from dataclasses import dataclass
from random import Random

from ring_star.distances import DistanceMatrix, build_distance_matrix
from ring_star.heuristics import (
    assign_to_nearest_station,
    build_greedy_solution,
    nearest_neighbor_cycle,
    two_opt_cycle,
)
from ring_star.instance import RingStarProblem
from ring_star.solution import RingStarSolution
from ring_star.validation import validate_solution


@dataclass(frozen=True)
class LocalSearchResult:
    """Summary of a stochastic local search run."""

    initial_solution: RingStarSolution
    best_solution: RingStarSolution
    iterations: int
    accepted_moves: int
    initial_cost: float
    best_cost: float


@dataclass(frozen=True)
class TabuSearchResult:
    """Summary of a tabu search run."""

    initial_solution: RingStarSolution
    best_solution: RingStarSolution
    iterations: int
    performed_moves: int
    initial_cost: float
    best_cost: float
    tabu_tenure: int
    candidates_per_iteration: int


def improve_with_station_swaps(
    problem: RingStarProblem,
    initial_solution: RingStarSolution,
    distances: DistanceMatrix,
    iterations: int,
    seed: int = 0,
) -> LocalSearchResult:
    """Improve a solution by stochastic station/non-station swaps.

    The method is a descent heuristic: worsening moves are rejected. This keeps
    the algorithm easy to explain and guarantees that the returned solution is
    never worse than the initial one for the same cost function.
    """

    if iterations < 0:
        raise ValueError("Number of iterations must be non-negative.")

    validate_solution(problem, initial_solution)

    random = Random(seed)
    current_solution = initial_solution
    current_cost = initial_solution.costs(distances, problem.alpha).total
    best_solution = initial_solution
    best_cost = current_cost
    accepted_moves = 0

    for _ in range(iterations):
        station_to_remove = _sample_removable_station(
            current_solution,
            problem,
            random,
        )
        point_to_add = _sample_non_station(
            current_solution,
            problem,
            random,
        )
        if station_to_remove is None or point_to_add is None:
            break

        candidate_stations = set(current_solution.stations)
        candidate_stations.remove(station_to_remove)
        candidate_stations.add(point_to_add)
        candidate_solution = build_solution_from_stations(
            problem,
            distances,
            frozenset(candidate_stations),
        )
        candidate_cost = candidate_solution.costs(distances, problem.alpha).total

        if candidate_cost < current_cost:
            current_solution = candidate_solution
            current_cost = candidate_cost
            accepted_moves += 1

            if candidate_cost < best_cost:
                best_solution = candidate_solution
                best_cost = candidate_cost

    return LocalSearchResult(
        initial_solution=initial_solution,
        best_solution=best_solution,
        iterations=iterations,
        accepted_moves=accepted_moves,
        initial_cost=initial_solution.costs(distances, problem.alpha).total,
        best_cost=best_cost,
    )


def build_local_search_solution(
    problem: RingStarProblem,
    iterations: int | None = None,
    seed: int = 0,
) -> LocalSearchResult:
    """Build a greedy solution and improve it with station swaps."""

    distances = build_distance_matrix(problem.instance.points)
    initial_solution = build_greedy_solution(problem)
    iteration_budget = iterations if iterations is not None else max(500, 10 * problem.instance.n)
    return improve_with_station_swaps(
        problem,
        initial_solution,
        distances,
        iterations=iteration_budget,
        seed=seed,
    )


def improve_with_tabu_search(
    problem: RingStarProblem,
    initial_solution: RingStarSolution,
    distances: DistanceMatrix,
    iterations: int,
    seed: int = 0,
    tabu_tenure: int = 20,
    candidates_per_iteration: int | None = None,
) -> TabuSearchResult:
    """Improve a solution with a stochastic tabu search.

    Tabu search uses the same swap neighborhood as the descent heuristic, but it
    may accept a worse current solution to escape local optima. Recently removed
    stations are marked tabu, meaning they cannot be immediately re-added unless
    the move improves the best solution found so far.
    """

    if iterations < 0:
        raise ValueError("Number of iterations must be non-negative.")
    if tabu_tenure < 0:
        raise ValueError("Tabu tenure must be non-negative.")

    validate_solution(problem, initial_solution)

    random = Random(seed)
    current_solution = initial_solution
    current_cost = initial_solution.costs(distances, problem.alpha).total
    best_solution = initial_solution
    best_cost = current_cost
    tabu_until: dict[int, int] = {}
    performed_moves = 0
    sampled_candidates = candidates_per_iteration or max(20, problem.instance.n)

    if sampled_candidates <= 0:
        raise ValueError("Candidates per iteration must be positive.")

    for iteration in range(iterations):
        candidate = _best_admissible_sampled_swap(
            problem,
            current_solution,
            distances,
            random,
            sampled_candidates,
            tabu_until,
            iteration,
            best_cost,
        )
        if candidate is None:
            continue

        station_to_remove, point_to_add, candidate_solution, candidate_cost = candidate
        current_solution = candidate_solution
        current_cost = candidate_cost
        performed_moves += 1

        # Forbid immediately undoing the move by re-adding the removed station.
        tabu_until[station_to_remove] = iteration + tabu_tenure

        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

    return TabuSearchResult(
        initial_solution=initial_solution,
        best_solution=best_solution,
        iterations=iterations,
        performed_moves=performed_moves,
        initial_cost=initial_solution.costs(distances, problem.alpha).total,
        best_cost=best_cost,
        tabu_tenure=tabu_tenure,
        candidates_per_iteration=sampled_candidates,
    )


def build_tabu_search_solution(
    problem: RingStarProblem,
    iterations: int | None = None,
    seed: int = 0,
    tabu_tenure: int = 20,
    candidates_per_iteration: int | None = None,
) -> TabuSearchResult:
    """Build a greedy solution and improve it with tabu search."""

    distances = build_distance_matrix(problem.instance.points)
    initial_solution = build_greedy_solution(problem)
    iteration_budget = iterations if iterations is not None else max(500, 10 * problem.instance.n)
    return improve_with_tabu_search(
        problem,
        initial_solution,
        distances,
        iterations=iteration_budget,
        seed=seed,
        tabu_tenure=tabu_tenure,
        candidates_per_iteration=candidates_per_iteration,
    )


def build_solution_from_stations(
    problem: RingStarProblem,
    distances: DistanceMatrix,
    stations: frozenset[int],
) -> RingStarSolution:
    """Rebuild assignments and the 2-opt-improved cycle for a station set."""

    assignments = assign_to_nearest_station(stations, distances)
    cycle = two_opt_cycle(
        nearest_neighbor_cycle(stations, distances, problem.required_station),
        distances,
    )
    solution = RingStarSolution(
        stations=stations,
        cycle=cycle,
        assignments=assignments,
    )
    validate_solution(problem, solution)
    return solution


def _sample_removable_station(
    solution: RingStarSolution,
    problem: RingStarProblem,
    random: Random,
) -> int | None:
    removable = sorted(
        station
        for station in solution.stations
        if station != problem.required_station
    )
    if not removable:
        return None
    return random.choice(removable)


def _sample_non_station(
    solution: RingStarSolution,
    problem: RingStarProblem,
    random: Random,
) -> int | None:
    non_stations = [
        point
        for point in range(problem.instance.n)
        if point not in solution.stations
    ]
    if not non_stations:
        return None
    return random.choice(non_stations)


def _best_admissible_sampled_swap(
    problem: RingStarProblem,
    solution: RingStarSolution,
    distances: DistanceMatrix,
    random: Random,
    candidates_per_iteration: int,
    tabu_until: dict[int, int],
    iteration: int,
    best_cost: float,
) -> tuple[int, int, RingStarSolution, float] | None:
    removable = sorted(
        station
        for station in solution.stations
        if station != problem.required_station
    )
    non_stations = [
        point
        for point in range(problem.instance.n)
        if point not in solution.stations
    ]
    if not removable or not non_stations:
        return None

    max_candidates = len(removable) * len(non_stations)
    sample_size = min(candidates_per_iteration, max_candidates)
    sampled_swaps = _sample_unique_swaps(removable, non_stations, sample_size, random)
    best_candidate: tuple[int, int, RingStarSolution, float] | None = None

    for station_to_remove, point_to_add in sampled_swaps:
        candidate_stations = set(solution.stations)
        candidate_stations.remove(station_to_remove)
        candidate_stations.add(point_to_add)
        candidate_solution = build_solution_from_stations(
            problem,
            distances,
            frozenset(candidate_stations),
        )
        candidate_cost = candidate_solution.costs(distances, problem.alpha).total

        is_tabu = iteration < tabu_until.get(point_to_add, -1)
        aspiration = candidate_cost < best_cost
        if is_tabu and not aspiration:
            continue

        if best_candidate is None or candidate_cost < best_candidate[3]:
            best_candidate = (
                station_to_remove,
                point_to_add,
                candidate_solution,
                candidate_cost,
            )

    return best_candidate


def _sample_unique_swaps(
    removable: list[int],
    non_stations: list[int],
    sample_size: int,
    random: Random,
) -> list[tuple[int, int]]:
    swaps: set[tuple[int, int]] = set()
    while len(swaps) < sample_size:
        swaps.add((random.choice(removable), random.choice(non_stations)))
    return list(swaps)
