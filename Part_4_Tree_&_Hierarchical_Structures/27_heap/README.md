# Heap From Scratch (T1)

*Part 4 — Trees & Hierarchical Structures*

## Problem

Finding "the current max/min" by scanning is O(n) every time; it should be O(1).

## Objective

Implement heapify, insert, and extract-min/max for a binary heap.

---

**Input:** `insert(value)`, `extract_min()` / `extract_max()`, `peek()`; optionally `heapify(array)`. **Output:** Correct min/max maintained after every operation; the internal array satisfies the heap property after every mutation.

**Edge cases:**

- `extract()` on an empty heap
- Heap with exactly one element
- Inserting duplicate values
- Sift-up/sift-down at the boundaries (root, last leaf) — index math here is the usual bug source
- Building a heap from an existing unsorted array should be implemented as `heapify` in O(n), not as n individual `insert()` calls (which would be O(n log n))

**Suggested structure:**

```
heap/
├── heap.py           # insert/extract/peek/heapify
└── tests/
    └── test_heap.py  # heap-property verification after every operation
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
