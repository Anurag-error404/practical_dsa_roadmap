"""Riders/tasks are Requests; drivers/workers are Resources."""
from dataclasses import dataclass, field

Location = tuple[float, float]


@dataclass
class Request:
    id: str
    location: Location
    required_skill: str | None = None
    requested_at: float = 0.0


@dataclass
class Resource:
    id: str
    location: Location
    available: bool = True
    skills: frozenset[str] = frozenset()


@dataclass
class Assignment:
    request_id: str
    resource_id: str
    cost: float


@dataclass
class MatchResult:
    assignments: list[Assignment] = field(default_factory=list)
    unmatched_requests: list[str] = field(default_factory=list)
    idle_resources: list[str] = field(default_factory=list)
