"""Exact mixed-integer model for the Ring-Star problem.

The formulation follows the project statement directly:

* choose exactly ``p`` metro stations, including the required station;
* assign every point to one chosen station;
* build one connected cycle through all chosen stations;
* minimize the weighted metro length plus the walking assignment length.

The cycle connectivity is enforced with a single-commodity flow rooted at the
required station.  This avoids disconnected subtours in the selected metro
edges.
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass

from ring_star.distances import build_distance_matrix
from ring_star.instance import RingStarProblem
from ring_star.solution import RingStarSolution
from ring_star.validation import validate_solution


class ExactSolverUnavailableError(ImportError):
    """Raised when the optional PuLP dependency is not installed."""


class ExactSolveError(RuntimeError):
    """Raised when the exact solver cannot return a feasible optimal solution."""


@dataclass(frozen=True)
class ExactSolveResult:
    """Summary returned by the exact PLNE solver."""

    solution: RingStarSolution
    objective_value: float
    status: str
    solver_name: str
    time_limit: int | None
    optimal: bool


def solve_exact_solution(
    problem: RingStarProblem,
    *,
    time_limit: int | None = None,
    solver_message: bool = False,
) -> ExactSolveResult:
    """Solve the Ring-Star problem exactly with a PLNE model.

    The implementation uses PuLP with CBC.  PuLP is kept optional so the rest of
    the project remains usable without an exact solver installed.
    """

    pulp = _import_pulp()
    distances = build_distance_matrix(problem.instance.points)
    model = pulp.LpProblem("ring_star", pulp.LpMinimize)
    n = problem.instance.n
    root = problem.required_station
    points = range(n)
    undirected_edges = [(i, j) for i in points for j in range(i + 1, n)]
    directed_edges = [(i, j) for i in points for j in points if i != j]

    station = model.add_variable_dicts("station", points, cat=pulp.LpBinary)
    assignment = model.add_variable_dicts(
        "assignment",
        (points, points),
        cat=pulp.LpBinary,
    )
    metro_edge = model.add_variable_dicts(
        "metro_edge",
        undirected_edges,
        cat=pulp.LpBinary,
    )
    flow = model.add_variable_dicts(
        "flow",
        directed_edges,
        lowBound=0,
        upBound=problem.p - 1,
        cat=pulp.LpContinuous,
    )

    model += (
        problem.alpha
        * pulp.lpSum(
            distances[i][j] * metro_edge[(i, j)] for i, j in undirected_edges
        )
        + pulp.lpSum(
            distances[i][j] * assignment[i][j] for i in points for j in points
        )
    )

    model += pulp.lpSum(station[i] for i in points) == problem.p
    model += station[root] == 1

    for i in points:
        model += pulp.lpSum(assignment[i][j] for j in points) == 1
        model += assignment[i][i] == station[i]

        incident_edges = [
            metro_edge[_edge_key(i, j)]
            for j in points
            if i != j
        ]
        model += pulp.lpSum(incident_edges) == 2 * station[i]

        for j in points:
            model += assignment[i][j] <= station[j]

    for i, j in undirected_edges:
        model += metro_edge[(i, j)] <= station[i]
        model += metro_edge[(i, j)] <= station[j]
        model += flow[(i, j)] + flow[(j, i)] <= (problem.p - 1) * metro_edge[(i, j)]

    for i in points:
        outgoing = pulp.lpSum(flow[(i, j)] for j in points if i != j)
        incoming = pulp.lpSum(flow[(j, i)] for j in points if i != j)
        if i == root:
            model += outgoing - incoming == problem.p - 1
        else:
            model += incoming - outgoing == station[i]

    solver, solver_name = _build_cbc_solver(pulp, time_limit, solver_message)
    model.solve(solver)
    raw_status = pulp.LpStatus[model.status]
    if raw_status != "Optimal":
        raise ExactSolveError(f"Exact solver did not return a feasible solution: {raw_status}.")

    selected_stations = frozenset(
        i for i in points if _variable_value(station[i]) >= 0.5
    )
    selected_edges = frozenset(
        edge for edge in undirected_edges if _variable_value(metro_edge[edge]) >= 0.5
    )
    cycle = _cycle_from_selected_edges(selected_stations, selected_edges, root)
    assignments = tuple(
        max(points, key=lambda j: _variable_value(assignment[i][j]))
        for i in points
    )
    solution = RingStarSolution(
        stations=selected_stations,
        cycle=cycle,
        assignments=assignments,
    )
    validate_solution(problem, solution)

    status = "Optimal" if time_limit is None else "feasible_time_limited"
    return ExactSolveResult(
        solution=solution,
        objective_value=float(pulp.value(model.objective)),
        status=status,
        solver_name=solver_name,
        time_limit=time_limit,
        optimal=time_limit is None,
    )


def _import_pulp():
    try:
        import pulp
    except ModuleNotFoundError as error:
        raise ExactSolverUnavailableError(
            "PuLP is required for the exact PLNE solver. "
            "Install project dependencies with: pip install -r requirements.txt"
        ) from error

    return pulp


def _build_cbc_solver(pulp, time_limit: int | None, solver_message: bool):
    for solver_name in ("COIN_CMD", "PULP_CBC_CMD"):
        solver_class = getattr(pulp, solver_name, None)
        if solver_class is None:
            continue

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            solver = solver_class(msg=solver_message, timeLimit=time_limit)
        try:
            is_available = bool(solver.available())
        except Exception:
            is_available = True

        if is_available:
            return solver, "CBC"

    raise ExactSolverUnavailableError(
        "No CBC solver is available for PuLP. "
        "Install a compatible solver, for example with: pip install 'pulp[cbc]'"
    )


def _edge_key(i: int, j: int) -> tuple[int, int]:
    return (i, j) if i < j else (j, i)


def _variable_value(variable) -> float:
    value = variable.value()
    if value is None:
        return 0.0
    return float(value)


def _cycle_from_selected_edges(
    stations: frozenset[int],
    edges: frozenset[tuple[int, int]],
    root: int,
) -> tuple[int, ...]:
    adjacency: dict[int, list[int]] = {station: [] for station in stations}
    for i, j in edges:
        adjacency[i].append(j)
        adjacency[j].append(i)

    for neighbors in adjacency.values():
        neighbors.sort()

    cycle = [root]
    previous: int | None = None
    current = root
    while len(cycle) < len(stations):
        next_station = next(
            (
                neighbor
                for neighbor in adjacency[current]
                if neighbor != previous and neighbor not in cycle
            ),
            None,
        )
        if next_station is None:
            raise ExactSolveError("Could not extract a valid metro cycle.")
        cycle.append(next_station)
        previous, current = current, next_station

    if root not in adjacency[current]:
        raise ExactSolveError("The selected metro edges do not close the cycle.")

    return tuple(cycle)
