"""Heap-based."""
from collections.abc import Hashable

from graph import Graph


def dijkstra(graph: Graph, source: Hashable) -> dict[Hashable, float]:
    """Shortest distance to every node (unreachable = inf). Non-negative weights only."""
    raise NotImplementedError
