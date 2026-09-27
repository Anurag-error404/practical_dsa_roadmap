"""Rendering plus input handling. curses (stdlib) works for a terminal version."""
from grid import Cell, Grid


class Game:
    def __init__(self, grid: Grid, player: Cell, npc: Cell, goal: Cell):
        raise NotImplementedError

    def handle_input(self, key: str) -> None:
        """Move the player or place an obstacle."""
        raise NotImplementedError

    def tick(self) -> None:
        """Advance one step: the NPC follows its path, recomputing only if needed."""
        raise NotImplementedError

    def render(self) -> str:
        raise NotImplementedError


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
