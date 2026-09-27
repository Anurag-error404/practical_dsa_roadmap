"""Loads and normalizes documents."""
from pathlib import Path


def load_documents(folder: str | Path) -> dict[str, str]:
    """Map document name to raw text for every document in `folder`."""
    raise NotImplementedError


def normalize(text: str) -> str:
    """Canonical form used for comparison (casing, punctuation, whitespace)."""
    raise NotImplementedError
