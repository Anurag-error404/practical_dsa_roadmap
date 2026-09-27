# Ride/Job Matching Simulator (T2)

*Part 8 — Advanced Topics*

## Problem

Assigning many requests to many resources (riders↔drivers, tasks↔workers) needs more than first-come-first-served.

## Objective

Build a simulator that matches requests to resources via bipartite matching or greedy assignment.

---

**Input:** A set of riders/tasks and drivers/workers, each with attributes (location, availability, skill); a matching request. **Output:** An assignment of riders to drivers (or tasks to workers), optimizing for some criteria (distance, wait time, match count).

**Edge cases:**

- More riders/tasks than available drivers/workers — some requests go unmatched; this must be reported explicitly, not silently dropped
- A driver/worker with no compatible match at all (skill or location mismatch) — reported as idle, not an error
- Ties in matching quality — the algorithm should pick one assignment deterministically, not arbitrarily
- A driver/worker becoming unavailable mid-simulation — decide whether already-assigned-but-not-started matches need to be re-matched

**Suggested structure:**

```
ride-job-matching/
├── models.py       # Rider/Driver or Task/Worker schema
├── matcher.py      # bipartite matching (greedy or Hopcroft-Karp)
├── simulator.py    # runs matching over simulated requests
└── tests/
    └── test_matching.py   # unmatched-request reporting, tie handling
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
