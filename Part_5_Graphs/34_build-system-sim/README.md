# Build-System Simulator (T2)

*Part 5 — Graphs*

## Problem

A dependency file needs to become a valid, deterministic execution order.

## Objective

Read task dependencies from a file; output a valid build order (or report a cycle).

---

**Input:** A dependency spec (task → list of tasks it depends on). **Output:** A valid execution order, or a reported circular dependency showing which tasks are involved.

**Edge cases:**

- A circular dependency — report *which tasks* form the cycle, not just "a cycle exists somewhere"
- A task listed as a dependency but never itself defined — decide whether this is an error or gets auto-included as a no-op task
- Duplicate dependency declarations for the same pair
- A fully independent task with no dependencies and nothing depending on it — should still appear in the output, order-agnostic

**Suggested structure:**

```
build-system-sim/
├── parser.py           # reads the dependency spec file
├── topo_sort.py         # reused from Project 33
├── cycle_reporter.py     # extracts and displays the actual cycle path
└── tests/
    └── test_build_order.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
