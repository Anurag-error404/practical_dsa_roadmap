# Grid/Path DP Solvers (T1)

*Part 6 — Dynamic Programming*

## Problem

Counting paths or minimum cost through a grid by brute-force enumeration is exponential.

## Objective

Implement unique-paths, min-path-sum, and edit-distance.

---

**Input:** An m×n grid (with obstacle markers for the obstacle variant); two strings (edit distance). **Output:** Number of unique paths, minimum path sum, or minimum edit distance.

**Edge cases:**

- The start or end cell itself is an obstacle — 0 valid paths
- A 1×1 grid — trivially 1 path, cost equal to the single cell's value
- Edit distance between two identical strings — 0
- Edit distance where one string is empty — distance equals the length of the other string
- An obstacle configuration that fully blocks every path — must return 0, not crash

**Suggested structure:**

```
grid-path-dp/
├── unique_paths.py
├── min_path_sum.py
├── edit_distance.py
└── tests/
    └── test_grid_dp.py   # fully-blocked-path case, explicitly
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
