"""insert/delete/search."""
from typing import Any


class TreeNode:
    def __init__(self, value: Any):
        self.value = value
        self.left: "TreeNode | None" = None
        self.right: "TreeNode | None" = None


class BST:
    def __init__(self):
        self.root: TreeNode | None = None

    def insert(self, value: Any) -> None:
        """Insert value. Duplicate policy (reject / right child / count) is yours; be consistent."""
        raise NotImplementedError

    def delete(self, value: Any) -> None:
        """Remove value; the tree must still be a valid BST (0, 1, and 2-children cases)."""
        raise NotImplementedError

    def search(self, value: Any) -> bool:
        raise NotImplementedError
