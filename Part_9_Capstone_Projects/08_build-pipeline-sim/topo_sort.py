"""Validates the DAG and detects cycles."""
from models import BuildTask


def find_cycle(tasks: dict[str, BuildTask]) -> list[str] | None:
    """Task names forming a cycle, or None."""
    raise NotImplementedError


def topo_order(tasks: dict[str, BuildTask]) -> list[str]:
    raise NotImplementedError
