"""Unblocks dependents on completion and feeds the heap."""
from collections.abc import Iterable
from datetime import datetime

from dependency_graph import DependencyGraph
from models import Task
from priority_queue import ReadyQueue


class TaskManager:
    def __init__(self):
        self.tasks: dict[int, Task] = {}
        self.graph = DependencyGraph()
        self.ready = ReadyQueue()

    def create_task(self, name: str, priority: int, dependencies: Iterable[int] = (),
                    deadline: datetime | None = None) -> Task:
        raise NotImplementedError

    def complete_task(self, task_id: int) -> None:
        """Mark done and unblock any dependents whose dependencies are now all done."""
        raise NotImplementedError

    def get_next_task(self) -> Task | None:
        """Highest-priority task among currently unblocked ones."""
        raise NotImplementedError

    def report(self, now: datetime | None = None) -> dict[str, list[Task]]:
        """{"blocked": [...], "overdue": [...]}."""
        raise NotImplementedError
