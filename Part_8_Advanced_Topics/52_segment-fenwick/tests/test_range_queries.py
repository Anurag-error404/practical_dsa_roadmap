import pytest

from segment_tree import SegmentTree
from fenwick_tree import FenwickTree
from fixtures import load_fixture, random_array, random_ops, save_fixture


def test_invalid_range_or_out_of_bounds_rejected():
    # TODO: `l > r`, or out-of-bounds indices — should be validated and rejected
    ...


def test_single_element_range():
    # TODO: `l == r` (single-element range query)
    ...


def test_re_update_is_set_not_add():
    # TODO: Re-updating an index that was already updated before — behavior should be consistent
    #       (a "set," not accidentally an "add," unless explicitly built as an add-based Fenwick
    #       tree)
    ...


def test_full_array_range():
    # TODO: Querying the full array range (a boundary case for the tree's internal structure)
    ...


def test_empty_array():
    # TODO: An empty array (size 0) — handle explicitly or disallow, but don't crash silently
    ...
