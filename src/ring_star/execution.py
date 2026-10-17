"""One execution path for the CLI, experiments and saved artifacts."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from time import perf_counter
from math import isfinite

from ring_star.distances import build_distance_matrix
from ring_star.exact import ExactSolveError, ExactSolverUnavailableError, solve_exact_solution
from ring_star.heuristics import build_greedy_solution
from ring_star.instance import RingStarProblem
from ring_star.metaheuristics import build_local_search_solution, build_tabu_search_solution
from ring_star.solution import RingStarSolution
from ring_star.validation import validate_solution

METHODS = ("greedy", "local_search", "tabu_search", "exact_plne")
METHOD_LABELS = {
    "greedy": "Construction par grille",
    "local_search": "Recherche locale",
    "tabu_search": "Recherche tabou",
    "exact_plne": "PLNE / CBC",
}


@dataclass(frozen=True)
class RunConfig:
    method: str = "tabu_search"
    seed: int = 0
    iterations: int | None = None
    tabu_tenure: int = 20
    candidates_per_iteration: int | None = None
    time_limit: float | None = None
    search_time_limit: float | None = None

    def __post_init__(self) -> None:
        if self.method not in METHODS:
            raise ValueError(f"Unknown method: {self.method}.")
        for name, minimum in (("seed", None), ("iterations", 0), ("tabu_tenure", 0), ("candidates_per_iteration", 1)):
            value = getattr(self, name)
            if value is None and name in {"iterations", "candidates_per_iteration"}:
                continue
            if type(value) is not int or (minimum is not None and value < minimum):
                raise ValueError(f"Invalid integer parameter: {name}.")
        for name in ("time_limit", "search_time_limit"):
            value = getattr(self, name)
            if value is not None and (isinstance(value, bool) or not isfinite(value) or value <= 0):
                raise ValueError(f"{name} must be finite and > 0, or None.")


@dataclass(frozen=True)
class RunResult:
    config: RunConfig
    solution: RingStarSolution | None
    status: str
    elapsed_seconds: float
    optimal: bool = False
    lower_bound: float | None = None
    relative_gap: float | None = None
    details: dict = field(default_factory=dict)
    history: tuple[dict, ...] = ()
    initial_solution: RingStarSolution | None = None
    solver_log: str = ""
    error: str | None = None


def execute(problem: RingStarProblem, config: RunConfig) -> RunResult:
    """Time optimization including distances and initial construction, excluding I/O."""
    start = perf_counter()
    distances = build_distance_matrix(problem.instance.points)
    if config.method == "greedy":
        solution = build_greedy_solution(problem, distances=distances)
        value = solution.costs(distances, problem.alpha).total
        return RunResult(config, solution, "ok", perf_counter() - start,
                         history=({"iteration": 0, "evaluations": 0, "elapsed_seconds": 0.0,
                                   "current_cost": value, "best_cost": value},))
    if config.method in {"local_search", "tabu_search"}:
        arguments = dict(iterations=config.iterations, seed=config.seed,
                         distances=distances, time_limit=config.search_time_limit)
        if config.method == "local_search":
            result = build_local_search_solution(problem, **arguments)
            counters = {"accepted_moves": result.accepted_moves}
        else:
            result = build_tabu_search_solution(
                problem, tabu_tenure=config.tabu_tenure,
                candidates_per_iteration=config.candidates_per_iteration, **arguments,
            )
            counters = {"performed_moves": result.performed_moves,
                        "tabu_tenure": result.tabu_tenure,
                        "candidates_per_iteration": result.candidates_per_iteration}
        validate_solution(problem, result.best_solution)
        return RunResult(
            config, result.best_solution, "ok", perf_counter() - start,
            details={**counters, "iterations": result.iterations,
                     "iteration_budget": result.iteration_budget,
                     "evaluated_moves": result.evaluated_moves, "stop_reason": result.stop_reason,
                     "initial_cost": result.initial_cost, "best_cost": result.best_cost},
            history=tuple(asdict(step) for step in result.history),
            initial_solution=result.initial_solution,
        )
    try:
        exact = solve_exact_solution(problem, time_limit=config.time_limit, distances=distances)
    except ExactSolverUnavailableError as error:
        return RunResult(config, None, "solver_unavailable", perf_counter() - start, error=str(error))
    except ExactSolveError as error:
        return RunResult(config, None, error.status, perf_counter() - start,
                         solver_log=error.solver_log, error=str(error))
    return RunResult(
        config, exact.solution, "optimal" if exact.optimal else exact.status,
        perf_counter() - start, exact.optimal, exact.lower_bound, exact.relative_gap,
        details={"solver": exact.solver_name}, solver_log=exact.solver_log,
    )
