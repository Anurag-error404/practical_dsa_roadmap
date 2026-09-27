"""sum/avg/filter over a single column."""
from collections.abc import Callable
from typing import Any

from store import ColumnStore


def col_sum(store: ColumnStore, column: str) -> float:
    """Sum of a column. An empty dataset sums to 0."""
    raise NotImplementedError


def col_avg(store: ColumnStore, column: str) -> float | None:
    """Average of a column. Empty dataset: error or None, your call."""
    raise NotImplementedError


def col_filter(store: ColumnStore, column: str, predicate: Callable[[Any], bool]) -> list[int]:
    """Row indices whose value in `column` satisfies `predicate`."""
    raise NotImplementedError
