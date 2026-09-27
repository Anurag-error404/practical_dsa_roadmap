from pathlib import Path


def split_lines(text: str) -> list[str]:
    """Lines for diffing. Trailing-newline and line-ending handling is yours."""
    raise NotImplementedError


def read_lines(path: str | Path) -> list[str]:
    return split_lines(Path(path).read_text())
