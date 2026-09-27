from collections.abc import Iterable

from indexer import InvertedIndex
from matcher import find_phrase
from models import Document, SearchResult
from ranker import top_k
from trie import Trie


class SearchEngine:
    def __init__(self):
        self.documents: dict[str, Document] = {}
        self.index = InvertedIndex()
        self.trie = Trie()

    def add_documents(self, docs: Iterable[Document]) -> None:
        """Store, index, and feed each doc's terms to the trie."""
        raise NotImplementedError

    def query(self, text: str, k: int = 10) -> list[SearchResult]:
        """Ranked results for keywords and/or "exact phrases". No hits: empty list."""
        raise NotImplementedError

    def autocomplete(self, prefix: str, limit: int = 10) -> list[str]:
        raise NotImplementedError
