"""Core structure: put/get/delete/resize."""
from typing import Any

from hash_functions import hash_key


class HashTable:
    def __init__(self, capacity: int = 8):
        """Initialize with given capacity. Resize when load factor exceeds ~0.7."""
        raise NotImplementedError

    def put(self, key, value: Any) -> None:
        """Insert or update. Must resolve collisions (chaining or open addressing)."""
        raise NotImplementedError

    def get(self, key) -> Any:
        """Return value for key, or raise/return sentinel if not found."""
        raise NotImplementedError

    def delete(self, key) -> None:
        """Remove key. Missing key: no-op or clear error, never a crash."""
        raise NotImplementedError

    @property
    def capacity(self) -> int:
        raise NotImplementedError

    @property
    def load_factor(self) -> float:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, key) -> bool:
        raise NotImplementedError
