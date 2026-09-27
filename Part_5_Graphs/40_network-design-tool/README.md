# Network Design Tool (T2)

*Part 5 — Graphs*

## Problem

Given cities and cable costs, wiring everything to everything is needlessly expensive.

## Objective

Given nodes + edge costs, output the minimum-cost way to connect all of them.

---

**Input:** A list of cities/nodes + candidate connection costs between pairs. **Output:** The minimum-cost set of connections that links every city, and the total cost.

**Edge cases:**

- Some city pairs have no possible direct connection — MST must be computed using only the available edges, or the tool must report that full connectivity isn't achievable
- A city with no viable connection to anywhere — an isolated node, report this explicitly rather than silently omitting it
- Ties in total cost between multiple valid network designs
- A very large number of cities making a true all-pairs candidate edge list impractical — generate candidate edges more selectively (e.g., k-nearest neighbors) rather than every possible pair

**Suggested structure:**

```
network-design-tool/
├── city_loader.py
├── cost_model.py    # computes/loads edge costs
├── mst.py           # reused from Project 39
├── report.py        # outputs chosen connections + total cost
└── tests/
    └── test_network_design.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
