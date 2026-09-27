"""Heap of ready (unblocked) tasks."""
from models import Task


class ReadyQueue:
    def __init__(self):
        raise NotImplementedError

    def push(self, task: Task) -> None:
        raise NotImplementedError

    def pop(self) -> Task:
        """Highest-priority ready task (ties broken by deadline, then creation order)."""
        raise NotImplementedError

    def peek(self) -> Task | None:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
