"""Linked-list/rope-based buffer."""


class TextBuffer:
    def __init__(self, text: str = ""):
        raise NotImplementedError

    def insert(self, position: int, text: str) -> None:
        raise NotImplementedError

    def delete(self, position: int, length: int) -> str:
        """Remove and return the deleted text."""
        raise NotImplementedError

    def text(self) -> str:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
