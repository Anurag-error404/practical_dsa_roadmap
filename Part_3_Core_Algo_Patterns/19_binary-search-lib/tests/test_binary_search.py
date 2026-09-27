import pytest

from basic_search import binary_search
from first_last_occurrence import first_occurrence, last_occurrence
from rotated_search import search_rotated


def test_target_not_present():
    # TODO: Target not present in the array at all
    ...


def test_duplicates_first_and_last_differ():
    # TODO: Duplicates present — first-occurrence and last-occurrence must return different,
    #       correct indices
    ...


def test_empty_and_single_element_arrays():
    # TODO: Empty array, and array of size exactly 1
    ...


def test_rotation_point_zero_not_rotated():
    # TODO: Rotated array where the rotation point is 0 (i.e., not actually rotated) — must
    #       still work
    ...


def test_target_equals_pivot_in_rotated():
    # TODO: Target equal to the pivot element in a rotated search
    ...
