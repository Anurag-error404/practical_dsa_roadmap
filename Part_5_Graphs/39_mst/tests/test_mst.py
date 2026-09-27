import pytest

from graph import Graph
from prims import prim_mst
from kruskals import kruskal_mst
from random_graphs import random_connected


def test_disconnected_graph_forest_or_error():
    # TODO: A disconnected graph — no single spanning tree exists; detect this and either return
    #       a minimum spanning forest or an explicit error, rather than a partial/wrong tree
    ...


def test_duplicate_weights_total_cost_correct():
    # TODO: Duplicate-weight edges — multiple valid MSTs may exist with the same total cost; any
    #       one is acceptable, but total cost must be correct
    ...


def test_single_node_mst_empty_cost_zero():
    # TODO: A graph with only one node — trivial MST, no edges, cost 0
    ...


def test_prim_and_kruskal_agree_on_total_cost():
    # TODO: Prim's and Kruskal's must agree on total cost, even when they select different edges
    #       to get there
    ...
