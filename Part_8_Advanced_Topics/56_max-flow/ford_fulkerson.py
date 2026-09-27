"""BFS-based (Edmonds-Karp) for guaranteed termination."""
from collections.abc import Hashable

from graph import FlowGraph


def max_flow(graph: FlowGraph, source: Hashable, sink: Hashable) -> tuple[float, dict]:
    """(max flow value, final residual graph)."""
    raise NotImplementedError
