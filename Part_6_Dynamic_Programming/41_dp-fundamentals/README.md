# DP Fundamentals Bench (T1)

*Part 6 — Dynamic Programming*

## Problem

Naive recursive Fibonacci/coin-change recomputes the same subproblem exponentially many times.

## Objective

Implement memoized and tabulated versions; benchmark against naive recursion at n=35+.

---

**Input:** `n` (Fibonacci, climbing stairs), or a coin denomination list + target amount (coin change). **Output:** The computed value (nth Fibonacci number, ways to climb, minimum coins needed); timing comparison against naive recursion.

**Edge cases:**

- n = 0 or n = 1 — base cases that are easy to get subtly wrong
- Negative n — invalid input, should be rejected explicitly
- Coin change where no valid combination reaches the target — return -1/"impossible," don't crash
- n large enough that naive recursion would hang for minutes — cap or timeout the naive version specifically when benchmarking
- Duplicate denominations in the coin list

**Suggested structure:**

```
dp-fundamentals/
├── naive_recursive.py   # baseline, exponential
├── memoized.py          # top-down with cache
├── tabulated.py         # bottom-up
├── bench.py
└── tests/
    └── test_dp_basics.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
