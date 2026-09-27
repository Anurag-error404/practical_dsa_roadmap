"""Binary indexed tree, prefix-sum based."""


class FenwickTree:
    def __init__(self, values: list[int]):
        raise NotImplementedError

    def update(self, index: int, value: int) -> None:
        """Set values[index] = value (not add), in O(log n)."""
        raise NotImplementedError

    def prefix_sum(self, index: int) -> int:
        """Sum of values[0..index] inclusive."""
        raise NotImplementedError

    def query(self, left: int, right: int) -> int:
        """Sum of values[left..right] inclusive."""
        raise NotImplementedError
