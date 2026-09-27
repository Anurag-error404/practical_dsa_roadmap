# Segment Tree & Fenwick Tree (T1)

*Part 8 — Advanced Topics*

## Problem

Range-sum queries over frequently-updated data are slow both to read (recompute) and write (naive) naively.

## Objective

Implement both structures supporting O(log n) range query and point update.

---

**Input:** An array; `range_query(l, r)` (sum/min/max); `update(index, value)`. **Output:** Correct aggregate for the queried range; a structure reflecting point updates immediately.

**Edge cases:**

- `l > r`, or out-of-bounds indices — should be validated and rejected
- `l == r` (single-element range query)
- Re-updating an index that was already updated before — behavior should be consistent (a "set," not accidentally an "add," unless explicitly built as an add-based Fenwick tree)
- Querying the full array range (a boundary case for the tree's internal structure)
- An empty array (size 0) — handle explicitly or disallow, but don't crash silently

**Suggested structure:**

```
segment-fenwick/
├── segment_tree.py   # range query + point update
├── fenwick_tree.py   # binary indexed tree, prefix-sum based
└── tests/
    └── test_range_queries.py   # l==r, full range, cross-checked against brute-force sum
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
