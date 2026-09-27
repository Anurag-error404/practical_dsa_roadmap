# LCS/LIS With Reconstruction (T1)

*Part 6 — Dynamic Programming*

## Problem

Knowing the *length* of the longest common subsequence isn't the same as knowing *what it is*.

## Objective

Implement LCS and LIS, and reconstruct the actual sequence, not just its length.

---

**Input:** Two strings (LCS), or one array of numbers (LIS). **Output:** The length of the LCS/LIS, *and* the actual subsequence itself.

**Edge cases:**

- One or both inputs empty — result is empty, length 0 (not `None`/an error)
- No common subsequence at all between two strings — still returns an explicit empty result
- LIS on a strictly decreasing array — longest increasing subsequence has length 1
- LIS with duplicate values — decide strictly-increasing vs. non-decreasing and be consistent, since this changes the answer
- Multiple LCS/LIS of the same max length exist — only one is needed, but it must be programmatically verified as an actual valid subsequence of the input, not just a length match

**Suggested structure:**

```
lcs-lis/
├── lcs.py   # DP table + backtrack reconstruction
├── lis.py   # O(n log n) or O(n²) + reconstruction
└── tests/
    └── test_reconstruction.py   # verifies reconstructed sequence is genuinely valid
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
