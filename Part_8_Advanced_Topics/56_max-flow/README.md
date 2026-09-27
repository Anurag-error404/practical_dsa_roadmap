# Basic Max-Flow (T1)

*Part 8 — Advanced Topics*

## Problem

"How much can flow through this network given capacity limits" isn't answerable by inspection.

## Objective

Implement Ford-Fulkerson; verify max-flow equals min-cut on a small test graph.

---

**Input:** A directed graph with edge capacities; source and sink nodes. **Output:** The maximum flow value from source to sink; the min-cut edges.

**Edge cases:**

- Source equals sink — degenerate case, should be rejected as invalid input
- No path exists from source to sink at all — max flow is 0
- A graph containing cycles — Ford-Fulkerson must handle this correctly via the residual graph, not loop forever
- Zero-capacity edges — should behave as if the edge doesn't exist
- Verify max-flow value equals min-cut capacity (the max-flow min-cut theorem) as a built-in correctness check

**Suggested structure:**

```
max-flow/
├── graph.py             # capacities + residual graph
├── ford_fulkerson.py    # BFS-based (Edmonds-Karp) for guaranteed termination
├── min_cut.py           # derives min-cut from the final residual graph
└── tests/
    └── test_max_flow.py   # max-flow == min-cut verification
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
