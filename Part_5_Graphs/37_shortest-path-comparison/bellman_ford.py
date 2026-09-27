"""Includes negative-cycle detection."""
from collections.abc import Hashable

from graph import Graph


def bellman_ford(graph: Graph, source: Hashable) -> dict[Hashable, float]:
    """Shortest distance to every node (unreachable = inf). A negative cycle must be reported."""
    raise NotImplementedError
