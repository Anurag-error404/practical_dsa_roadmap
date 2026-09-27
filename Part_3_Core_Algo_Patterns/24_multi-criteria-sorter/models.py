"""Item schema."""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Item:
    name: str
    date: datetime | None = None
    size: int | None = None
