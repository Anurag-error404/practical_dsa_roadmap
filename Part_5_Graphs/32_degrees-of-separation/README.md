# Degrees-of-Separation Tool (T2)

*Part 5 — Graphs*

## Problem

"How is person A connected to person B" isn't answerable by inspection on a real network.

## Objective

Given a friend-graph dataset, compute shortest connection path via BFS.

---

**Input:** A friend-graph dataset (edges as pairs); two user IDs to query. **Output:** The shortest path length (degrees) between them, and the path itself.

**Edge cases:**

- The two users are the same person — degree 0
- No path exists (they're in disconnected parts of the graph) — report "not connected" explicitly, don't error or loop forever
- A graph large enough that naive re-scans per query are too slow — BFS should be efficient, not O(V²)
- Multiple shortest paths of equal length — only one needs to be returned, but the choice should be deterministic and reproducible

**Suggested structure:**

```
degrees-of-separation/
├── graph_loader.py   # loads edges into an adjacency list
├── bfs_path.py        # shortest path + degree count
├── cli.py             # query interface
└── tests/
    └── test_bfs_path.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
