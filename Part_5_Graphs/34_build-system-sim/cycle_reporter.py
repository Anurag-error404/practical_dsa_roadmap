"""Extracts and displays the actual cycle path."""


def find_cycle(deps: dict[str, list[str]]) -> list[str] | None:
    """The tasks forming a cycle, in order (e.g. [a, b, c, a]), or None."""
    raise NotImplementedError


def format_cycle(cycle: list[str]) -> str:
    raise NotImplementedError
