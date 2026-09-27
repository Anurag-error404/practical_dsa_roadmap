from dataclasses import dataclass


@dataclass
class Event:
    timestamp: float
    user_id: str
    event_type: str
    value: float
