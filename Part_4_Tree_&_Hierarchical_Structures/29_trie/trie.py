"""insert/search/starts_with/delete."""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        """True only if `word` was inserted as a complete word."""
        raise NotImplementedError

    def starts_with(self, prefix: str) -> bool:
        """True if any inserted word starts with prefix."""
        raise NotImplementedError

    def delete(self, word: str) -> bool:
        """Remove word without breaking other words that share its nodes. Return True if it existed."""
        raise NotImplementedError
