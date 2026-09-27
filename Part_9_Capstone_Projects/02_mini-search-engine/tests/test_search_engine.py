import pytest

from models import Document, SearchResult
from indexer import tokenize, InvertedIndex
from trie import TrieNode, Trie
from matcher import find_phrase
from ranker import top_k
from query_api import SearchEngine


def test_term_in_zero_documents_returns_empty():
    # TODO: A query term appearing in zero documents — return empty, not an error
    ...


def test_phrase_plus_keyword_query_combination():
    # TODO: A query mixing an exact phrase with loose keywords — decide how these combine (must-
    #       match phrase + optional keyword boost, or something simpler)
    ...


def test_incremental_index_build():
    # TODO: A document set large enough that the inverted index must be built incrementally
    #       rather than all at once
    ...


def test_autocomplete_zero_matches_empty_list():
    # TODO: Autocomplete for a prefix with zero matches — empty list, not an error
    ...


def test_relevance_ties_stable_ranking():
    # TODO: Two documents tied on relevance score — needs a defined tie-break for stable ranking
    ...
