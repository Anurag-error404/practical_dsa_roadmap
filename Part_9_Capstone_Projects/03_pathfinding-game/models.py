"""Maze storage shared by the generator, validator, pathfinder, NPC, and game loop."""
from dataclasses import dataclass, field

Cell = tuple[int, int]


@dataclass
class Maze:
    rows: int
    cols: int
    walls: set[Cell] = field(default_factory=set)

    def in_bounds(self, cell: Cell) -> bool:
        r, c = cell
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_open(self, cell: Cell) -> bool:
        return self.in_bounds(cell) and cell not in self.walls
