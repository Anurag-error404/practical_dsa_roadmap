"""BFS reachability check."""
from models import Cell, Maze


def reachable_from(maze: Maze, start: Cell) -> set[Cell]:
    raise NotImplementedError


def is_fully_connected(maze: Maze, start: Cell) -> bool:
    """Every open cell is reachable from start."""
    raise NotImplementedError
