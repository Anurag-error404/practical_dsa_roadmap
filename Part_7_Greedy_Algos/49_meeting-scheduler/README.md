# Meeting-Room Scheduler (T2)

*Part 7 — Greedy Algorithms*

## Problem

Overlapping meeting requests need the maximum non-conflicting subset selected automatically.

## Objective

Given meeting time ranges, output the max number schedulable without conflict.

---

**Input:** A list of meeting requests, each with `(start, end)`, possibly a priority. **Output:** The maximum set of meetings schedulable without conflict; the list of rejected meetings.

**Edge cases:**

- Back-to-back meetings (one ends exactly when the next starts) — decide whether this is allowed
- Meetings with equal start times
- A duplicate meeting request
- A large volume of meetings needing the efficient greedy approach (sort by end time) rather than brute-force checking every combination
- Invalid time ranges (end before start) — should be rejected outright

**Suggested structure:**

```
meeting-scheduler/
├── models.py           # Meeting(start, end, priority)
├── scheduler.py        # greedy interval scheduling
├── conflict_checker.py
└── tests/
    └── test_scheduler.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
