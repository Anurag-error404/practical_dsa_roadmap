# Shortest-Path Comparison (T1)

*Part 5 — Graphs*

## Problem

Dijkstra, Bellman-Ford, and Floyd-Warshall solve "shortest path" differently — the differences matter.

## Objective

Run all three on the same weighted graph; confirm they agree; time each.

---

**Input:** A weighted graph (possibly with negative weights, to exercise Bellman-Ford); a source node (and target, or none for Floyd-Warshall's all-pairs mode). **Output:** Shortest distances from source to all nodes (Dijkstra/Bellman-Ford); the full all-pairs distance matrix (Floyd-Warshall).

**Edge cases:**

- Negative edge weights fed to Dijkstra — Dijkstra assumes non-negative weights and will silently give a wrong answer; either reject negative weights explicitly or document the limitation
- A negative cycle present — Bellman-Ford must *detect and report* this, not return a plausible-looking but wrong finite distance
- A disconnected graph — unreachable nodes should report infinity/unreachable, not error
- A graph with a single node; self-loops with a weight attached

**Suggested structure:**

```
shortest-path-comparison/
├── graph.py
├── dijkstra.py          # heap-based
├── bellman_ford.py      # includes negative-cycle detection
├── floyd_warshall.py    # all-pairs
└── tests/
    └── test_shortest_path.py   # cross-checks all three agree where valid
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
