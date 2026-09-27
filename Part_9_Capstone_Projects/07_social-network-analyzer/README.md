# Social Network Analyzer

*Type 3 — Capstones*

## Problem

A friend-graph hides its structure — who's central, who's clustered, who's how far apart.

## Objective

Compute degrees of separation, detect friend clusters, and rank most-connected users on a real graph dataset.

---

**Combines:** Graphs + BFS · Union-Find · Heaps

**Input:** A friend-graph dataset (edges); `degrees_of_separation(a, b)`, `friend_groups()`, `most_connected(k)`. **Output:** Shortest path/degree count; distinct friend clusters; top-K most-connected users.

**Edge cases:**

- A user with zero friends — an isolated node, which is technically its own friend group of size 1
- The entire graph being one single connected component — only one friend group exists at all
- Ties in "most connected" right at the k-th position — decide whether to include all ties or strictly cap at k
- A graph large enough that repeated from-scratch BFS on every query is noticeably slow — decide whether that's acceptable or whether some precomputation is warranted

**Suggested structure:**

```
social-network-analyzer/
├── graph_loader.py
├── bfs_degrees.py   # shortest path / degrees of separation
├── union_find.py    # friend cluster detection
├── heap_topk.py      # most-connected users
└── tests/
    └── test_analyzer.py   # isolated node, single-giant-component case
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
