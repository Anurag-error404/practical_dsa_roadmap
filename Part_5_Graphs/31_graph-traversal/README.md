# Graph Traversal Library (T1)

*Part 5 — Graphs*

## Problem

"Is there a path from A to B" and "are these all connected" need systematic traversal.

## Objective

Implement BFS, DFS, cycle detection, and connected-components on an adjacency-list graph.

---

**Input:** A graph as an adjacency list (nodes + edges, directed or undirected); a start node for BFS/DFS. **Output:** Traversal order; boolean for cycle detection; list of connected components.

**Edge cases:**

- A disconnected graph — traversal from one node won't reach every node, so full connected-component detection needs to loop over *all* nodes, not just start once
- Self-loops (a node with an edge to itself)
- Parallel edges (multiple edges between the same pair of nodes)
- Cycle detection differs between directed and undirected graphs — these need genuinely separate logic, not one function reused for both
- An empty graph, and a single node with no edges

**Suggested structure:**

```
graph-traversal/
├── graph.py                   # adjacency list representation
├── bfs.py
├── dfs.py
├── cycle_detection.py         # separate directed/undirected logic
├── connected_components.py
└── tests/
    └── test_traversal.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
