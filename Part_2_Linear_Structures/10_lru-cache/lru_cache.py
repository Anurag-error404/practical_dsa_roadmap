"""Doubly linked list + hash map combo."""
from typing import Any


class _Node:
    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.prev: "_Node | None" = None
        self.next: "_Node | None" = None


class LRUCache:
    def __init__(self, capacity: int):
        raise NotImplementedError

    def get(self, key: Any) -> Any:
        """Value for key (and mark it most recent), or a clear miss."""
        raise NotImplementedError

    def put(self, key: Any, value: Any) -> None:
        """Insert/update and mark most recent. Over capacity: evict the least recently used."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
