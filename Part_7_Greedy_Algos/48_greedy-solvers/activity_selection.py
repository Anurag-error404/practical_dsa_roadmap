from dataclasses import dataclass


@dataclass
class Activity:
    start: float
    end: float


def select_activities(activities: list[Activity]) -> list[Activity]:
    """Max set of non-overlapping activities. Document whether touching endpoints overlap."""
    raise NotImplementedError
