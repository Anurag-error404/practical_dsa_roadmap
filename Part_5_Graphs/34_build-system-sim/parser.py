"""Reads the dependency spec file."""
from pathlib import Path


def parse_spec(text: str) -> dict[str, list[str]]:
    """task -> tasks it depends on. Pick a spec format (e.g. "build: compile test")."""
    raise NotImplementedError


def load_spec(path: str | Path) -> dict[str, list[str]]:
    return parse_spec(Path(path).read_text())
