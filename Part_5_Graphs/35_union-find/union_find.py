"""Path compression plus union by rank."""
from collections.abc import Hashable, Iterable


class UnionFind:
    def __init__(self, elements: Iterable[Hashable] = (), *, path_compression: bool = True, union_by_rank: bool = True):
        """The flags let tests and benchmarks compare with and without each optimization."""
        raise NotImplementedError

    def find(self, x: Hashable) -> Hashable:
        """Representative of x's set."""
        raise NotImplementedError

    def union(self, a: Hashable, b: Hashable) -> bool:
        """Merge the sets of a and b. Return True if they were separate."""
        raise NotImplementedError

    def connected(self, a: Hashable, b: Hashable) -> bool:
        raise NotImplementedError
