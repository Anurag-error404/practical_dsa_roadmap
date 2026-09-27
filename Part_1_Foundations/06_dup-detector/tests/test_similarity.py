import pytest

from ingest import load_documents, normalize
from similarity import shingles, similarity, find_similar_pairs, matching_passages
from report import format_report


def test_length_normalized_score_for_excerpt_vs_full():
    # TODO: Documents of very different lengths (a 200-word excerpt of a 5,000-word article) —
    #       length-normalize the score
    ...


def test_short_quotes_below_min_match_length_ignored():
    # TODO: Legitimate short quotes/citations triggering a false positive — consider a minimum
    #       match-length before counting
    ...


def test_very_short_documents_not_flagged():
    # TODO: Very short documents (a tweet-length text) giving inflated similarity by chance —
    #       set a minimum document length
    ...


def test_large_set_avoids_all_pairs_comparison():
    # TODO: Large document sets making all-pairs comparison O(n²) — use shingling + hashing
    #       (MinHash/LSH) to avoid full pairwise comparison
    ...
