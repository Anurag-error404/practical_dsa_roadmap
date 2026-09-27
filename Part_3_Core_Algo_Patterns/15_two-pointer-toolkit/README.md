# Two-Pointer Toolkit (T1)

*Part 3 — Core Algorithmic Patterns*

## Problem

Naive pair-finding in sorted data is O(n²) when O(n) is possible.

## Objective

Solve merge-two-sorted-arrays, remove-duplicates, and container-with-most-water.

---

**Input:** Sorted array(s) — two sorted arrays (merge), one sorted array (remove duplicates), or an array of heights (container-with-most-water). **Output:** Merged sorted array; deduplicated array with new logical length; max water area (integer).

**Edge cases:**

- One or both arrays empty (merge)
- Array where every element is a duplicate (dedup result should be length 1)
- All-equal heights for the container problem (area is determined purely by width)
- Array of length 0 or 1 for the container problem — no valid pair exists

**Suggested structure:**

```
two-pointer-toolkit/
├── merge_sorted.py
├── remove_duplicates.py
├── container_with_water.py
└── tests/
    └── test_two_pointer.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
