import pytest

from dictionary import load_dictionary
from edit_distance import edit_distance
from suggester import suggest


def test_correct_word_returns_itself_first():
    # TODO: The input word is already correctly spelled — should still return sensibly (e.g.,
    #       itself as the top match)
    ...


def test_large_dictionary_limitation_noted():
    # TODO: A large dictionary making per-query full edit-distance comparison against every
    #       entry too slow — note this as a known limitation, or note a prefix/BK-tree structure
    #       as a future optimization
    ...


def test_ties_at_same_distance_return_several():
    # TODO: Multiple dictionary words tied at the same edit distance — return several,
    #       optionally ranked by frequency
    ...
