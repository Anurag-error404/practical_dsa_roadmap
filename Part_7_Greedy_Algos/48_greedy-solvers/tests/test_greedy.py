import pytest

from activity_selection import Activity, select_activities
from huffman_coding import HuffmanNode, huffman_codes
from fractional_knapsack import Item, fractional_knapsack


def test_identical_start_end_tie_break():
    # TODO: Activities with identical start/end times — need a consistent tie-break rule
    #       (typically: sort by end time, then start time)
    ...


def test_touching_activities_overlap_policy():
    # TODO: An activity ending exactly when another starts — decide whether this counts as
    #       overlapping (inclusive) or not (exclusive), and document it
    ...


def test_single_character_huffman():
    # TODO: A single distinct character for Huffman — same degenerate-tree issue as the
    #       compressor project; needs explicit handling
    ...


def test_equal_ratio_items_total_value_correct():
    # TODO: Fractional knapsack items with identical value-to-weight ratio — order doesn't
    #       matter, but total value must still be correct
    ...


def test_capacity_zero():
    # TODO: Capacity of 0
    ...
