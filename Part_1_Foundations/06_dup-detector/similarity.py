"""Shingling, hashing, and comparison logic."""


def shingles(text: str, k: int = 5) -> set:
    """The k-shingles (overlapping k-word or k-char windows) of normalized text."""
    raise NotImplementedError


def similarity(a: set, b: set) -> float:
    """Score in [0, 1] for two shingle sets, normalized for length differences."""
    raise NotImplementedError


def find_similar_pairs(docs: dict[str, str], threshold: float) -> list[tuple[str, str, float]]:
    """(doc_a, doc_b, score) for every pair scoring >= threshold, without an all-pairs scan."""
    raise NotImplementedError


def matching_passages(a: str, b: str, min_length: int) -> list[str]:
    """Passages shared by a and b that are at least `min_length` long."""
    raise NotImplementedError
