# Real-Time Analytics Dashboard

*Type 3 — Capstones*

## Problem

A live stream of events needs instant rolling metrics *and* historical range queries, without re-scanning everything.

## Objective

Build a dashboard showing rolling window metrics, range-aggregate queries, and live top-K trending items.

---

**Combines:** Sliding Window · Segment/Fenwick Tree · Heaps · Hashing

**Input:** Streaming events `(timestamp, user_id, event_type, value)`; `rolling_metric(window)`, `range_query(start, end)`, `top_k_trending(k)`. **Output:** Live-updating rolling metrics; historical range aggregates; current top-K trending items.

**Edge cases:**

- A query window/range containing zero events — return a defined default, not an error
- An event arriving with a timestamp *earlier* than already-processed data (late/out-of-order arrival) — decide whether to accept and re-index or reject, and document the choice, since it affects both the rolling window and range-query correctness
- Extremely high event throughput — the rolling-window (deque) and range-query (Fenwick tree) structures both need fast updates without bottlenecking each other
- Fewer than K distinct items exist so far for trending — return what's available, don't pad with empty entries

**Suggested structure:**

```
realtime-dashboard/
├── event_ingest.py    # receives + routes events to relevant structures
├── sliding_window.py  # rolling metrics (monotonic deque)
├── fenwick_tree.py    # range-query aggregates
├── trending_heap.py   # top-K trending via heap + hash map
├── dashboard_api.py
└── tests/
    └── test_dashboard.py   # out-of-order event handling, cross-structure consistency
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
