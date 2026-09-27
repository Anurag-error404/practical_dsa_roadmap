import pytest

from dynamic_array import DynamicArray
from bench_harness import measure


def test_get_out_of_bounds_raises_clear_error():
    # TODO: `get()` with an out-of-bounds index — should raise/return a clear error, not read
    #       garbage memory
    ...


def test_push_at_capacity_resizes_before_write():
    # TODO: `push()` exactly at current capacity — must trigger resize (commonly ×2) before the
    #       write, not after
    ...


def test_capacity_policy_after_many_removals():
    # TODO: Many pushes then many removals — decide whether to shrink capacity back down (and
    #       when)
    ...


def test_get_zero_on_empty_array_fails_cleanly():
    # TODO: Pushing zero elements, then calling `get(0)` — should fail cleanly
    ...
