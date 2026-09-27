import pytest

from indexer import load_documents, tokenize, InvertedIndex
from kmp_or_rabinkarp import find_all
from ranker import rank
from query_api import SearchResult, CatalogueSearch


def test_term_in_zero_documents_returns_empty():
    # TODO: Search term found in zero documents — return an empty result, not an error
    ...


def test_very_common_term_ranking_meaningful():
    # TODO: A very common term appearing in nearly every document — ranking still needs to mean
    #       something (e.g., frequency-based scoring, not just presence/absence)
    ...


def test_whole_word_vs_partial_match_policy():
    # TODO: Whole-word vs. partial-word matching (should `"cat"` match `"category"`?) — decide
    #       and document
    ...


def test_documents_added_after_index_built():
    # TODO: Documents added/updated after the initial index is built — decide whether
    #       incremental re-indexing is supported, or a full rebuild is required
    ...


def test_large_set_uses_inverted_index_not_scan():
    # TODO: A document set large enough that a linear scan per query is too slow — build an
    #       inverted index upfront rather than searching each document at query time
    ...
