import pytest

from n_queens import solve_n_queens
from sudoku_solver import solve_sudoku
from permutations_subsets import permutations, subsets


def test_n_queens_2_and_3_have_no_solution():
    # TODO: N-Queens for N=2 or N=3 — provably has no solution; must return empty, not crash or
    #       loop
    ...


def test_sudoku_invalid_or_unsolvable_start():
    # TODO: A Sudoku puzzle that's invalid or unsolvable from the start (contradictory pre-
    #       filled cells)
    ...


def test_sudoku_already_solved():
    # TODO: A Sudoku puzzle that's already fully solved (no blanks to fill)
    ...


def test_duplicate_elements_policy():
    # TODO: Duplicate elements in the permutation/subset input — decide whether duplicate
    #       results should be filtered
    ...


def test_empty_set_yields_empty_subset():
    # TODO: Empty input set for subsets — the empty set itself is a valid subset and should
    #       appear in the output
    ...
