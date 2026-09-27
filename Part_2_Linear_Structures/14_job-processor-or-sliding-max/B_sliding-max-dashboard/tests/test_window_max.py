import pytest

from sliding_window_max import SlidingWindowMax
from stream_simulator import generate_events


def test_partial_window_before_n_events():
    # TODO: Fewer than N events have arrived yet — the window is partial, not an error
    ...


def test_max_evicted_when_it_leaves_window():
    # TODO: A value that was the max leaves the window — it must be evicted from the internal
    #       deque even though it's still the largest value seen overall
    ...


def test_duplicate_max_values_evicted_correctly():
    # TODO: Duplicate max values in the window — the deque needs to handle ties correctly on
    #       eviction, not just distinct values
    ...
