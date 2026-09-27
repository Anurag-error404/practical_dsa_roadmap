"""Receives events and routes them to the relevant structures."""
from fenwick_tree import FenwickTree
from models import Event
from sliding_window import RollingWindow
from trending_heap import Trending


class EventIngest:
    def __init__(self, window: RollingWindow, totals: FenwickTree, trending: Trending):
        self.window = window
        self.totals = totals
        self.trending = trending

    def ingest(self, event: Event) -> None:
        """Update every structure consistently (late-event policy applies to all of them)."""
        raise NotImplementedError
