import pytest

import naive_recursive
import memoized
import tabulated
import bench
from random_cases import cases, random_coins


def test_base_cases_n_zero_and_one():
    # TODO: n = 0 or n = 1 — base cases that are easy to get subtly wrong
    ...


def test_negative_n_rejected():
    # TODO: Negative n — invalid input, should be rejected explicitly
    ...


def test_coin_change_impossible_returns_minus_one():
    # TODO: Coin change where no valid combination reaches the target — return -1/"impossible,"
    #       don't crash
    ...


def test_naive_version_capped_for_large_n():
    # TODO: n large enough that naive recursion would hang for minutes — cap or timeout the
    #       naive version specifically when benchmarking
    ...


def test_duplicate_denominations():
    # TODO: Duplicate denominations in the coin list
    ...
