"""Reads CSV into a column-oriented store."""
from pathlib import Path

from store import ColumnStore


def load_csv(path: str | Path) -> ColumnStore:
    """Load CSV rows into a ColumnStore.

    Dirty data (a stray non-numeric value in a numeric column) must fail loudly here,
    not later at query time.
    """
    raise NotImplementedError
