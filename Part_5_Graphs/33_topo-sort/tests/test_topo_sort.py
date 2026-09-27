import pytest

from graph import Graph
from kahns_algorithm import topo_sort_kahn
from dfs_based import topo_sort_dfs
from random_graphs import random_dag


def test_cycle_detected_and_reported():
    # TODO: A cycle present — must be detected and reported, not silently produce a wrong or
    #       partial ordering
    ...


def test_any_valid_order_has_every_edge_pointing_forward():
    # TODO: Multiple valid topological orders exist — any one is acceptable, but verify it by
    #       checking every edge points forward in the output order
    ...


def test_disconnected_components_all_nodes_appear():
    # TODO: Disconnected components within the same graph — every node must still appear in the
    #       final order
    ...


def test_isolated_node_appears():
    # TODO: A node with no edges at all (isolated)
    ...
