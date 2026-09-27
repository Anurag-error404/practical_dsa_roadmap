import pytest

from subset_generator import subsets
from single_number import single_number
from bit_counter import count_bits
from bits import MASK32, MASK64, bit, fmt_bin


def test_empty_set_yields_only_empty_subset():
    # TODO: Empty input set — subset generation should still yield exactly one subset, the empty
    #       set
    ...


def test_large_ints_vs_fixed_bit_width():
    # TODO: Very large integers relative to fixed bit-width assumptions (matters especially in
    #       32-bit vs. 64-bit contexts)
    ...


def test_negative_numbers_twos_complement():
    # TODO: Negative numbers and two's-complement effects on bitwise operations
    ...


def test_single_number_precondition_violation_documented():
    # TODO: Single-number problem given input that violates its precondition (more than one
    #       number appears an odd number of times) — document this as an assumption rather than
    #       silently returning a wrong answer
    ...
