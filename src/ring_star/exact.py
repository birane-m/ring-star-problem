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
import re
import tempfile
from pathlib import Path
from math import isfinite
from dataclasses import dataclass

from ring_star.distances import DistanceMatrix, build_distance_matrix
from ring_star.instance import RingStarProblem
from ring_star.solution import RingStarSolution
from ring_star.validation import validate_solution


class ExactSolverUnavailableError(ImportError):
    """Raised when the optional PuLP dependency is not installed."""


class ExactSolveError(RuntimeError):
    """Raised when no integer feasible solution is available."""

    def __init__(self, message: str, *, status: str = "error", solver_log: str = ""):
        super().__init__(message)
        self.status = status
        self.solver_log = solver_log


@dataclass(frozen=True)
class ExactSolveResult:
    """Summary returned by the exact PLNE solver."""

    solution: RingStarSolution
    objective_value: float
    status: str
    solver_name: str
    time_limit: float | None
    optimal: bool
    lower_bound: float | None = None
    relative_gap: float | None = None
    solver_log: str = ""


def solve_exact_solution(
    problem: RingStarProblem,
    *,
    time_limit: float | None = None,
    solver_message: bool = False,
    distances: DistanceMatrix | None = None,
) -> ExactSolveResult:
    """Solve the Ring-Star problem exactly with a PLNE model.

    The implementation uses PuLP with CBC.  PuLP is kept optional so the rest of
    the project remains usable without an exact solver installed.
    """

    if time_limit is not None and (isinstance(time_limit, bool) or not isfinite(time_limit) or time_limit <= 0):
        raise ValueError("Exact time limit must be finite and strictly positive, or None.")
    pulp = _import_pulp()
    if distances is None:
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

    with tempfile.TemporaryDirectory(prefix="ring-star-cbc-") as directory:
        log_path = Path(directory) / "cbc.log"
        solver, solver_name = _build_cbc_solver(pulp, time_limit, False, log_path)
        try:
            model.solve(solver)
        except pulp.PulpSolverError as error:
            log = log_path.read_text(errors="replace") if log_path.exists() else ""
            raise ExactSolveError(str(error), solver_log=log) from error
        log = log_path.read_text(errors="replace") if log_path.exists() else ""
    if solver_message:
        print(log)
    optimal = model.status == pulp.LpStatusOptimal and model.sol_status == pulp.LpSolutionOptimal
    integer_feasible = model.sol_status in (pulp.LpSolutionOptimal, pulp.LpSolutionIntegerFeasible)
    if not integer_feasible:
        status = "no_solution_time_limit" if model.status == pulp.LpStatusNotSolved and time_limit is not None else "no_solution"
        raise ExactSolveError(
            f"No integer feasible solution: {pulp.LpStatus[model.status]}.",
            status=status, solver_log=log,
        )
    binaries = [*station.values(), *metro_edge.values(), *(assignment[i][j] for i in points for j in points)]
    if any(v.value() is None or abs(float(v.value()) - round(float(v.value()))) > 1e-5 for v in binaries):
        raise ExactSolveError("Solver returned a fractional incumbent.", solver_log=log)

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

    objective = solution.costs(distances, problem.alpha).total
    lower_bound = objective if optimal else _read_lower_bound(log)
    if lower_bound is not None and lower_bound > objective + 1e-4:
        lower_bound = None  # Never export an inconsistent bound from a solver log.
    gap = None if lower_bound is None else max(0.0, objective - lower_bound) / max(abs(objective), 1e-12)
    return ExactSolveResult(
        solution=solution, objective_value=objective,
        status="Optimal" if optimal else "feasible_time_limited" if time_limit is not None else "feasible",
        solver_name=solver_name, time_limit=time_limit, optimal=optimal,
        lower_bound=lower_bound, relative_gap=gap, solver_log=log,
    )


def _read_lower_bound(log: str) -> float | None:
    # CBC prints this summary on a time-limited run. Do not infer a bound from
    # the LP relaxation alone or from the best known heuristic solution.
    matches = re.findall(r"Lower bound:\s*([-+0-9.eE]+)", log)
    if not matches:
        return None
    try:
        value = float(matches[-1])
        return value if isfinite(value) else None
    except ValueError:
        return None


def _import_pulp():
    try:
        import pulp
    except ModuleNotFoundError as error:
        raise ExactSolverUnavailableError(
            "PuLP is required for the exact PLNE solver. "
            "Install project dependencies with: pip install -r requirements.txt"
        ) from error

    return pulp


def _build_cbc_solver(pulp, time_limit: float | None, solver_message: bool, log_path: Path | None = None):
    for solver_name in ("COIN_CMD", "PULP_CBC_CMD"):
        solver_class = getattr(pulp, solver_name, None)
        if solver_class is None:
            continue

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            solver = solver_class(msg=solver_message, timeLimit=time_limit, logPath=str(log_path) if log_path else None, threads=0, options=["randomSeed 1"])
        try:
            is_available = bool(solver.available())
        except (OSError, pulp.PulpSolverError):
            is_available = False

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
