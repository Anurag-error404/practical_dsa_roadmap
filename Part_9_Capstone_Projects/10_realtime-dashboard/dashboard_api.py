from event_ingest import EventIngest
from fenwick_tree import FenwickTree
from models import Event
from sliding_window import RollingWindow
from trending_heap import Trending


class Dashboard:
    def __init__(self, window_seconds: float = 60.0, horizon_buckets: int = 86_400):
        self.ingest = EventIngest(RollingWindow(window_seconds), FenwickTree(horizon_buckets), Trending())

    def push(self, event: Event) -> None:
        self.ingest.ingest(event)

    def rolling_metric(self, now: float) -> dict[str, float | None]:
        raise NotImplementedError

    def range_query(self, start: float, end: float) -> float:
        raise NotImplementedError

    def top_k_trending(self, k: int) -> list[tuple[str, float]]:
        raise NotImplementedError
