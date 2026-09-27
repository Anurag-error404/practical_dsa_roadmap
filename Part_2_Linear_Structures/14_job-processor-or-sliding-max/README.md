# Job Processor / Sliding-Max Dashboard (T2)

*Part 2 — Linear Structures*

## Problem

Tasks arrive faster than they can run, or you need the max over a moving window.

## Objective

Build a priority-aware job queue, or a live dashboard showing max-in-last-N-events.

---

Two directions for this slot — pick one:

### Direction A: Priority Job Processor

**Input:** `submit_job(priority)`, `process_next()`. **Output:** Jobs processed in priority order (highest first).

**Edge cases:**

- Multiple jobs with the same priority — decide tie-breaking (typically FIFO among equal priority)
- `process_next()` on an empty queue
- A job's priority changing after submission (priority queues don't support update-in-place natively — you'd need a workaround, e.g. lazy deletion)

**Suggested structure:**

```
job-processor/
├── job_queue.py         # heap-based priority queue
└── tests/
    └── test_priority_order.py   # tie-breaking behavior specifically
```

### Direction B: Sliding-Window-Max Dashboard

**Input:** A stream of `(timestamp, value)` events + a window size N. **Output:** The current max value within the last N events (or last N seconds).

**Edge cases:**

- Fewer than N events have arrived yet — the window is partial, not an error
- A value that was the max *leaves* the window — it must be evicted from the internal deque even though it's still the largest value seen overall
- Duplicate max values in the window — the deque needs to handle ties correctly on eviction, not just distinct values

**Suggested structure:**

```
sliding-max-dashboard/
├── sliding_window_max.py   # monotonic deque
├── stream_simulator.py     # generates the event feed for testing
└── tests/
    └── test_window_max.py
```

---

## Run

Run inside the direction folder you keep:

```bash
pip install -r requirements.txt
pytest
```

This slot has two directions (`A_job-processor/`, `B_sliding-max-dashboard/`). Pick one and delete the other.
