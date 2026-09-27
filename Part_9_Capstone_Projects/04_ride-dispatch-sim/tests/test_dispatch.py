import pytest

from models import Driver, RideRequest, Assignment, Unmatched
from road_network import RoadNetwork
from dijkstra import shortest_route, travel_times
from driver_pool import DriverPool
from matcher import assign
from simulator import DispatchSimulator


def test_no_driver_in_radius_reported_unmatched_with_reason():
    # TODO: No available driver within a reasonable radius — report as unmatched with a reason,
    #       don't silently drop the request
    ...


def test_competing_requests_resolved_deterministically():
    # TODO: Multiple requests competing for the same nearest driver — resolve deterministically
    #       (e.g., request-arrival order)
    ...


def test_driver_offline_mid_assignment_excluded_from_future():
    # TODO: A driver going offline mid-assignment — an in-progress ride shouldn't be disrupted,
    #       but future matching must exclude them immediately
    ...


def test_disconnected_region_reported_unreachable():
    # TODO: A rider and all drivers sitting in a disconnected region of the road network —
    #       report unreachable, don't hang trying to compute a nonexistent path
    ...
