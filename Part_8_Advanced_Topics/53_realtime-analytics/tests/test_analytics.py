import pytest

from ingest import Ingestor
from fenwick_tree import FenwickTree
from query_api import QueryAPI


def test_empty_range_returns_default():
    # TODO: A query range containing no events — return a sensible default (0 for sum; explicit
    #       null/error for min/max of an empty set), not a crash
    ...


def test_out_of_order_event_policy():
    # TODO: Events arriving out of chronological order — decide whether to accept and re-index,
    #       or reject late data
    ...


def test_high_throughput_point_updates_no_rebuild():
    # TODO: High event throughput requiring efficient point updates without full structure
    #       rebuilds
    ...


def test_future_range_returns_available_data():
    # TODO: A query range extending into the future (no data there yet) — return what's
    #       available, not an error
    ...
