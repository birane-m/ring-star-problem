"""Constructive heuristics for the Ring-Star problem.

The Ring-Star problem mixes two decisions:

* selecting p stations among all points, as in the p-median problem;
* ordering the selected stations in a cycle, as in the TSP.

This module implements a first deterministic constructive heuristic. It follows
the idea suggested in the subject: select geographically spread stations with a
grid, assign each point to its nearest station, then build a station cycle with
the nearest-neighbor TSP heuristic.
"""

from __future__ import annotations

from math import ceil, sqrt

from ring_star.distances import DistanceMatrix, build_distance_matrix
from ring_star.instance import Point
from ring_star.instance import RingStarProblem
from ring_star.solution import RingStarSolution
from ring_star.validation import validate_solution


def select_stations_farthest_first(
    problem: RingStarProblem,
    distances: DistanceMatrix,
) -> frozenset[int]:
    """Select p stations with a deterministic farthest-first rule.

    The required station is selected first. Each next station is the point whose
    distance to its closest selected station is maximal.

    This function is useful as a standalone baseline and as a repair step for
    the grid heuristic. If the grid creates fewer than p stations because some
    cells are empty, farthest-first adds the least-covered points first.
    """

    selected = {problem.required_station}
    candidates = set(range(problem.instance.n)) - selected

    while len(selected) < problem.p:
        next_station = max(
            candidates,
            key=lambda point: (
                min(distances[point][station] for station in selected),
                -point,
            ),
        )
        selected.add(next_station)
        candidates.remove(next_station)

    return frozenset(selected)


def select_stations_grid_then_complete(
    problem: RingStarProblem,
    distances: DistanceMatrix,
) -> frozenset[int]:
    """Select stations with the grid heuristic from the subject.

    A q x q grid is built with q = ceil(sqrt(p)). For each non-empty cell, the
    point closest to the cell center is selected. The result is then adjusted to
    contain exactly p stations.

    The adjustment makes the heuristic robust:

    * if the grid selects fewer than p stations, farthest-first completion adds
      points in poorly covered areas;
    * if the grid selects more than p stations, redundant stations are removed,
      while always preserving the required station.
    """

    selected = set(_grid_station_candidates(problem.instance.points, problem.p))
    selected.add(problem.required_station)
    selected = _complete_stations_farthest_first(problem, distances, selected)
    selected = _remove_redundant_stations(problem, distances, selected)
    return frozenset(selected)


def assign_to_nearest_station(
    stations: frozenset[int],
    distances: DistanceMatrix,
) -> tuple[int, ...]:
    """Assign every point to its nearest selected station.

    Stations are assigned to themselves. For non-station points, ties are broken
    by the smallest station index to keep the heuristic deterministic.
    """

    assignments: list[int] = []
    ordered_stations = sorted(stations)

    for point in range(len(distances)):
        if point in stations:
            assignments.append(point)
            continue

        nearest_station = min(
            ordered_stations,
            key=lambda station: (distances[point][station], station),
        )
        assignments.append(nearest_station)

    return tuple(assignments)


def nearest_neighbor_cycle(
    stations: frozenset[int],
    distances: DistanceMatrix,
    start: int,
) -> tuple[int, ...]:
    """Build a station cycle with the nearest-neighbor TSP heuristic.

    Starting from the required station, the algorithm repeatedly visits the
    nearest unvisited station. The returned tuple gives the visit order; the
    closing edge from the last station back to the first is implicit.
    """

    if start not in stations:
        raise ValueError("The cycle start must be one of the selected stations.")

    unvisited = set(stations)
    unvisited.remove(start)
    cycle = [start]
    current = start

    while unvisited:
        next_station = min(
            unvisited,
            key=lambda station: (distances[current][station], station),
        )
        cycle.append(next_station)
        unvisited.remove(next_station)
        current = next_station

    return tuple(cycle)


