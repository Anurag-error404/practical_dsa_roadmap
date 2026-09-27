import pytest

from bloom_filter import BloomFilter


def test_false_positive_rate_measured():
    # TODO: False positives are expected and must be tested for, not treated as a bug
    ...


def test_no_false_negatives_ever():
    # TODO: False negatives must never occur — an item that was explicitly added must always
    #       return "might contain" true
    ...


def test_undersized_filter_tradeoff_documented():
    # TODO: Filter size/hash-count chosen too small for the expected item count — leads to
    #       unacceptably high false-positive rates; document the size/accuracy trade-off
    ...
