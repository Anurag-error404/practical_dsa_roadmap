# Dynamic Array (T1)

*Part 1 — Foundations*

## Problem

Built-in arrays hide their resize logic — you don't know what happens on overflow.

## Objective

Implement push/get/resize-on-overflow; verify amortized O(1) append via benchmark.

---

**Input:** A sequence of operations: `push(value)`, `get(index)`. **Output:** Correct value returned by `get()`; internal `size`/`capacity` inspectable for tests.

**Edge cases:**

- `get()` with an out-of-bounds index — should raise/return a clear error, not read garbage memory
- `push()` exactly at current capacity — must trigger resize (commonly ×2) *before* the write, not after
- Many pushes then many removals — decide whether to shrink capacity back down (and when)
- Pushing zero elements, then calling `get(0)` — should fail cleanly

**Suggested structure:**

```
dynamic-array/
├── dynamic_array.py
└── tests/
    └── test_dynamic_array.py   # capacity growth, bounds checks, amortized cost
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
