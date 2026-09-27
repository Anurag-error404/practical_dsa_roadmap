from collections.abc import Iterator

Cell = tuple[int, int]


def foreground_cells(grid: list[list[int]]) -> list[Cell]:
    raise NotImplementedError


def neighbors(grid: list[list[int]], cell: Cell) -> Iterator[Cell]:
    """Adjacent foreground cells. 4- vs 8-connectivity is decided (and documented) here."""
    raise NotImplementedError
