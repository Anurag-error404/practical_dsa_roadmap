import pytest

from algorithms.naive_dedupe import naive_dedupe
from algorithms.hash_dedupe import hash_dedupe
from bench import make_input, run
from plot import plot


def test_quadratic_algorithm_capped_at_large_sizes():
    # TODO: Input size large enough that the O(n²) version would take minutes — needs a timeout
    #       or size cap for that algorithm only
    ...


def test_timing_reports_median_of_multiple_trials():
    # TODO: Single-run timing noise (JIT/cache warm-up) — take multiple trials, report median
    ...


def test_empty_input_runs_without_error():
    # TODO: Empty input (size 0) — should still run without error
    ...


def test_unordered_input_sizes_handled():
    # TODO: Input sizes not in increasing order
    ...
