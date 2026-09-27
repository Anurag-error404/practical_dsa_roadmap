# Sort Algorithm Bench (T1)

*Part 3 — Core Algorithmic Patterns*

## Problem

"Which sort is fastest" depends entirely on the data — nobody believes this until they measure it.

## Objective

Implement merge/quick/heap/counting sort; benchmark each on random vs. nearly-sorted input.

---

**Input:** An unsorted array; a chosen algorithm (merge/quick/heap/counting); a data distribution to test against (random, nearly-sorted, reverse-sorted, all-duplicates). **Output:** The sorted array; timing per algorithm per distribution.

**Edge cases:**

- Already-sorted input fed to a naive quicksort with a poor (e.g., first-element) pivot choice — this is the classic worst-case that degrades to O(n²) and can even stack-overflow a recursive implementation
- An array where every element is identical
- Counting sort given a huge value range relative to array size — memory blows up; document that counting sort needs a *bounded* range to be viable
- Empty array, and array of size 1

**Suggested structure:**

```
sort-bench/
├── algorithms/
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── heap_sort.py
│   └── counting_sort.py
├── bench.py                    # runs all algos across all distributions
└── tests/
    └── test_correctness.py     # verifies sorted output for every algorithm
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
