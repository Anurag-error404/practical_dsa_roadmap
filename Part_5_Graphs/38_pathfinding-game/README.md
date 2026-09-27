# Pathfinding Game (T2)

*Part 5 — Graphs*

## Problem

A game character needs to navigate around obstacles toward a goal, not walk through walls.

## Objective

Build a grid game where an NPC/player pathfinds live via Dijkstra or A\*.

---

**Input:** A grid with walls/obstacles, a start and goal cell; player input (interactive) or an automatic pathfinding trigger for an NPC. **Output:** The rendered grid with the computed path; live NPC movement toward the goal, recalculating if the path gets blocked.

**Edge cases:**

- No valid path exists between start and goal — this must be explicitly detected and communicated (e.g., an "unreachable" state), not leave the NPC frozen or the game crashed
- Start cell equals goal cell
- The player places a new obstacle mid-game that blocks the currently-computed path — must trigger a recompute, not keep following a now-invalid route
- A grid large enough that recomputing a full path every single frame is too slow — recompute only when necessary (path invalidated) or on a fixed tick, not every frame

**Suggested structure:**

```
pathfinding-game/
├── grid.py          # grid representation + obstacle placement
├── pathfinder.py    # A* or Dijkstra implementation
├── game_loop.py     # rendering + input handling
└── tests/
    └── test_pathfinder.py   # unreachable-goal case, explicitly
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
