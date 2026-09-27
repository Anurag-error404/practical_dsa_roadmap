"""Outputs flagged pairs above threshold."""


def format_report(pairs: list[tuple[str, str, float]], passages: dict[tuple[str, str], list[str]]) -> str:
    """Human-readable list of flagged pairs, their scores, and the matched passages."""
    raise NotImplementedError
