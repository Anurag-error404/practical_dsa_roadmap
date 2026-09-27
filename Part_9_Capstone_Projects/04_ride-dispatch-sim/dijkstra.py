"""ETA/route computation."""
from models import Node
from road_network import RoadNetwork


def shortest_route(network: RoadNetwork, source: Node, target: Node) -> tuple[float, list[Node]] | None:
    """(minutes, route), or None if unreachable."""
    raise NotImplementedError


def travel_times(network: RoadNetwork, source: Node) -> dict[Node, float]:
    raise NotImplementedError
