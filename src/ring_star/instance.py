"""Problem and instance definitions for Ring-Star."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

Point = tuple[float, float]


def _normalize_points(points: Iterable[Point]) -> tuple[Point, ...]:
    normalized = tuple((float(x), float(y)) for x, y in points)
    if not normalized:
        raise ValueError("An instance must contain at least one point.")
    return normalized


@dataclass(frozen=True)
class RingStarInstance:
    """Geometric data of a Ring-Star instance."""

    name: str
    points: tuple[Point, ...]
    required_station: int = 0
    edge_weight_type: str | None = None

    def __post_init__(self) -> None:
        points = _normalize_points(self.points)
        object.__setattr__(self, "points", points)

        if not self.name:
            raise ValueError("Instance name cannot be empty.")
        if not 0 <= self.required_station < len(points):
            raise ValueError("Required station index is outside the instance.")

    @property
    def n(self) -> int:
        return len(self.points)


@dataclass(frozen=True)
class RingStarProblem:
    """A Ring-Star instance with optimization parameters."""

    instance: RingStarInstance
    p: int
    alpha: float = 1.0

    def __post_init__(self) -> None:
        if not 3 <= self.p <= self.instance.n:
            raise ValueError("Parameter p must satisfy 3 <= p <= n.")
        if not 0 <= self.alpha <= 10:
            raise ValueError("Parameter alpha must satisfy 0 <= alpha <= 10.")

    @property
    def required_station(self) -> int:
        return self.instance.required_station
