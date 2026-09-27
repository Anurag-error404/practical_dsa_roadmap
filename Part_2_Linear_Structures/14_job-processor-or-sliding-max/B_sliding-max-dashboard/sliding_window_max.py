"""Monotonic deque."""


class SlidingWindowMax:
    def __init__(self, window: int):
        """Track the max over the last `window` events."""
        raise NotImplementedError

    def push(self, timestamp: float, value: float) -> None:
        raise NotImplementedError

    def current_max(self) -> float | None:
        """Max within the current (possibly partial) window."""
        raise NotImplementedError
