"""Topological sort plus cycle detection."""


class DependencyGraph:
    def __init__(self):
        raise NotImplementedError

    def add_task(self, task_id: int) -> None:
        raise NotImplementedError

    def add_dependency(self, task_id: int, depends_on: int) -> None:
        """Record task_id -> depends_on. Must reject self-cycles and multi-task cycles up front."""
        raise NotImplementedError

    def would_create_cycle(self, task_id: int, depends_on: int) -> bool:
        raise NotImplementedError

    def dependents(self, task_id: int) -> set[int]:
        """Tasks that depend directly on task_id."""
        raise NotImplementedError
