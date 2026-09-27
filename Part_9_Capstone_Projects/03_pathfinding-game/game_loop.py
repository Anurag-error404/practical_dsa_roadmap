"""Rendering plus input. curses (stdlib) works for a terminal version."""
from models import Cell, Maze
from npc import NPC


class Game:
    def __init__(self, maze: Maze, player: Cell, npc: NPC):
        self.maze = maze
        self.player = player
        self.npc = npc

    def handle_input(self, key: str) -> None:
        raise NotImplementedError

    def tick(self) -> None:
        raise NotImplementedError

    def render(self) -> str:
        raise NotImplementedError


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
