import pytest

from heap import Heap
from tree_debug import render_heap


def test_extract_on_empty_heap():
    # TODO: `extract()` on an empty heap
    ...


def test_single_element_heap():
    # TODO: Heap with exactly one element
    ...


def test_duplicate_values():
    # TODO: Inserting duplicate values
    ...


def test_sift_at_root_and_last_leaf_boundaries():
    # TODO: Sift-up/sift-down at the boundaries (root, last leaf) — index math here is the usual
    #       bug source
    ...


def test_heapify_is_linear_not_repeated_insert():
    # TODO: Building a heap from an existing unsorted array should be implemented as `heapify`
    #       in O(n), not as n individual `insert()` calls (which would be O(n log n))
    ...
