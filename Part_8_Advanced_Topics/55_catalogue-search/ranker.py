"""Scores and ranks results."""


def rank(hits: dict[str, list[int]], doc_lengths: dict[str, int], limit: int | None = None) -> list[tuple[str, float]]:
    """(doc_id, score) best first, from each doc's match positions."""
    raise NotImplementedError
