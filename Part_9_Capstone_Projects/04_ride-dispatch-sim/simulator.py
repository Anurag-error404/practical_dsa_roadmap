"""Drives the whole simulation over time."""
from driver_pool import DriverPool
from matcher import assign
from models import Assignment, Driver, RideRequest, Unmatched
from road_network import RoadNetwork


class DispatchSimulator:
    def __init__(self, network: RoadNetwork, drivers: list[Driver]):
        self.network = network
        self.pool = DriverPool(drivers)
        self.pending: list[RideRequest] = []

    def submit(self, request: RideRequest) -> None:
        raise NotImplementedError

    def step(self, now: float) -> tuple[list[Assignment], list[Unmatched]]:
        """Match pending requests at time `now`."""
        raise NotImplementedError

    def driver_offline(self, driver_id: str) -> None:
        """Exclude from future matching without disrupting an in-progress ride."""
        raise NotImplementedError
