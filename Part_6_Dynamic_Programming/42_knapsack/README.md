# Knapsack Solvers (T1)

*Part 6 — Dynamic Programming*

## Problem

Choosing items under a hard capacity constraint isn't solvable by sorting alone.

## Objective

Implement 0/1 knapsack and unbounded knapsack; verify against brute force on small cases.

---

**Input:** Item weights + values, capacity W; a flag for 0/1 vs. unbounded. **Output:** Max achievable value; optionally, the selected item set.

**Edge cases:**

- Capacity 0 — no items fit, value 0
- A single item heavier than the entire capacity — must be excluded, not crash
- All items with zero weight — value could be "unbounded" in a naive model; this degenerate case is worth flagging explicitly rather than silently mishandling
- Empty item list
- Unbounded knapsack: verify the capacity constraint is respected even when the same high-value/low-weight item is theoretically selectable many times over

**Suggested structure:**

```
knapsack/
├── knapsack_01.py
├── knapsack_unbounded.py
├── reconstruct_selection.py   # traces back which items were chosen
└── tests/
    └── test_knapsack.py       # verify against brute force on small cases
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
