"""Most-connected users."""
from models import FriendGraph, UserId


def most_connected(graph: FriendGraph, k: int) -> list[tuple[UserId, int]]:
    """Top k (user, friend_count). Ties at position k: include or cap, documented."""
    raise NotImplementedError
