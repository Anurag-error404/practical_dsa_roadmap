from collections.abc import Hashable


def friendships(source: list[list[int]] | dict[Hashable, list[Hashable]]) -> tuple[list[Hashable], list[tuple[Hashable, Hashable]]]:
    """Normalize an adjacency matrix or adjacency list into (people, friendship_pairs)."""
    raise NotImplementedError
