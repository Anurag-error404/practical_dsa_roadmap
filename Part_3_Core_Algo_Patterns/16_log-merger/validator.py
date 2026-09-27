"""Checks each input file is pre-sorted."""
from pathlib import Path


def check_sorted(path: Path) -> int | None:
    """Line number of the first out-of-order line, or None if the file is sorted."""
    raise NotImplementedError
