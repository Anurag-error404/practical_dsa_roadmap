"""Grid representation plus obstacle placement. Storage only."""
from collections.abc import Iterator

Cell = tuple[int, int]


class Grid:
    def __init__(self, rows: int, cols: int, walls: set[Cell] | None = None):
        self.rows = rows
        self.cols = cols
        self.walls: set[Cell] = set(walls or ())

    @classmethod
    def from_matrix(cls, matrix: list[list[int]]) -> "Grid":
        """1 = wall, 0 = open (the format random_grid() produces)."""
        return cls(len(matrix), len(matrix[0]) if matrix else 0,
                   {(r, c) for r, row in enumerate(matrix) for c, v in enumerate(row) if v})

    def in_bounds(self, cell: Cell) -> bool:
        r, c = cell
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_open(self, cell: Cell) -> bool:
        return self.in_bounds(cell) and cell not in self.walls

    def place_wall(self, cell: Cell) -> None:
        self.walls.add(cell)

    def remove_wall(self, cell: Cell) -> None:
        self.walls.discard(cell)

    def neighbors(self, cell: Cell) -> Iterator[Cell]:
        """Walkable cells one step from `cell`. Movement rules (4 vs 8 directions) are yours."""
        raise NotImplementedError
