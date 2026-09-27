import pytest

from graph import Graph
from bfs import bfs
from dfs import dfs
from cycle_detection import has_cycle_directed, has_cycle_undirected
from connected_components import connected_components
from random_graphs import random_edges


def test_disconnected_graph_components_cover_all_nodes():
    # TODO: A disconnected graph — traversal from one node won't reach every node, so full
    #       connected-component detection needs to loop over all nodes, not just start once
    ...


def test_self_loops():
    # TODO: Self-loops (a node with an edge to itself)
    ...


def test_parallel_edges():
    # TODO: Parallel edges (multiple edges between the same pair of nodes)
    ...


def test_cycle_detection_directed_vs_undirected():
    # TODO: Cycle detection differs between directed and undirected graphs — these need
    #       genuinely separate logic, not one function reused for both
    ...


def test_empty_graph_and_single_isolated_node():
    # TODO: An empty graph, and a single node with no edges
    ...
