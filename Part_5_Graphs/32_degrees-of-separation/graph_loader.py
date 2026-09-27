"""Loads edges into an adjacency list."""
from pathlib import Path


def load_edges(path: str | Path) -> dict[str, set[str]]:
    """Undirected friend graph from a file of "a b" pairs, one per line."""
    raise NotImplementedError
