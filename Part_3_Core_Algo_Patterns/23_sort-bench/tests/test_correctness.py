import pytest

from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort
from algorithms.counting_sort import counting_sort
from bench import make_input, run


def test_sorted_input_with_naive_pivot_worst_case():
    # TODO: Already-sorted input fed to a naive quicksort with a poor (e.g., first-element)
    #       pivot choice — this is the classic worst-case that degrades to O(n²) and can even
    #       stack-overflow a recursive implementation
    ...


def test_all_identical_elements():
    # TODO: An array where every element is identical
    ...


def test_counting_sort_requires_bounded_range():
    # TODO: Counting sort given a huge value range relative to array size — memory blows up;
    #       document that counting sort needs a bounded range to be viable
    ...


def test_empty_and_single_element_arrays():
    # TODO: Empty array, and array of size 1
    ...
