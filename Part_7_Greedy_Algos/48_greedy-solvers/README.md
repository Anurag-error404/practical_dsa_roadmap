# Greedy Solver Set (T1)

*Part 7 — Greedy Algorithms*

## Problem

Some optimization problems have a provably-correct "always pick the best option now" shortcut.

## Objective

Implement activity selection, Huffman coding, and fractional knapsack.

---

**Input:** Activity `(start, end)` list (activity selection); character frequencies (Huffman coding); item weight/value pairs + capacity, with fractional items allowed (fractional knapsack). **Output:** Max non-overlapping activities selected; a Huffman code per character; max achievable value (fractional knapsack allows partial items).

**Edge cases:**

- Activities with identical start/end times — need a consistent tie-break rule (typically: sort by end time, then start time)
- An activity ending exactly when another starts — decide whether this counts as overlapping (inclusive) or not (exclusive), and document it
- A single distinct character for Huffman — same degenerate-tree issue as the compressor project; needs explicit handling
- Fractional knapsack items with identical value-to-weight ratio — order doesn't matter, but total value must still be correct
- Capacity of 0

**Suggested structure:**

```
greedy-solvers/
├── activity_selection.py
├── huffman_coding.py
├── fractional_knapsack.py
└── tests/
    └── test_greedy.py   # boundary-overlap case, explicitly
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
