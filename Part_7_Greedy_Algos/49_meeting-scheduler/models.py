from dataclasses import dataclass


@dataclass
class Meeting:
    start: float
    end: float
    priority: int = 0
    name: str = ""
