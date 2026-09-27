"""Per-client deque of timestamps."""


class SlidingWindowLimiter:
    def __init__(self, limit: int, window_seconds: float = 60.0):
        """Allow at most `limit` requests per client in any rolling `window_seconds`."""
        raise NotImplementedError

    def allow(self, client_id: str, timestamp: float) -> bool:
        """Record the request if allowed. True = allow, False = deny."""
        raise NotImplementedError
