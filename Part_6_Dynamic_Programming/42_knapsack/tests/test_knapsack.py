import pytest

from knapsack_01 import knapsack_01
from knapsack_unbounded import knapsack_unbounded
from reconstruct_selection import reconstruct_01, reconstruct_unbounded
from random_cases import cases, random_items


def test_capacity_zero_gives_value_zero():
    # TODO: Capacity 0 — no items fit, value 0
    ...


def test_item_heavier_than_capacity_excluded():
    # TODO: A single item heavier than the entire capacity — must be excluded, not crash
    ...


def test_all_zero_weight_items_flagged():
    # TODO: All items with zero weight — value could be "unbounded" in a naive model; this
    #       degenerate case is worth flagging explicitly rather than silently mishandling
    ...


def test_empty_item_list():
    # TODO: Empty item list
    ...


def test_unbounded_respects_capacity_with_repeated_item():
    # TODO: Unbounded knapsack: verify the capacity constraint is respected even when the same
    #       high-value/low-weight item is theoretically selectable many times over
    ...
