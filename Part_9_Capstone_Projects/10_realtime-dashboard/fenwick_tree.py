"""Fenwick tree (binary indexed tree). Copy in or adapt your Project 52 implementation."""


class FenwickTree:
    def __init__(self, size: int):
        """All-zero tree over indices 0..size-1."""
        raise NotImplementedError

    def add(self, index: int, delta: float) -> None:
        """Point update: values[index] += delta."""
        raise NotImplementedError

    def prefix_sum(self, index: int) -> float:
        """Sum of values[0..index] inclusive."""
        raise NotImplementedError

    def range_sum(self, left: int, right: int) -> float:
        """Sum of values[left..right] inclusive."""
        raise NotImplementedError
