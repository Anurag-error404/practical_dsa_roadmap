from dataclasses import dataclass, field

Snapshot = dict[str, str]


@dataclass
class Commit:
    id: str
    message: str
    files: dict[str, str] = field(default_factory=dict)
    parent_ids: list[str] = field(default_factory=list)
