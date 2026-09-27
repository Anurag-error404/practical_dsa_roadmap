from dataclasses import dataclass
from typing import Literal


@dataclass
class Edit:
    """One reversible change, recorded for undo/redo."""
    kind: Literal["insert", "delete"]
    position: int
    text: str
