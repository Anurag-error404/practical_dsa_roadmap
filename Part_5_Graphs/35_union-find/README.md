# Union-Find (T1)

*Part 5 — Graphs*

## Problem

Repeatedly checking "are these two nodes connected" via full traversal is slow at scale.

## Objective

Implement Union-Find with path compression + union by rank; benchmark vs. naive BFS checks.

---

**Input:** A sequence of `union(a, b)` and `find(a)` / `connected(a, b)` operations. **Output:** Correct connectivity answers after every union.

**Edge cases:**

- `union(a, a)` — unioning an element with itself
- `find()` on an element never explicitly added — decide whether it auto-initializes or errors
- Calling `union()` on the same pair repeatedly — should be idempotent, without incorrectly inflating rank/size bookkeeping
- Path compression must not corrupt the rank/size values used by union-by-rank
- A long chain built before path compression runs — a good stress test to confirm the optimization is actually reducing lookup depth, not just present in the code

**Suggested structure:**

```
union-find/
├── union_find.py   # path compression + union by rank
└── tests/
    └── test_union_find.py   # performance comparison with/without optimizations
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
