"""Top-K trending via heap plus hash map."""


class Trending:
    def __init__(self):
        raise NotImplementedError

    def record(self, item: str, weight: float = 1.0) -> None:
        raise NotImplementedError

    def top_k(self, k: int) -> list[tuple[str, float]]:
        """Up to k items; fewer if fewer exist (no padding)."""
        raise NotImplementedError
