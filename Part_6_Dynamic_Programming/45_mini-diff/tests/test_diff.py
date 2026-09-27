import pytest

from line_splitter import split_lines, read_lines
from lcs_diff import diff
from report_formatter import format_diff
from random_cases import cases, random_lines


def test_identical_files_zero_changes():
    # TODO: Identical files — diff should show zero changes
    ...


def test_completely_different_files_all_changed():
    # TODO: Completely different files — every line shows as changed, not an error
    ...


def test_very_different_lengths():
    # TODO: Files of very different lengths
    ...


def test_repeated_lines_mapped_to_correct_occurrence():
    # TODO: A line appearing multiple times in both files — must correctly track which specific
    #       occurrence maps to which, not just match by content globally (a classic diff-
    #       algorithm subtlety)
    ...


def test_large_input_limitation_documented():
    # TODO: Files large enough that a naive O(n·m) LCS is too slow/memory-heavy — document this
    #       limitation explicitly rather than silently hanging on large inputs
    ...
