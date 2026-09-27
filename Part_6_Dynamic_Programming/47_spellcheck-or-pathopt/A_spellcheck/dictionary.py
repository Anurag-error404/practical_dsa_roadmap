from pathlib import Path


def load_dictionary(path: str | Path) -> dict[str, int]:
    """word -> frequency (for tie-break ranking)."""
    raise NotImplementedError
