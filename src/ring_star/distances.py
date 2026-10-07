"""Distance helpers for Ring-Star instances."""

from __future__ import annotations

from math import hypot

from ring_star.instance import Point

DistanceMatrix = tuple[tuple[float, ...], ...]


def euclidean_distance(point_a: Point, point_b: Point) -> float:
    """Return the Euclidean distance between two planar points."""

    return hypot(point_a[0] - point_b[0], point_a[1] - point_b[1])


def build_distance_matrix(points: tuple[Point, ...]) -> DistanceMatrix:
    """Build the complete symmetric Euclidean distance matrix."""

    return tuple(
        tuple(euclidean_distance(point_i, point_j) for point_j in points)
        for point_i in points
    )
