import pytest

from circular_queue import CircularQueue
from deque import Deque


def test_enqueue_on_full_queue_follows_policy():
    # TODO: `enqueue()` on a full circular queue — decide the policy (reject the write, or
    #       overwrite the oldest entry) and document it
    ...


def test_dequeue_on_empty_queue():
    # TODO: `dequeue()` on an empty queue
    ...


def test_front_rear_wraparound_past_array_end():
    # TODO: Wraparound index math — front/rear pointers crossing past the end of the underlying
    #       array back to index 0 is where most bugs live
    ...


def test_capacity_boundary_n_minus_1_vs_n_items():
    # TODO: Fixed-capacity vs. resizable circular queue — pick one and test exactly at the
    #       capacity boundary (n-1 items vs. n items)
    ...
