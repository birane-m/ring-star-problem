"""Validation rules for Ring-Star solutions."""

from __future__ import annotations

from ring_star.instance import RingStarProblem
from ring_star.solution import RingStarSolution


class SolutionValidationError(ValueError):
    """Raised when a Ring-Star solution violates the problem constraints."""


def validate_solution(problem: RingStarProblem, solution: RingStarSolution) -> None:
    """Raise SolutionValidationError if the solution is infeasible."""

    n = problem.instance.n
    p = problem.p
    required_station = problem.required_station

    if len(solution.stations) != p:
        raise SolutionValidationError("The solution must contain exactly p stations.")

    if required_station not in solution.stations:
        raise SolutionValidationError("The required station is missing.")

    for station in solution.stations:
        if not 0 <= station < n:
            raise SolutionValidationError("A station index is outside the instance.")

    if len(solution.assignments) != n:
        raise SolutionValidationError("Each point must have exactly one assignment.")

    for point, station in enumerate(solution.assignments):
        if not 0 <= station < n:
            raise SolutionValidationError("An assignment points outside the instance.")
        if station not in solution.stations:
            raise SolutionValidationError("An assignment points to a non-station.")
        if point in solution.stations and station != point:
            raise SolutionValidationError("Each station must be assigned to itself.")

    if len(solution.cycle) != p:
        raise SolutionValidationError("The cycle must contain exactly p stations.")

    if len(set(solution.cycle)) != len(solution.cycle):
        raise SolutionValidationError("The cycle must be simple.")

    if set(solution.cycle) != set(solution.stations):
        raise SolutionValidationError("The cycle must contain exactly the stations.")
