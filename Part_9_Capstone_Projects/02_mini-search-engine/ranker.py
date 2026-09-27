"""Heap-based top-K relevance ranking."""


def top_k(scores: dict[str, float], k: int) -> list[tuple[str, float]]:
    """Best k (doc_id, score) with a stable tie-break."""
    raise NotImplementedError
