import pytest

from kmp import failure_function, kmp_search
from rabin_karp import rabin_karp_search


def test_pattern_longer_than_text_returns_empty():
    # TODO: Pattern longer than the text — no matches possible, return empty, not an error
    ...


def test_overlapping_matches_all_found():
    # TODO: A pattern that overlaps itself in the text (e.g., `"aa"` in `"aaaa"`) — must find
    #       all overlapping matches, not skip past them
    ...


def test_empty_pattern_convention():
    # TODO: An empty pattern — decide the convention (matches everywhere, or explicitly
    #       rejected) and document it
    ...


def test_rabin_karp_spurious_hit_verified():
    # TODO: Rabin-Karp: a hash collision that isn't an actual character match (a "spurious hit")
    #       — must be verified with a direct character comparison before confirming, or the
    #       algorithm will report false positives
    ...
