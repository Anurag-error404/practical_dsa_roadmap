# Pathfinding Game with Procedural Mazes

*Type 3 — Capstones*

## Problem

A game world needs to be different every playthrough, and its inhabitants need to navigate it intelligently.

## Objective

Build a game with procedurally generated mazes and an NPC that pathfinds around the player in real time.

---

**Combines:** Backtracking · Graphs + Dijkstra/A\* · Heaps · BFS

**Input:** A seed for maze generation; player movement input; NPC spawn point. **Output:** A rendered maze; NPC path recalculated live as the player moves or blocks a route.

**Edge cases:**

- Maze generation must *guarantee* full connectivity — verify with a BFS reachability check post-generation, every playable cell reachable from the start
- NPC and player landing on the same cell — decide the collision rule explicitly
- The player blocking the maze in a way that fully disconnects the NPC from its goal — must detect this "no path" state and handle it gracefully (NPC waits, or moves to nearest reachable point), not crash
- A maze large enough that per-frame full pathfinding lags — only recompute when the path is actually invalidated, not every frame
- Multiple equally-short paths existing — the NPC shouldn't flicker between them frame to frame

**Suggested structure:**

```
pathfinding-game/
├── maze_generator.py   # randomized DFS/Prim's-based, backtracking
├── maze_validator.py   # BFS reachability check
├── pathfinder.py       # A*/Dijkstra with incremental recompute
├── npc.py              # NPC state machine, path-following
├── game_loop.py        # rendering + input
└── tests/
    └── test_maze_and_pathing.py   # connectivity guarantee, path invalidation on block
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
