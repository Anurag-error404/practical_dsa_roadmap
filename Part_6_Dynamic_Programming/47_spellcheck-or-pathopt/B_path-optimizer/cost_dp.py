from grid import Cell, CostGrid


def min_cost_path(grid: CostGrid, start: Cell, end: Cell) -> tuple[float, list[Cell]] | None:
    """(total cost, path) avoiding obstacles, or None when unreachable."""
    raise NotImplementedError
