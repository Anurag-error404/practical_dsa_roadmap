"""Traces back which items were chosen."""


def reconstruct_01(dp: list[list[int]], weights: list[int], capacity: int) -> list[int]:
    """Indices of the chosen items."""
    raise NotImplementedError


def reconstruct_unbounded(dp: list[int], weights: list[int], values: list[int], capacity: int) -> list[int]:
    """Indices of the chosen items (repeats allowed)."""
    raise NotImplementedError
