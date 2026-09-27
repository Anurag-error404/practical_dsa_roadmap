from typing import Any


class Deque:
    """O(1) push/pop at both ends."""

    def __init__(self, capacity: int | None = None):
        raise NotImplementedError

    def push_front(self, value: Any) -> None:
        raise NotImplementedError

    def push_back(self, value: Any) -> None:
        raise NotImplementedError

    def pop_front(self) -> Any:
        raise NotImplementedError

    def pop_back(self) -> Any:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
