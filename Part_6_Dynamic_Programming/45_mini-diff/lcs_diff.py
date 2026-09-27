"""Reuses/adapts the LCS from Project 44."""

DiffOp = tuple[str, str]


def diff(a: list[str], b: list[str]) -> list[DiffOp]:
    """Ordered ops: (" ", line) unchanged, ("-", line) removed from a, ("+", line) added in b."""
    raise NotImplementedError
