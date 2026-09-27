from typing import Any


class Node:
    def __init__(self, value: Any, prev: "Node | None" = None, next: "Node | None" = None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        raise NotImplementedError

    def insert(self, value: Any, position: int) -> None:
        """Insert so value ends up at `position` (0 = head, len = tail). Keep prev/next consistent."""
        raise NotImplementedError

    def delete(self, position: int) -> Any:
        """Remove and return the value at `position`."""
        raise NotImplementedError

    def reverse(self) -> None:
        """Reverse in place. 0 or 1 nodes is a no-op."""
        raise NotImplementedError

    def detect_cycle(self) -> bool:
        raise NotImplementedError

    def to_list(self) -> list:
        """Values head -> tail, for assertions."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
