"""Splits an expression string into tokens."""


class ParseError(ValueError):
    """Malformed expression (unbalanced parentheses, stray characters, ...)."""


def tokenize(expr: str) -> list[str]:
    """Numbers (multi-digit, decimals), operators, and parens, ignoring spacing."""
    raise NotImplementedError
