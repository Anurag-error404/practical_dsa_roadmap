"""Public API tying the buffer, history, autocomplete, and search together."""
from search import find, replace_all
from text_buffer import TextBuffer
from trie import Trie
from undo_redo import History


class Editor:
    def __init__(self, text: str = ""):
        self.buffer = TextBuffer(text)
        self.history = History()
        self.words = Trie()

    def insert(self, position: int, text: str) -> None:
        raise NotImplementedError

    def delete(self, position: int, length: int) -> None:
        raise NotImplementedError

    def undo(self) -> None:
        raise NotImplementedError

    def redo(self) -> None:
        raise NotImplementedError

    def find(self, pattern: str) -> list[int]:
        raise NotImplementedError

    def replace(self, pattern: str, replacement: str) -> int:
        """Replace all; return the count."""
        raise NotImplementedError

    def suggest(self, prefix: str, limit: int = 5) -> list[str]:
        raise NotImplementedError
