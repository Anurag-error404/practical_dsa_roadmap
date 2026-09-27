"""Reads the dependency spec."""
from pathlib import Path

from models import BuildTask


def parse_spec(text: str) -> dict[str, BuildTask]:
    raise NotImplementedError


def load_spec(path: str | Path) -> dict[str, BuildTask]:
    return parse_spec(Path(path).read_text())
