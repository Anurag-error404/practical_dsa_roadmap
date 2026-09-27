# Complexity Benchmark Harness (T1)

*Part 1 — Foundations*

## Problem

You've read that O(n²) is "slow," but never watched it actually fail at scale.

## Objective

Implement the same task two ways; measure real runtime at 10³/10⁵/10⁷ inputs; plot the curve.

---

**Input:** Two function implementations solving the same task (e.g., dedupe) — one O(n²), one O(n) — plus a list of input sizes to test at. **Output:** A table of `(input_size, algorithm, time_ms)` rows; optionally a rendered chart.

**Edge cases:**

- Input size large enough that the O(n²) version would take minutes — needs a timeout or size cap for that algorithm only
- Single-run timing noise (JIT/cache warm-up) — take multiple trials, report median
- Empty input (size 0) — should still run without error
- Input sizes not in increasing order

**Suggested structure:**

```
complexity-bench/
├── algorithms/
│   ├── naive_dedupe.py       # O(n²) version
│   └── hash_dedupe.py        # O(n) version
├── bench.py                  # runs each algo across sizes, records timing
├── results.csv
└── plot.py                   # optional: renders the growth curve
```

---

## Scaffold notes

- Added `tests/test_bench.py`; the suggested structure has no tests folder.
- `bench.py` and `plot.py` use the shared timing harness in `../_shared/bench_harness.py`.

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
