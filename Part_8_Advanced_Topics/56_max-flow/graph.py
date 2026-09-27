"""Capacities plus residual graph."""
from collections.abc import Hashable


class FlowGraph:
    def __init__(self):
        self.capacity: dict[Hashable, dict[Hashable, float]] = {}

    def add_node(self, u: Hashable) -> None:
        self.capacity.setdefault(u, {})

    def add_edge(self, u: Hashable, v: Hashable, capacity: float) -> None:
        """Directed u->v. Parallel edges merge by summing capacity."""
        self.add_node(u)
        self.add_node(v)
        self.capacity[u][v] = self.capacity[u].get(v, 0) + capacity

    def nodes(self) -> list[Hashable]:
        return list(self.capacity)

    def residual(self) -> dict[Hashable, dict[Hashable, float]]:
        """Initial residual graph, reverse edges included."""
        raise NotImplementedError
