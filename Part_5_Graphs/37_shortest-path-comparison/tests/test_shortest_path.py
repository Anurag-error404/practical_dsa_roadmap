import pytest

from graph import Graph
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from floyd_warshall import floyd_warshall
from random_graphs import random_connected, random_edges


def test_dijkstra_negative_weights_rejected_or_documented():
    # TODO: Negative edge weights fed to Dijkstra — Dijkstra assumes non-negative weights and
    #       will silently give a wrong answer; either reject negative weights explicitly or
    #       document the limitation
    ...


def test_bellman_ford_reports_negative_cycle():
    # TODO: A negative cycle present — Bellman-Ford must detect and report this, not return a
    #       plausible-looking but wrong finite distance
    ...


def test_unreachable_nodes_are_infinite():
    # TODO: A disconnected graph — unreachable nodes should report infinity/unreachable, not
    #       error
    ...


def test_single_node_and_weighted_self_loop():
    # TODO: A graph with a single node; self-loops with a weight attached
    ...
