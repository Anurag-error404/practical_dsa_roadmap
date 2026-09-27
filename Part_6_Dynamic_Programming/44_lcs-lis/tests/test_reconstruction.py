import pytest

from lcs import lcs
from lis import lis
from random_cases import cases, random_ints, random_string_pair


def test_empty_inputs_give_empty_result():
    # TODO: One or both inputs empty — result is empty, length 0 (not `None`/an error)
    ...


def test_no_common_subsequence_explicit_empty():
    # TODO: No common subsequence at all between two strings — still returns an explicit empty
    #       result
    ...


def test_lis_strictly_decreasing_length_one():
    # TODO: LIS on a strictly decreasing array — longest increasing subsequence has length 1
    ...


def test_lis_duplicates_strict_vs_non_decreasing():
    # TODO: LIS with duplicate values — decide strictly-increasing vs. non-decreasing and be
    #       consistent, since this changes the answer
    ...


def test_reconstruction_is_valid_subsequence():
    # TODO: Multiple LCS/LIS of the same max length exist — only one is needed, but it must be
    #       programmatically verified as an actual valid subsequence of the input, not just a
    #       length match
    ...
