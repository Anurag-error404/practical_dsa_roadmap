"""Binary-search-based bisection."""
from collections.abc import Callable


def find_first_bad(n: int, test_commit: Callable[[int], bool]) -> int:
    """Index of the first bad commit in 0..n-1 using O(log n) test_commit() calls."""
    raise NotImplementedError
