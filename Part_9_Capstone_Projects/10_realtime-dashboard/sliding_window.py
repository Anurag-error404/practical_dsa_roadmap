"""Rolling metrics (monotonic deque)."""
from models import Event


class RollingWindow:
    def __init__(self, window_seconds: float):
        raise NotImplementedError

    def add(self, event: Event) -> None:
        raise NotImplementedError

    def metrics(self, now: float) -> dict[str, float | None]:
        """e.g. {"count", "sum", "max"} over the last window_seconds."""
        raise NotImplementedError
