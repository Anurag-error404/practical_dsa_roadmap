"""NPC state machine plus path following."""
from models import Cell, Maze


class NPC:
    def __init__(self, position: Cell):
        self.position = position
        self.path: list[Cell] = []
        self.state = "idle"

    def update(self, maze: Maze, target: Cell) -> Cell:
        """Advance one step toward target, recomputing the path only when invalidated."""
        raise NotImplementedError
