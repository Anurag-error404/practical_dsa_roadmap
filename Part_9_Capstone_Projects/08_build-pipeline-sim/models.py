from dataclasses import dataclass, field


@dataclass
class BuildTask:
    name: str
    duration: float = 1.0
    deps: list[str] = field(default_factory=list)


@dataclass
class Schedule:
    rounds: list[list[str]] = field(default_factory=list)
    total_time: float = 0.0
