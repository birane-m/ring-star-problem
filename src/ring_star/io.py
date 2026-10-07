"""Input helpers for Ring-Star instances."""

from __future__ import annotations

from pathlib import Path

from ring_star.instance import Point, RingStarInstance


class TsplibFormatError(ValueError):
    """Raised when a TSPLIB file cannot be parsed as a coordinate instance."""


def load_tsplib_instance(path: str | Path) -> RingStarInstance:
    """Load a TSPLIB coordinate instance.

    The project uses TSPLIB files as a source of points. Distances are computed
    separately from the coordinates by the Ring-Star model.
    """

    path = Path(path)
    lines = path.read_text(encoding="utf-8").splitlines()

    headers: dict[str, str] = {}
    coordinates: dict[int, Point] = {}
    in_coordinates = False

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        if line.upper() == "EOF":
            break

        if in_coordinates:
            node_id, point = _parse_coordinate_line(line)
            if node_id in coordinates:
                raise TsplibFormatError(f"Duplicate node id: {node_id}.")
            coordinates[node_id] = point
            continue

        if line.upper() == "NODE_COORD_SECTION":
            in_coordinates = True
            continue

        key, value = _parse_header_line(line)
        headers[key] = value

    if not in_coordinates:
        raise TsplibFormatError("Missing NODE_COORD_SECTION.")
    if not coordinates:
        raise TsplibFormatError("Missing node coordinates.")

    dimension = _parse_dimension(headers)
    if dimension is not None and len(coordinates) != dimension:
        raise TsplibFormatError(
            f"Expected {dimension} coordinates, found {len(coordinates)}."
        )

    points = tuple(point for _, point in sorted(coordinates.items()))
    name = headers.get("NAME") or path.stem
    edge_weight_type = headers.get("EDGE_WEIGHT_TYPE")

    return RingStarInstance(
        name=name,
        points=points,
        required_station=0,
        edge_weight_type=edge_weight_type,
    )


def _parse_header_line(line: str) -> tuple[str, str]:
    if ":" in line:
        key, value = line.split(":", 1)
    else:
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            raise TsplibFormatError(f"Invalid TSPLIB header line: {line!r}.")
        key, value = parts

    return key.strip().upper(), value.strip()


def _parse_coordinate_line(line: str) -> tuple[int, Point]:
    parts = line.split()
    if len(parts) < 3:
        raise TsplibFormatError(f"Invalid coordinate line: {line!r}.")

    try:
        node_id = int(parts[0])
        x = float(parts[1])
        y = float(parts[2])
    except ValueError as error:
        raise TsplibFormatError(f"Invalid coordinate line: {line!r}.") from error

    return node_id, (x, y)


def _parse_dimension(headers: dict[str, str]) -> int | None:
    value = headers.get("DIMENSION")
    if value is None:
        return None

    try:
        return int(value)
    except ValueError as error:
        raise TsplibFormatError(f"Invalid DIMENSION value: {value!r}.") from error