def build_greedy_solution(problem: RingStarProblem) -> RingStarSolution:
    """Build a valid Ring-Star solution with the constructive heuristic.

    Pipeline:

    1. compute the Euclidean distance matrix;
    2. select p stations with the grid-based heuristic;
    3. assign every point to its nearest station;
    4. build a nearest-neighbor cycle on selected stations;
    5. validate the resulting Ring-Star solution.
    """

    distances = build_distance_matrix(problem.instance.points)
    stations = select_stations_grid_then_complete(problem, distances)
    assignments = assign_to_nearest_station(stations, distances)
    cycle = nearest_neighbor_cycle(stations, distances, problem.required_station)
    solution = RingStarSolution(
        stations=stations,
        cycle=cycle,
        assignments=assignments,
    )

    validate_solution(problem, solution)
    return solution


def _grid_station_candidates(points: tuple[Point, ...], p: int) -> tuple[int, ...]:
    """Return station candidates produced by the q x q grid step.

    For each non-empty cell, the selected candidate is the point closest to the
    geometric center of the cell. Empty cells are skipped, which is why a repair
    step may be needed afterwards.
    """

    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    q = max(1, ceil(sqrt(p)))
    step_x = (max_x - min_x) / q if max_x > min_x else 1.0
    step_y = (max_y - min_y) / q if max_y > min_y else 1.0

    candidates: list[int] = []
    selected = set()

    # Iterate in a stable order so that repeated runs produce identical output.
    for cell_x in range(q):
        for cell_y in range(q):
            center = (
                min_x + (cell_x + 0.5) * step_x,
                min_y + (cell_y + 0.5) * step_y,
            )
            points_in_cell = [
                index
                for index, point in enumerate(points)
                if _point_is_in_cell(
                    point,
                    cell_x,
                    cell_y,
                    q,
                    min_x,
                    min_y,
                    step_x,
                    step_y,
                )
            ]

            if not points_in_cell:
                continue

            candidate = min(
                points_in_cell,
                key=lambda index: (_squared_distance(points[index], center), index),
            )
            if candidate not in selected:
                candidates.append(candidate)
                selected.add(candidate)

    return tuple(candidates)


def _point_is_in_cell(
    point: Point,
    cell_x: int,
    cell_y: int,
    q: int,
    min_x: float,
    min_y: float,
    step_x: float,
    step_y: float,
) -> bool:
    """Return True if a point belongs to a grid cell.

    The last row and column include their upper bound. This avoids losing points
    located exactly on the maximum x or y coordinate.
    """

    x, y = point
    lower_x = min_x + cell_x * step_x
    upper_x = min_x + (cell_x + 1) * step_x
    lower_y = min_y + cell_y * step_y
    upper_y = min_y + (cell_y + 1) * step_y

    inside_x = lower_x <= x <= upper_x if cell_x == q - 1 else lower_x <= x < upper_x
    inside_y = lower_y <= y <= upper_y if cell_y == q - 1 else lower_y <= y < upper_y
    return inside_x and inside_y


def _complete_stations_farthest_first(
    problem: RingStarProblem,
    distances: DistanceMatrix,
    selected: set[int],
) -> set[int]:
    """Add stations until exactly p are selected.

    Each added station is the candidate maximizing its distance to the closest
    already selected station. This prioritizes areas that are currently poorly
    covered by the station set.
    """

    candidates = set(range(problem.instance.n)) - selected

    while len(selected) < problem.p:
        next_station = max(
            candidates,
            key=lambda point: (
                min(distances[point][station] for station in selected),
                -point,
            ),
        )
        selected.add(next_station)
        candidates.remove(next_station)

    return selected


def _remove_redundant_stations(
    problem: RingStarProblem,
    distances: DistanceMatrix,
    selected: set[int],
) -> set[int]:
    """Remove stations until exactly p remain.

    A station is considered redundant when it is very close to another selected
    station. The required station is never removed.
    """

    while len(selected) > problem.p:
        removable = [station for station in selected if station != problem.required_station]
        station_to_remove = min(
            removable,
            key=lambda station: (
                min(
                    distances[station][other_station]
                    for other_station in selected
                    if other_station != station
                ),
                station,
            ),
        )
        selected.remove(station_to_remove)

    return selected


def _squared_distance(point_a: Point, point_b: Point) -> float:
    """Return a squared Euclidean distance for comparisons.

    The square root is unnecessary here because only relative distances are
    compared.
    """

    return (point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2
