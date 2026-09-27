"""Shortest path / degrees of separation."""
from models import FriendGraph, UserId


def degrees_of_separation(graph: FriendGraph, a: UserId, b: UserId) -> tuple[int, list[UserId]] | None:
    """(degree, path), or None if not connected."""
    raise NotImplementedError
