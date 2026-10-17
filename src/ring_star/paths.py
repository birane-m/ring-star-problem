"""Legacy path helpers retained for existing integrations; new runs use unique folders."""
from pathlib import Path

def default_point_cloud_output_path(instance_path: str | Path) -> Path:
    """Return the default PNG path for an instance point cloud."""

    return Path("outputs") / "figures" / "instances" / f"{Path(instance_path).stem}.png"


def default_greedy_solution_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default PNG path for a greedy solution plot."""

    return (
        Path("outputs")
        / "figures"
        / "heuristics"
        / f"{Path(instance_path).stem}_greedy_p{p}.png"
    )


def default_greedy_result_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default JSON path for a greedy solution result."""

    return (
        Path("outputs")
        / "results"
        / "heuristics"
        / f"{Path(instance_path).stem}_greedy_p{p}.json"
    )


def default_greedy_result_markdown_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default Markdown path for a greedy solution result."""

    return default_greedy_result_output_path(instance_path, p).with_suffix(".md")


def default_local_search_solution_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default PNG path for a local search solution plot."""

    return (
        Path("outputs")
        / "figures"
        / "metaheuristics"
        / f"{Path(instance_path).stem}_local_search_p{p}.png"
    )


def default_local_search_result_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default JSON path for a local search result."""

    return (
        Path("outputs")
        / "results"
        / "metaheuristics"
        / f"{Path(instance_path).stem}_local_search_p{p}.json"
    )


def default_tabu_solution_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default PNG path for a tabu search solution plot."""

    return (
        Path("outputs")
        / "figures"
        / "metaheuristics"
        / f"{Path(instance_path).stem}_tabu_p{p}.png"
    )


def default_tabu_result_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default JSON path for a tabu search result."""

    return (
        Path("outputs")
        / "results"
        / "metaheuristics"
        / f"{Path(instance_path).stem}_tabu_p{p}.json"
    )


def default_exact_solution_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default PNG path for an exact PLNE solution plot."""

    return (
        Path("outputs")
        / "figures"
        / "exact"
        / f"{Path(instance_path).stem}_exact_p{p}.png"
    )


def default_exact_result_output_path(instance_path: str | Path, p: int) -> Path:
    """Return the default JSON path for an exact PLNE result."""

    return (
        Path("outputs")
        / "results"
        / "exact"
        / f"{Path(instance_path).stem}_exact_p{p}.json"
    )


def default_benchmark_output_path() -> Path:
    """Return the default CSV path for benchmark results."""

    return Path("outputs") / "results" / "benchmarks" / "robustness.csv"


def default_comparison_output_path() -> Path:
    """Return the default CSV path for benchmark comparisons."""

    return Path("outputs") / "results" / "benchmarks" / "comparaison_methodes.csv"


def default_comparison_figures_directory() -> Path:
    """Return the default directory for benchmark comparison PNG figures."""

    return Path("outputs") / "figures" / "benchmarks"


def default_benchmark_solution_figures_directory() -> Path:
    """Return the default directory for benchmark solution PNG figures."""

    return Path("outputs") / "figures" / "benchmark_solutions"
