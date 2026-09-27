"""Builds an inverted index across documents."""
from pathlib import Path


def load_documents(folder: str | Path) -> dict[str, str]:
    """doc_id -> text for every document in folder."""
    raise NotImplementedError


def tokenize(text: str) -> list[str]:
    """Terms as indexed. Whole-word vs partial matching is decided here."""
    raise NotImplementedError


class InvertedIndex:
    def __init__(self):
        raise NotImplementedError

    def add_document(self, doc_id: str, text: str) -> None:
        """Index one document (incremental add/update policy is yours)."""
        raise NotImplementedError

    def postings(self, term: str) -> dict[str, list[int]]:
        """doc_id -> positions of term."""
        raise NotImplementedError
