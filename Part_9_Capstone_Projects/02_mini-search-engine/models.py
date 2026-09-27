from dataclasses import dataclass, field


@dataclass
class Document:
    id: str
    text: str
    title: str = ""


@dataclass
class SearchResult:
    doc_id: str
    score: float
    positions: list[int] = field(default_factory=list)
    snippets: list[str] = field(default_factory=list)
