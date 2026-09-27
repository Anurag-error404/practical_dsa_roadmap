from dataclasses import dataclass

from indexer import InvertedIndex


@dataclass
class SearchResult:
    doc_id: str
    score: float
    positions: list[int]


class CatalogueSearch:
    def __init__(self, documents: dict[str, str]):
        self.documents = dict(documents)
        self.index = InvertedIndex()
        for doc_id, text in self.documents.items():
            self.index.add_document(doc_id, text)

    def search(self, query: str, limit: int = 10) -> list[SearchResult]:
        """Ranked documents containing the term/phrase. No hits: empty list."""
        raise NotImplementedError
