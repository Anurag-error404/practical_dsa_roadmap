# Bitmask Utility Set (T1)

*Part 8 — Advanced Topics*

## Problem

Storing 8 boolean flags as 8 separate variables wastes space and is error-prone to check.

## Objective

Implement subset generation, single-number-finder, and bit-counting via bitmasks.

---

**Input:** Integers for bit operations; a set of elements for bitmask-based subset generation. **Output:** All subsets (via bitmask iteration); the single non-duplicate number in an array; the bit count of a number.

**Edge cases:**

- Empty input set — subset generation should still yield exactly one subset, the empty set
- Very large integers relative to fixed bit-width assumptions (matters especially in 32-bit vs. 64-bit contexts)
- Negative numbers and two's-complement effects on bitwise operations
- Single-number problem given input that violates its precondition (more than one number appears an odd number of times) — document this as an assumption rather than silently returning a wrong answer

**Suggested structure:**

```
bitmask-utils/
├── subset_generator.py   # bitmask iteration, 0 to 2^n - 1
├── single_number.py      # XOR trick
├── bit_counter.py        # Brian Kernighan's algorithm
└── tests/
    └── test_bitmask.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
