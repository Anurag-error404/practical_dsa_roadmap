# Friend-Circles / Image Regions (T2)

*Part 5 — Graphs*

## Problem

Determining which users (or pixels) form a connected group needs fast grouping, not per-pair checks.

## Objective

Detect friend groups in a social graph, or connected regions in a simple 2D image grid.

---

Two directions for this slot — pick one:

### Direction A: Friend Circles

**Input:** Adjacency list/matrix of friendships. **Output:** Number of distinct friend groups, and the members of each.

### Direction B: Image Regions

**Input:** A 2D grid of pixel values (e.g., 0/1 for background/foreground). **Output:** Number of connected regions, and the pixels belonging to each.

**Edge cases (both directions):**

- A fully disconnected input — every person/pixel is its own group
- A fully connected input — one single giant group
- *(Image)* Diagonal adjacency vs. only up/down/left/right — decide and document which counts as "connected," since this materially changes the region count
- An empty input grid or graph

**Suggested structure:**

```
friend-circles-or-regions/
├── union_find.py       # reused from Project 35
├── graph_builder.py    # (or grid_scanner.py for the image variant)
├── region_counter.py
└── tests/
    └── test_regions.py   # adjacency rule, explicitly, for the image variant
```

---

## Run

Run inside the direction folder you keep:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../../_shared python <script>.py`.

This slot has two directions (`A_friend-circles/`, `B_image-regions/`). Pick one and delete the other.
