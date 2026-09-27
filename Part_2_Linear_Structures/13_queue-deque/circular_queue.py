from typing import Any


class CircularQueue:
    """Fixed-size array with wrapping front/rear indices."""

    def __init__(self, capacity: int):
        raise NotImplementedError

    def enqueue(self, value: Any) -> None:
        """Add at rear. When full: reject or overwrite oldest, your documented policy."""
        raise NotImplementedError

    def dequeue(self) -> Any:
        """Remove from front (FIFO)."""
        raise NotImplementedError

    def peek(self) -> Any:
        raise NotImplementedError

    def is_full(self) -> bool:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
