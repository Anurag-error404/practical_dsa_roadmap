"""Receives events and updates the underlying structure."""
from fenwick_tree import FenwickTree


class Ingestor:
    def __init__(self, start_time: float, bucket_seconds: float = 1.0, capacity: int = 86_400):
        """Events map to time buckets of `bucket_seconds`, starting at start_time."""
        raise NotImplementedError

    def bucket(self, timestamp: float) -> int:
        """Time bucket index for a timestamp."""
        raise NotImplementedError

    def ingest(self, timestamp: float, value: float) -> None:
        """Point-update the structure. Late (out-of-order) events: accept or reject, documented."""
        raise NotImplementedError
