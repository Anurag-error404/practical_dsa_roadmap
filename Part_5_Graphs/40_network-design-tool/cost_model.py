"""Computes or loads edge costs."""
from pathlib import Path

from city_loader import City

Edge = tuple[str, str, float]


def load_costs(path: str | Path) -> list[Edge]:
    """Candidate connections (city_a, city_b, cost) from a file."""
    raise NotImplementedError


def candidate_edges(cities: list[City], k: int | None = None) -> list[Edge]:
    """Candidate connections computed from coordinates. k limits each city to its k nearest."""
    raise NotImplementedError
