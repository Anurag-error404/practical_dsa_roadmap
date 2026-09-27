# Budget Allocator (T2)

*Part 6 — Dynamic Programming*

## Problem

A team has limited budget and more good ideas than it can fund.

## Objective

Given projects with cost + value, output the value-maximizing subset within budget.

---

**Input:** A list of projects, each with `(cost, value)`; a total budget. **Output:** The subset of projects to fund that maximizes total value within budget, plus leftover unused budget.

**Edge cases:**

- A single project costing more than the entire budget — must be excluded from consideration
- Multiple projects with identical cost and value — any valid optimal selection is fine, but total value must be exactly correct
- Budget of 0 — fund nothing, don't error
- Multiple different subsets tying at the same max value — the tool should return one *consistently*, not vary between runs on the same input

**Suggested structure:**

```
budget-allocator/
├── models.py            # Project schema (cost, value)
├── knapsack_solver.py   # reused from Project 42
├── report.py            # shows selected projects + leftover budget
└── tests/
    └── test_allocator.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
