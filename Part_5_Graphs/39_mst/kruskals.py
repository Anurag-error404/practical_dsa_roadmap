"""Union-find based; sorts edges by weight."""
from graph import Graph

Edge = tuple


def kruskal_mst(graph: Graph) -> tuple[list[Edge], float]:
    """(MST edges, total cost). Same disconnected-graph convention as prim_mst."""
    raise NotImplementedError
