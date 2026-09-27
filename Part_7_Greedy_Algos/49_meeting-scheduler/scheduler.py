"""Greedy interval scheduling."""
from models import Meeting


def schedule(meetings: list[Meeting]) -> tuple[list[Meeting], list[Meeting]]:
    """(accepted, rejected): the max conflict-free set, plus everything left out."""
    raise NotImplementedError
