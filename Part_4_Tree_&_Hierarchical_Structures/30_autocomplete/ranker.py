"""Frequency-based suggestion ranking."""


class Ranker:
    def __init__(self, frequencies: dict[str, int] | None = None):
        raise NotImplementedError

    def record_use(self, word: str) -> None:
        """Optional: bump a word's rank when it's used."""
        raise NotImplementedError

    def rank(self, words: list[str], limit: int) -> list[str]:
        """The best `limit` words, most useful first."""
        raise NotImplementedError
