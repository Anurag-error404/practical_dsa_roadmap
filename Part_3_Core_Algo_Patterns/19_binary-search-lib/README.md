# Binary Search Library (T1)

*Part 3 — Core Algorithmic Patterns*

## Problem

Standard binary search breaks on duplicates or rotated arrays without care.

## Objective

Implement search, first/last-occurrence, and search-in-rotated-sorted-array.

---

**Input:** A sorted array + target (basic search, first/last occurrence); a rotated sorted array + target (rotated search). **Output:** Index of the target, or a clear "not found" (-1); correct boundary index for first/last occurrence.

**Edge cases:**

- Target not present in the array at all
- Duplicates present — first-occurrence and last-occurrence must return *different, correct* indices
- Empty array, and array of size exactly 1
- Rotated array where the rotation point is 0 (i.e., not actually rotated) — must still work
- Target equal to the pivot element in a rotated search

**Suggested structure:**

```
binary-search-lib/
├── basic_search.py
├── first_last_occurrence.py
├── rotated_search.py
└── tests/
    └── test_binary_search.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
