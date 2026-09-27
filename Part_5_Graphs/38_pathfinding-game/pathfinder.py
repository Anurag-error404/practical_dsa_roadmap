"""A* or Dijkstra."""
from grid import Cell, Grid


def find_path(grid: Grid, start: Cell, goal: Cell) -> list[Cell] | None:
    """Cells from start to goal inclusive, or None when unreachable."""
    raise NotImplementedError
