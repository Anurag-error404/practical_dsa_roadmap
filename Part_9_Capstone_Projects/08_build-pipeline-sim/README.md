# Build Pipeline Simulator

*Type 3 — Capstones*

## Problem

Build tasks with dependencies waste time if run sequentially when some could run in parallel.

## Objective

Compute valid execution order, detect independent task groups, and maximize parallel scheduling.

---

**Combines:** Topological Sort · Graphs · Union-Find · Greedy

**Input:** A task dependency spec; the number of available parallel workers. **Output:** An execution schedule showing which tasks run in which round (parallel batch); total time given per-task duration.

**Edge cases:**

- A circular dependency — must be detected and reported *before* attempting to build any schedule
- More independent, ready tasks at once than available workers — the excess must queue for the next round, not all run simultaneously beyond capacity
- A task with zero duration — should schedule and complete instantly without breaking the timing math
- A pipeline that's fully sequential (no parallelism possible at all) — should still complete correctly, just with worker utilization of 1 throughout

**Suggested structure:**

```
build-pipeline-sim/
├── parser.py         # reads the dependency spec
├── topo_sort.py      # validates DAG, detects cycles
├── union_find.py     # identifies independent task groups (optional optimization)
├── scheduler.py      # assigns tasks to worker-rounds, respecting deps + capacity
└── tests/
    └── test_pipeline.py   # cycle detection, worker-capacity overflow case
```

---

## Scaffold notes

- `models.py` holds the dataclasses shared across modules, so every module speaks the same types.

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
