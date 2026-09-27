import pytest

from maze.generator import generate_maze
from maze.solver import solve_maze
from sudoku.validator import is_valid_board
from sudoku.solver import solve_sudoku, count_solutions, hint


def test_generated_maze_always_solvable():
    # TODO: Maze generation must guarantee solvability — use a generation method that inherently
    #       guarantees connectivity (e.g., randomized DFS or Prim's-based carving) rather than
    #       generating random walls and hoping
    ...


def test_one_by_one_maze():
    # TODO: A 1×1 maze (degenerate case)
    ...


def test_sudoku_multiple_solutions_flagged_ambiguous():
    # TODO: A Sudoku puzzle with multiple valid solutions — flag it as ambiguous rather than
    #       silently returning one
    ...


def test_hint_on_solved_or_contradictory_puzzle_flagged():
    # TODO: User requests a hint on an already-solved or contradictory puzzle — this is an
    #       invalid state to flag, not solve around
    ...
