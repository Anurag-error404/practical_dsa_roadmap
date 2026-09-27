"""Project schema."""
from dataclasses import dataclass


@dataclass
class Project:
    name: str
    cost: int
    value: int
