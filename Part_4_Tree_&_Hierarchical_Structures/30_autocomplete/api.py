"""query(prefix) -> ranked suggestions."""
from collections.abc import Iterable
from pathlib import Path

from ranker import Ranker
from trie import Trie


def load_words(path: str | Path) -> list[str]:
    """One word per line; blank lines skipped."""
    return [w for line in Path(path).read_text().splitlines() if (w := line.strip())]


class Autocomplete:
    def __init__(self, words: Iterable[str], frequencies: dict[str, int] | None = None):
        self.trie = Trie()
        for w in words:
            self.trie.insert(w)
        self.ranker = Ranker(frequencies)

    def query(self, prefix: str, limit: int = 10) -> list[str]:
        """Up to `limit` ranked completions of prefix. No matches: empty list."""
        raise NotImplementedError
