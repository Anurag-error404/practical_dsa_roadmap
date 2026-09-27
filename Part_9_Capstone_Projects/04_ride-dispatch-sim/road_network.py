"""Graph representation of the city. Storage only."""
from models import Node


class RoadNetwork:
    def __init__(self):
        self.adj: dict[Node, list[tuple[Node, float]]] = {}

    def add_intersection(self, u: Node) -> None:
        self.adj.setdefault(u, [])

    def add_road(self, u: Node, v: Node, minutes: float, one_way: bool = False) -> None:
        self.add_intersection(u)
        self.add_intersection(v)
        self.adj[u].append((v, minutes))
        if not one_way:
            self.adj[v].append((u, minutes))

    def neighbors(self, u: Node) -> list[tuple[Node, float]]:
        return self.adj[u]
