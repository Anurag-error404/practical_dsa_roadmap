"""Failure function plus search."""


def failure_function(pattern: str) -> list[int]:
    """lps[i] = length of the longest proper prefix of pattern[:i+1] that is also a suffix."""
    raise NotImplementedError


def kmp_search(text: str, pattern: str) -> list[int]:
    """Every start index of pattern in text, overlapping matches included."""
    raise NotImplementedError
