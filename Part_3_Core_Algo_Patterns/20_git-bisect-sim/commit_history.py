"""Generates a mock history with a hidden first-bad commit."""
import random


class CommitHistory:
    """Commits 0..n-1. All commits before `first_bad` are good, all from it onward are bad.

    The algorithm should only learn state through test_commit(); `calls` counts those checks.
    """

    def __init__(self, n: int, first_bad: int | None = None, seed: int | None = None):
        if n < 1:
            raise ValueError("history needs at least one commit")
        self.n = n
        self.first_bad = random.Random(seed).randrange(n) if first_bad is None else first_bad
        if not 0 <= self.first_bad < n:
            raise ValueError(f"first_bad must be in [0, {n})")
        self.calls = 0

    def test_commit(self, commit_id: int) -> bool:
        """True if the commit is bad."""
        if not 0 <= commit_id < self.n:
            raise IndexError(commit_id)
        self.calls += 1
        return commit_id >= self.first_bad

    def __len__(self) -> int:
        return self.n


if __name__ == "__main__":
    h = CommitHistory(10, first_bad=3)
    assert [h.test_commit(i) for i in range(10)] == [False] * 3 + [True] * 7 and h.calls == 10
    assert CommitHistory(100, seed=4).first_bad == CommitHistory(100, seed=4).first_bad
    print("commit_history ok")
