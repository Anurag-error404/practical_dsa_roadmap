"""Inverted index (hashing)."""
from models import Document


def tokenize(text: str) -> list[str]:
    raise NotImplementedError


class InvertedIndex:
    def __init__(self):
        raise NotImplementedError

    def add(self, doc: Document) -> None:
        """Index one document; supports incremental builds."""
        raise NotImplementedError

    def postings(self, term: str) -> dict[str, list[int]]:
        """doc_id -> term positions."""
        raise NotImplementedError

    def terms(self) -> list[str]:
        raise NotImplementedError
