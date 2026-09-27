# MST Implementation (T1)

*Part 5 — Graphs*

## Problem

Connecting all nodes cheaply isn't the same as connecting them at all.

## Objective

Implement Prim's and Kruskal's; verify both produce the same total minimum cost.

---

**Input:** A weighted, undirected, connected graph. **Output:** The set of edges forming the MST, and its total cost.

**Edge cases:**

- A disconnected graph — no single spanning tree exists; detect this and either return a minimum spanning forest or an explicit error, rather than a partial/wrong tree
- Duplicate-weight edges — multiple valid MSTs may exist with the same total cost; any one is acceptable, but total cost must be correct
- A graph with only one node — trivial MST, no edges, cost 0
- Prim's and Kruskal's must agree on total cost, even when they select different edges to get there

**Suggested structure:**

```
mst/
├── graph.py
├── prims.py       # heap-based
├── kruskals.py    # union-find based, sorts edges by weight
└── tests/
    └── test_mst.py   # verifies matching total cost between both algorithms
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
