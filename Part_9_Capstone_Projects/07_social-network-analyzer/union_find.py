"""Union-Find. Copy in your Project 35 implementation (or rewrite it)."""
from collections.abc import Hashable


class UnionFind:
    def __init__(self, elements=()):
        raise NotImplementedError

    def find(self, x: Hashable) -> Hashable:
        """Representative of x's set."""
        raise NotImplementedError

    def union(self, a: Hashable, b: Hashable) -> bool:
        """Merge the sets of a and b. Return True if they were separate."""
        raise NotImplementedError

    def connected(self, a: Hashable, b: Hashable) -> bool:
        raise NotImplementedError


def friend_groups(graph) -> list[set]:
    """Friend clusters; an isolated user is a group of one."""
    raise NotImplementedError
