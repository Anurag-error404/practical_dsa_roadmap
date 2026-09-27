import pytest

from bst import TreeNode, BST
from traversals import inorder, preorder, postorder
from balance_checker import height, is_balanced
from tree_debug import binary_children, print_tree


def test_delete_node_with_zero_one_and_two_children():
    # TODO: Deleting a node with 0, 1, or 2 children — the 2-children case (replace with in-
    #       order successor/predecessor) is where almost every BST bug lives
    ...


def test_delete_root():
    # TODO: Deleting the root node specifically
    ...


def test_duplicate_insert_policy():
    # TODO: Inserting a duplicate value — decide the policy (reject, insert as right child, or
    #       maintain a count) and be consistent
    ...


def test_search_empty_tree():
    # TODO: `search()` on an empty tree
    ...


def test_delete_missing_value():
    # TODO: Deleting a value that doesn't exist in the tree
    ...


def test_degenerate_tree_flagged_unbalanced():
    # TODO: A degenerate tree (all left or all right children only, effectively a linked list) —
    #       your balance checker should correctly flag this
    ...
