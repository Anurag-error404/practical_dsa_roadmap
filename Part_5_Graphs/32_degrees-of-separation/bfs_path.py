"""Shortest path plus degree count."""


def shortest_path(adj: dict[str, set[str]], a: str, b: str) -> list[str] | None:
    """One shortest path a -> ... -> b (deterministic among ties), or None if not connected."""
    raise NotImplementedError


def degrees(adj: dict[str, set[str]], a: str, b: str) -> int | None:
    """Edges on the shortest path (0 when a == b), or None if not connected."""
    raise NotImplementedError
