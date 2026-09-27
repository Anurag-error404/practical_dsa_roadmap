from collections.abc import Hashable
from dataclasses import dataclass, field

Node = Hashable


@dataclass
class Driver:
    id: str
    location: Node
    online: bool = True
    busy: bool = False


@dataclass
class RideRequest:
    id: str
    pickup: Node
    dropoff: Node
    requested_at: float = 0.0


@dataclass
class Assignment:
    request_id: str
    driver_id: str
    eta: float
    route: list[Node] = field(default_factory=list)


@dataclass
class Unmatched:
    request_id: str
    reason: str
