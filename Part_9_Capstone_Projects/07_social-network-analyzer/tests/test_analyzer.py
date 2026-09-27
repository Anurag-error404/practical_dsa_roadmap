import pytest

from models import FriendGraph
from graph_loader import load_graph
from bfs_degrees import degrees_of_separation
from union_find import UnionFind, friend_groups
from heap_topk import most_connected


def test_isolated_user_is_own_group():
    # TODO: A user with zero friends — an isolated node, which is technically its own friend
    #       group of size 1
    ...


def test_single_giant_component():
    # TODO: The entire graph being one single connected component — only one friend group exists
    #       at all
    ...


def test_ties_at_kth_position_policy():
    # TODO: Ties in "most connected" right at the k-th position — decide whether to include all
    #       ties or strictly cap at k
    ...


def test_repeated_bfs_performance_on_large_graph():
    # TODO: A graph large enough that repeated from-scratch BFS on every query is noticeably
    #       slow — decide whether that's acceptable or whether some precomputation is warranted
    ...
