# Smart Task Manager

*Type 3 — Capstones*

## Problem

Tasks have priorities *and* dependencies *and* deadlines — no single structure handles all three.

## Objective

Build a task manager where urgent tasks surface first, blocked tasks wait for dependencies, and conflicts get resolved automatically.

---

**Combines:** Hashing · Heaps · Topological Sort · Greedy

**Input:** `create_task(name, priority, dependencies=[], deadline=None)`, `complete_task(id)`, `get_next_task()`. **Output:** The next task to work on (highest priority among currently-unblocked tasks); a report of blocked/overdue tasks.

**Edge cases:**

- A task depending on itself — a self-cycle, must be detected and rejected at creation, not discovered later
- A circular dependency across multiple tasks (A→B→A) — detect via cycle check before allowing the dependency to be added, not just at query time
- Completing a task that others depend on — verify dependents actually get unblocked and become eligible for `get_next_task()`
- Two unblocked tasks tied on priority — needs a defined tie-break (deadline, then creation order)
- A deadline set in the past at creation time — decide whether this is allowed, auto-flagged as overdue, or rejected

**Suggested structure:**

```
smart-task-manager/
├── models.py             # Task schema (id, priority, deps, deadline, status)
├── dependency_graph.py   # topological sort + cycle detection
├── priority_queue.py     # heap of ready (unblocked) tasks
├── scheduler.py          # unblocks deps on completion, feeds heap
└── tests/
    └── test_scheduler.py   # circular dependency rejection, unblock propagation
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
