import pytest

from tree_builder import FSNode, build_tree, build_synthetic
from search import search
from tree_debug import print_tree


def test_symlink_cycle_does_not_loop_forever():
    # TODO: Symbolic links that point back up the tree, creating a cycle — this breaks the "it's
    #       a tree" assumption; must detect and avoid infinite traversal
    ...


def test_permission_denied_folder_skipped():
    # TODO: Permission-denied folders encountered mid-traversal — skip and continue, don't crash
    #       the whole search
    ...


def test_case_sensitivity_policy():
    # TODO: Case-sensitive vs. case-insensitive search (platform-dependent — decide and
    #       document)
    ...


def test_empty_folders():
    # TODO: Empty folders
    ...


def test_term_matches_both_file_and_folder():
    # TODO: A search term matching both a file name and a folder name
    ...
