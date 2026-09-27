# Backtracking Solver Set (T1)

*Part 3 — Core Algorithmic Patterns*

## Problem

Some problems (N-Queens, Sudoku) have no formula — only systematic trial and undo.

## Objective

Solve N-Queens, a Sudoku solver, and a permutations/subsets generator.

---

**Input:** N (N-Queens); a 9×9 grid with some cells pre-filled (Sudoku); a set of distinct elements (permutations/subsets). **Output:** All valid solutions (or one); all permutations/subsets.

**Edge cases:**

- N-Queens for N=2 or N=3 — provably has *no* solution; must return empty, not crash or loop
- A Sudoku puzzle that's invalid or unsolvable from the start (contradictory pre-filled cells)
- A Sudoku puzzle that's already fully solved (no blanks to fill)
- Duplicate elements in the permutation/subset input — decide whether duplicate results should be filtered
- Empty input set for subsets — the empty set itself is a valid subset and should appear in the output

**Suggested structure:**

```
backtracking-solvers/
├── n_queens.py
├── sudoku_solver.py
├── permutations_subsets.py
└── tests/
    └── test_backtracking.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
