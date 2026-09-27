"""All-pairs."""
from collections.abc import Hashable

from graph import Graph


def floyd_warshall(graph: Graph) -> dict[Hashable, dict[Hashable, float]]:
    """dist[u][v] for every pair (unreachable = inf)."""
    raise NotImplementedError
