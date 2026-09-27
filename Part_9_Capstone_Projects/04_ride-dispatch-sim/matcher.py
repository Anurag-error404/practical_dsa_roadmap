"""Assignment logic (greedy nearest-available or bipartite matching)."""
from driver_pool import DriverPool
from models import Assignment, RideRequest, Unmatched
from road_network import RoadNetwork


def assign(requests: list[RideRequest], pool: DriverPool, network: RoadNetwork) -> tuple[list[Assignment], list[Unmatched]]:
    """Deterministic assignment; every unmatched request carries a reason."""
    raise NotImplementedError
