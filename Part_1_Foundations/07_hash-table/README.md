# Hash Table From Scratch (T1)

*Part 1 — Foundations*

## Problem

Hash maps feel magic until you've handled a collision yourself.

## Objective

Implement your own hash function + chaining or open addressing; test collision-heavy input.

---

**Input:** A sequence of `put(key, value)`, `get(key)`, `delete(key)` operations. **Output:** Correct value from `get()`; consistent state after `delete()`; no data loss across an internal resize.

**Edge cases:**

- Two different keys hashing to the same bucket (collision) — must resolve via chaining or open addressing, not silently overwrite
- `delete()` on a key that was never inserted — should be a no-op or clear error, not a crash
- Load factor crossing a threshold (e.g., 0.7) — trigger resize + rehash of *all* existing entries, not just new ones
- Using a mutable object as a key — document that this is unsafe (hash could change after insertion) or disallow it

**Suggested structure:**

```
hash-table/
├── hash_table.py       # core structure: put/get/delete/resize
├── hash_functions.py   # your custom hash function(s)
└── tests/
    └── test_collisions.py   # forces collisions deliberately
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
