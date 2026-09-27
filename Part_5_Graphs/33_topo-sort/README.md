# Topological Sort (T1)

*Part 5 — Graphs*

## Problem

Some tasks must run before others — an arbitrary order breaks dependencies.

## Objective

Implement topo sort via Kahn's algorithm and via DFS; detect impossible (cyclic) orderings.

---

**Input:** A DAG as an adjacency list or edge list of dependencies. **Output:** A valid topological order, or a clear cycle-detected report if the graph isn't actually a DAG.

**Edge cases:**

- A cycle present — must be detected and reported, not silently produce a wrong or partial ordering
- Multiple valid topological orders exist — any one is acceptable, but verify it by checking every edge points forward in the output order
- Disconnected components within the same graph — every node must still appear in the final order
- A node with no edges at all (isolated)

**Suggested structure:**

```
topo-sort/
├── graph.py
├── kahns_algorithm.py   # BFS-based, in-degree tracking
├── dfs_based.py         # DFS + stack-based approach
└── tests/
    └── test_topo_sort.py   # cycle detection, explicitly
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
