"""Heap/spatial index of available drivers by proximity."""
from collections.abc import Iterable

from models import Driver, Node
from road_network import RoadNetwork


class DriverPool:
    def __init__(self, drivers: Iterable[Driver] = ()):
        self.drivers: dict[str, Driver] = {d.id: d for d in drivers}

    def set_online(self, driver_id: str, online: bool) -> None:
        raise NotImplementedError

    def nearest_available(self, network: RoadNetwork, location: Node, k: int = 1) -> list[Driver]:
        """Up to k online, non-busy drivers closest by travel time."""
        raise NotImplementedError
