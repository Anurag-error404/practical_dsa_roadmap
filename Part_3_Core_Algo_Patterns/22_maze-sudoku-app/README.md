# Maze/Sudoku App (T2)

*Part 3 — Core Algorithmic Patterns*

## Problem

A puzzle generator needs to guarantee the puzzle it creates is actually solvable.

## Objective

Build a maze generator + solver, or a Sudoku app with a solve/hint feature.

---

**Input:** *(Maze)* grid dimensions + optional random seed. *(Sudoku)* a user-entered puzzle, or a "generate new" request. **Output:** *(Maze)* a generated maze guaranteed to have a solvable path, plus the solved path. *(Sudoku)* a puzzle, plus hint/solve output.

**Edge cases:**

- Maze generation must *guarantee* solvability — use a generation method that inherently guarantees connectivity (e.g., randomized DFS or Prim's-based carving) rather than generating random walls and hoping
- A 1×1 maze (degenerate case)
- A Sudoku puzzle with multiple valid solutions — flag it as ambiguous rather than silently returning one
- User requests a hint on an already-solved or contradictory puzzle — this is an invalid state to flag, not solve around

**Suggested structure:**

```
maze-sudoku-app/
├── maze/
│   ├── generator.py    # randomized DFS or Prim's-based generation
│   └── solver.py        # BFS/DFS solve + path output
├── sudoku/
│   ├── validator.py
│   └── solver.py
└── ui/
    └── app.py
```

---

## Scaffold notes

- Added `tests/test_maze_sudoku.py`; the suggested structure has no tests folder.

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
