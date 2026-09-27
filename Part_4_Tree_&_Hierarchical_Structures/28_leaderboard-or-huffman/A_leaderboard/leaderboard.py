"""Heap + hash map: O(log n) update, O(k) top-k read."""


class Leaderboard:
    def __init__(self):
        raise NotImplementedError

    def update(self, user: str, score: float) -> None:
        """Set user's score. Repeated updates move the user, never duplicate them."""
        raise NotImplementedError

    def top_k(self, k: int) -> list[tuple[str, float]]:
        """Current top k (user, score), best first."""
        raise NotImplementedError
