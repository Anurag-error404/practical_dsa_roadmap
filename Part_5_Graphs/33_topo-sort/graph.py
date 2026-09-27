"""Adjacency-list graph container. Storage only: traversal and algorithms live in the other modules."""
from collections.abc import Hashable, Iterable


class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj: dict[Hashable, list[tuple[Hashable, float]]] = {}
        self.edge_list: list[tuple[Hashable, Hashable, float]] = []

    def add_node(self, u: Hashable) -> None:
        self.adj.setdefault(u, [])

    def add_edge(self, u: Hashable, v: Hashable, weight: float = 1) -> None:
        """Store u->v (plus v->u if undirected). Parallel edges are kept; an undirected self-loop is stored once."""
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, weight))
        if not self.directed and u != v:
            self.adj[v].append((u, weight))
        self.edge_list.append((u, v, weight))

    def nodes(self) -> list[Hashable]:
        return list(self.adj)

    def neighbors(self, u: Hashable) -> list[tuple[Hashable, float]]:
        """(neighbor, weight) pairs. KeyError for a node that was never added."""
        return self.adj[u]

    def edges(self) -> list[tuple[Hashable, Hashable, float]]:
        """Every edge exactly as added (an undirected edge appears once)."""
        return list(self.edge_list)

    @classmethod
    def from_edges(cls, edges: Iterable[tuple], directed: bool = False, nodes: Iterable[Hashable] = ()) -> "Graph":
        """Build from (u, v) or (u, v, weight) tuples; `nodes` adds isolated nodes too."""
        g = cls(directed)
        for u in nodes:
            g.add_node(u)
        for e in edges:
            g.add_edge(*e)
        return g
