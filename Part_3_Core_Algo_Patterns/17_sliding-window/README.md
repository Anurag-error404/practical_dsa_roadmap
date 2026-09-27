# Sliding-Window Solver Set (T1)

*Part 3 — Core Algorithmic Patterns*

## Problem

Recomputing a window sum/count from scratch each shift is wasteful.

## Objective

Solve max-subarray-sum and longest-substring-without-repeats in O(n).

---

**Input:** An array + window size k (max-sum-subarray), or a string (longest-substring-without-repeats). **Output:** The max sum (number), or the length/actual substring.

**Edge cases:**

- k larger than the array length — no valid window exists
- Empty array or empty string
- All identical elements (max sum is trivial; longest-no-repeat substring has length 1)
- k = 0 or k equal to the full array length exactly

**Suggested structure:**

```
sliding-window/
├── max_sum_subarray.py
├── longest_substring_no_repeat.py
└── tests/
    └── test_sliding_window.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
