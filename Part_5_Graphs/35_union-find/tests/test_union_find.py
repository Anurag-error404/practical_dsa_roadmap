import pytest

from union_find import UnionFind
from random_graphs import random_edges


def test_union_with_itself():
    # TODO: `union(a, a)` — unioning an element with itself
    ...


def test_find_on_unknown_element_policy():
    # TODO: `find()` on an element never explicitly added — decide whether it auto-initializes
    #       or errors
    ...


def test_repeated_union_is_idempotent_rank_unchanged():
    # TODO: Calling `union()` on the same pair repeatedly — should be idempotent, without
    #       incorrectly inflating rank/size bookkeeping
    ...


def test_path_compression_preserves_rank():
    # TODO: Path compression must not corrupt the rank/size values used by union-by-rank
    ...


def test_long_chain_depth_reduced_by_compression():
    # TODO: A long chain built before path compression runs — a good stress test to confirm the
    #       optimization is actually reducing lookup depth, not just present in the code
    ...
