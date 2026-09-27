import pytest

from graph_loader import load_edges
from bfs_path import shortest_path, degrees
from cli import format_result
from random_graphs import random_edges


def test_same_user_is_degree_zero():
    # TODO: The two users are the same person — degree 0
    ...


def test_disconnected_users_report_not_connected():
    # TODO: No path exists (they're in disconnected parts of the graph) — report "not connected"
    #       explicitly, don't error or loop forever
    ...


def test_bfs_efficient_on_large_graph():
    # TODO: A graph large enough that naive re-scans per query are too slow — BFS should be
    #       efficient, not O(V²)
    ...


def test_equal_length_paths_choice_is_deterministic():
    # TODO: Multiple shortest paths of equal length — only one needs to be returned, but the
    #       choice should be deterministic and reproducible
    ...
