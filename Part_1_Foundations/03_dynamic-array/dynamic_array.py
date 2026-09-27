from typing import Any


class DynamicArray:
    """Resizable array on a fixed-size backing block (e.g. `[None] * capacity`). No list growth."""

    def __init__(self, capacity: int = 1):
        """Start empty with the given backing capacity."""
        raise NotImplementedError

    @property
    def size(self) -> int:
        """Number of stored elements."""
        raise NotImplementedError

    @property
    def capacity(self) -> int:
        """Length of the backing block."""
        raise NotImplementedError

    def push(self, value: Any) -> None:
        """Append in amortized O(1). At size == capacity, resize (commonly x2) before the write."""
        raise NotImplementedError

    def get(self, index: int) -> Any:
        """Element at index. Out-of-bounds must raise a clear error, never read stale slots."""
        raise NotImplementedError

    def pop(self) -> Any:
        """Remove and return the last element. Whether/when capacity shrinks is your policy."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
