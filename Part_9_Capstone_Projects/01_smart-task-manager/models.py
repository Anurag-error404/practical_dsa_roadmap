"""Task schema (id, priority, deps, deadline, status)."""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Status(Enum):
    PENDING = "pending"
    DONE = "done"


@dataclass
class Task:
    id: int
    name: str
    priority: int
    dependencies: set[int] = field(default_factory=set)
    deadline: datetime | None = None
    status: Status = Status.PENDING
    created_seq: int = 0
