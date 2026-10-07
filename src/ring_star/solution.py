"""Solution representation and cost computation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from ring_star.distances import DistanceMatrix


@dataclass(frozen=True)
class SolutionCosts:
    """Detailed cost components of a Ring-Star solution."""

    metro: float
    walking: float
    total: float


@dataclass(frozen=True)
class RingStarSolution:
    """Stations, cycle and assignments of a Ring-Star solution."""

    stations: frozenset[int]
    cycle: tuple[int, ...]
    assignments: tuple[int, ...]

    def __init__(
        self,
        stations: Iterable[int],
        cycle: Iterable[int],
        assignments: Iterable[int],
    ) -> None:
        object.__setattr__(self, "stations", frozenset(stations))
        object.__setattr__(self, "cycle", tuple(cycle))
        object.__setattr__(self, "assignments", tuple(assignments))

    def metro_cost(self, distances: DistanceMatrix) -> float:
        """Return the length of the closed cycle over selected stations."""

        if len(self.cycle) <= 1:
            return 0.0

        total = 0.0
        for station_a, station_b in zip(self.cycle, self.cycle[1:]):
            total += distances[station_a][station_b]
        total += distances[self.cycle[-1]][self.cycle[0]]
        return total

    def walking_cost(self, distances: DistanceMatrix) -> float:
        """Return the sum of distances from non-stations to assigned stations."""

        return sum(
            distances[point][station]
            for point, station in enumerate(self.assignments)
            if point not in self.stations
        )

    def costs(self, distances: DistanceMatrix, alpha: float) -> SolutionCosts:
        """Return the weighted objective and its two components."""

        metro = self.metro_cost(distances)
        walking = self.walking_cost(distances)
        return SolutionCosts(
            metro=metro,
            walking=walking,
            total=alpha * metro + walking,
        )
