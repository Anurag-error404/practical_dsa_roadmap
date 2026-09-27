"""A*/Dijkstra with incremental recompute."""
from models import Cell, Maze


def find_path(maze: Maze, start: Cell, goal: Cell) -> list[Cell] | None:
    raise NotImplementedError


def path_still_valid(maze: Maze, path: list[Cell]) -> bool:
    """False once any cell on the path became a wall."""
    raise NotImplementedError
