import pytest

from trie import TrieNode, Trie
from tree_debug import print_tree


def test_delete_word_that_prefixes_another_keeps_shared_nodes():
    # TODO: Deleting a word that is itself a prefix of another stored word — must not remove the
    #       shared nodes the other word still needs
    ...


def test_insert_empty_string():
    # TODO: Inserting the empty string
    ...


def test_case_sensitivity_policy():
    # TODO: Case sensitivity (decide and document)
    ...


def test_internal_prefix_starts_with_true_search_false():
    # TODO: A prefix that exists as an internal path but was never inserted as a complete word —
    #       `starts_with()` should return true, `search()` should return false for it
    ...


def test_delete_word_never_inserted():
    # TODO: Deleting a word that was never inserted
    ...
