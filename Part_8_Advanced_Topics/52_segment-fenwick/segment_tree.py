"""Range query plus point update."""
import operator
from collections.abc import Callable


class SegmentTree:
    def __init__(self, values: list[int], combine: Callable[[int, int], int] = operator.add, identity: int = 0):
        """combine/identity select the aggregate: (add, 0) = sum, (min, inf) = min, (max, -inf) = max."""
        raise NotImplementedError

    def query(self, left: int, right: int) -> int:
        """Aggregate over values[left..right] inclusive, in O(log n)."""
        raise NotImplementedError

    def update(self, index: int, value: int) -> None:
        """Set values[index] = value (set, not add), in O(log n)."""
        raise NotImplementedError
