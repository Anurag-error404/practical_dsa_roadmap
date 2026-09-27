"""insert/extract/peek/heapify on an array-backed binary heap."""
from typing import Any


class Heap:
    def __init__(self, max_heap: bool = False):
        """Min-heap by default; max_heap=True flips the ordering."""
        self.max_heap = max_heap
        self.data: list = []

    @classmethod
    def heapify(cls, items: list, max_heap: bool = False) -> "Heap":
        """Build a heap from an unsorted list in O(n) (sift-down from the last parent, not n inserts)."""
        raise NotImplementedError

    def insert(self, value: Any) -> None:
        raise NotImplementedError

    def extract(self) -> Any:
        """Remove and return the min (or max, for a max-heap)."""
        raise NotImplementedError

    def peek(self) -> Any:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
