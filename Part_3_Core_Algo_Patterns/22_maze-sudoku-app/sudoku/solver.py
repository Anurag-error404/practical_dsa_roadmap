Grid = list[list[int]]


def solve_sudoku(grid: Grid) -> Grid | None:
    raise NotImplementedError


def count_solutions(grid: Grid, limit: int = 2) -> int:
    """Number of solutions, stopping at `limit` (2 is enough to flag ambiguity)."""
    raise NotImplementedError


def hint(grid: Grid) -> tuple[int, int, int]:
    """(row, col, value) for one blank cell. Solved/contradictory puzzles are an invalid state."""
    raise NotImplementedError
