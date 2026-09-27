# Real-Time Analytics Backend (T2)

*Part 8 — Advanced Topics*

## Problem

A live dashboard needs "sum between time A and B" answered fast on constantly-changing data.

## Objective

Build a backend answering range-aggregate queries over a streaming metric feed.

---

**Input:** A stream of `(timestamp, metric_value)` events; range queries like "sum/min/max between time A and B." **Output:** Query results computed efficiently even as new events keep arriving.

**Edge cases:**

- A query range containing no events — return a sensible default (0 for sum; explicit null/error for min/max of an empty set), not a crash
- Events arriving out of chronological order — decide whether to accept and re-index, or reject late data
- High event throughput requiring efficient point updates without full structure rebuilds
- A query range extending into the future (no data there yet) — return what's available, not an error

**Suggested structure:**

```
realtime-analytics/
├── ingest.py         # receives events, updates the underlying structure
├── fenwick_tree.py   # reused/adapted from Project 52
├── query_api.py      # range query endpoint
└── tests/
    └── test_analytics.py   # out-of-order arrival, empty-range query
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
