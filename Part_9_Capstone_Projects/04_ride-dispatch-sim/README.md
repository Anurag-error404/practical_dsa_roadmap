# Ride-Sharing Dispatch Simulator

*Type 3 — Capstones*

## Problem

Matching riders to drivers needs both "who's closest" and "who's actually reachable fastest."

## Objective

Simulate dispatch: nearest-driver lookup, real ETA via shortest-path, and rider-driver assignment.

---

**Combines:** Graphs · Dijkstra · Heaps · Bipartite Matching/Greedy

**Input:** A city road network (graph); driver locations + availability; ride requests (pickup, dropoff). **Output:** Matched driver per request with computed route + ETA; a report of unmatched requests.

**Edge cases:**

- No available driver within a reasonable radius — report as unmatched with a reason, don't silently drop the request
- Multiple requests competing for the same nearest driver — resolve deterministically (e.g., request-arrival order)
- A driver going offline mid-assignment — an in-progress ride shouldn't be disrupted, but future matching must exclude them immediately
- A rider and all drivers sitting in a disconnected region of the road network — report unreachable, don't hang trying to compute a nonexistent path

**Suggested structure:**

```
ride-dispatch-sim/
├── road_network.py   # graph representation of the city
├── dijkstra.py        # ETA/route computation
├── driver_pool.py       # heap/spatial index of available drivers by proximity
├── matcher.py             # assignment logic (greedy nearest-available or bipartite matching)
├── simulator.py             # drives the whole simulation over time
└── tests/
    └── test_dispatch.py         # unmatched-request reporting, disconnected-network case
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
