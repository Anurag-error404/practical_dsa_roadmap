from dataclasses import dataclass
from pathlib import Path


@dataclass
class City:
    name: str
    x: float | None = None
    y: float | None = None


def load_cities(path: str | Path) -> list[City]:
    raise NotImplementedError
