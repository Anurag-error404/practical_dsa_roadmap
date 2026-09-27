"""Autocomplete. Copy in or adapt your Project 29/30 trie."""


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def complete(self, prefix: str, limit: int = 10) -> list[str]:
        """Up to `limit` stored words starting with prefix. No matches: empty list."""
        raise NotImplementedError
