"""Range query endpoint."""
from ingest import Ingestor


class QueryAPI:
    def __init__(self, ingestor: Ingestor):
        self.ingestor = ingestor

    def range_sum(self, t0: float, t1: float) -> float:
        """Sum of values in [t0, t1]. No events there: 0."""
        raise NotImplementedError

    def range_min(self, t0: float, t1: float) -> float | None:
        """Min in [t0, t1]; empty range is an explicit null/error. (Fenwick can't do min alone.)"""
        raise NotImplementedError

    def range_max(self, t0: float, t1: float) -> float | None:
        raise NotImplementedError
