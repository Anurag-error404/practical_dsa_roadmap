"""Height-based balance check."""
from bst import TreeNode


def height(root: TreeNode | None) -> int:
    """Height of the tree (decide and document: empty tree = 0 or -1)."""
    raise NotImplementedError


def is_balanced(root: TreeNode | None) -> bool:
    """True if every node's subtree heights differ by at most 1."""
    raise NotImplementedError
