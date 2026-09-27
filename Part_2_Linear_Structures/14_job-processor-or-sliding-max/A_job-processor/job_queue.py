"""Heap-based priority queue."""
from dataclasses import dataclass
from typing import Any


@dataclass
class Job:
    id: int
    priority: int
    payload: Any = None


class JobQueue:
    def __init__(self):
        raise NotImplementedError

    def submit_job(self, priority: int, payload: Any = None) -> Job:
        """Enqueue a new job and return it (with its assigned id)."""
        raise NotImplementedError

    def process_next(self) -> Job:
        """Remove and return the highest-priority job."""
        raise NotImplementedError

    def update_priority(self, job_id: int, priority: int) -> None:
        """Change a queued job's priority (heaps have no update-in-place, so you need a workaround)."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
