# DSA Project Specs — Capstones 1–5

*Full spec for each multi-concept capstone: input/output format, edge cases, suggested file structure*

These combine several concepts each — the edge cases below are deliberately the ones that live at the *seams* between subsystems, since that's where capstone bugs actually happen.

---

## Capstone 1: Smart Task Manager

**Combines:** Hashing · Heaps · Topological Sort · Greedy

**Input:** `create_task(name, priority, dependencies=[], deadline=None)`, `complete_task(id)`, `get_next_task()`. **Output:** The next task to work on (highest priority among currently-unblocked tasks); a report of blocked/overdue tasks.

**Edge cases:**

- A task depending on itself — a self-cycle, must be detected and rejected at creation, not discovered later
- A circular dependency across multiple tasks (A→B→A) — detect via cycle check before allowing the dependency to be added, not just at query time
- Completing a task that others depend on — verify dependents actually get unblocked and become eligible for `get_next_task()`
- Two unblocked tasks tied on priority — needs a defined tie-break (deadline, then creation order)
- A deadline set in the past at creation time — decide whether this is allowed, auto-flagged as overdue, or rejected

**Suggested structure:**

```
smart-task-manager/
├── models.py             # Task schema (id, priority, deps, deadline, status)
├── dependency_graph.py   # topological sort + cycle detection
├── priority_queue.py     # heap of ready (unblocked) tasks
├── scheduler.py          # unblocks deps on completion, feeds heap
└── tests/
    └── test_scheduler.py   # circular dependency rejection, unblock propagation
```

---

## Capstone 2: Mini Search Engine

**Combines:** Tries · Hashing · KMP/Rabin-Karp · Heaps · Sorting

**Input:** A document set to index; `query(text)` — phrase or keyword. **Output:** Ranked matching documents with snippet/match locations.

**Edge cases:**

- A query term appearing in zero documents — return empty, not an error
- A query mixing an exact phrase with loose keywords — decide how these combine (must-match phrase + optional keyword boost, or something simpler)
- A document set large enough that the inverted index must be built incrementally rather than all at once
- Autocomplete for a prefix with zero matches — empty list, not an error
- Two documents tied on relevance score — needs a defined tie-break for stable ranking

**Suggested structure:**

```
mini-search-engine/
├── indexer.py       # inverted index (hashing)
├── trie.py          # autocomplete over indexed terms
├── matcher.py       # KMP/Rabin-Karp for exact phrase matching within candidates
├── ranker.py        # heap-based top-K relevance ranking
├── query_api.py
└── tests/
    └── test_search_engine.py   # index + ranking + autocomplete together
```

---

## Capstone 3: Pathfinding Game with Procedural Mazes

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

## Capstone 4: Ride-Sharing Dispatch Simulator

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

## Capstone 5: Code Editor Core

**Combines:** Linked Lists/Rope · Stacks · Tries · String Matching

**Input:** Text edits (insert/delete at cursor); `undo()`; `redo()`; `find(text)`; `replace(text, new_text)`. **Output:** Current buffer content; undo/redo result; find match positions; replace count.

**Edge cases:**

- Undo used, then a *new* edit is made — the redo stack must be cleared (same rule as the browser-history project), not left stale
- `find()` on an empty buffer or with an empty search string
- Replace-all where the replacement text itself contains the search text — a naive "find-and-replace repeatedly" approach can loop forever; must be done in a single pass over the original positions
- A file large enough that a plain array-based buffer is slow for mid-document inserts — worth documenting this trade-off even if you choose a simpler structure over a full rope
- Autocomplete triggering on a partial word with zero dictionary matches

**Suggested structure:**

```
code-editor-core/
├── text_buffer.py   # linked-list/rope-based buffer
├── undo_redo.py     # two-stack undo/redo, invalidated on new edit
├── trie.py          # autocomplete for known identifiers/words
├── search.py        # find/replace using string matching
└── tests/
    └── test_editor_core.py   # undo-after-redo-invalidation case, explicitly
```

---

## Capstone 6: E-Commerce Catalogue Engine

**Combines:** Hashing · BST/Trees · Two Pointers/Sliding Window · Sorting · Knapsack DP

**Input:** A product catalogue (category, price, rating, etc.); `browse(category)`, `filter(price_range)`, `sort(criteria)`, `bundle_suggest(budget)`. **Output:** Filtered/sorted product list; a bundle recommendation within budget maximizing value.

**Edge cases:**

- A category with no products — empty result, not an error
- A price filter where min > max — invalid input, reject explicitly
- Sorting by a field some products are missing — decide where nulls sort (first, last, or excluded) and be consistent
- A bundle request where no combination fits the budget — return an empty bundle with a clear message, not an error
- A product belonging to multiple categories — decide whether the category structure is a strict tree (one parent) or a more general graph, since this changes your data model entirely

**Suggested structure:**

```
ecommerce-catalogue/
├── category_tree.py     # tree or graph, depending on multi-category decision
├── product_store.py     # hashing for product lookup
├── filter_sort.py       # two-pointer/sliding-window range filter + multi-key sort
├── bundle_optimizer.py  # knapsack-based bundle suggestion
└── tests/
    └── test_catalogue.py   # multi-category handling, no-fit bundle case
```

---

## Capstone 7: Social Network Analyzer

**Combines:** Graphs + BFS · Union-Find · Heaps

**Input:** A friend-graph dataset (edges); `degrees_of_separation(a, b)`, `friend_groups()`, `most_connected(k)`. **Output:** Shortest path/degree count; distinct friend clusters; top-K most-connected users.

**Edge cases:**

- A user with zero friends — an isolated node, which is technically its own friend group of size 1
- The entire graph being one single connected component — only one friend group exists at all
- Ties in "most connected" right at the k-th position — decide whether to include all ties or strictly cap at k
- A graph large enough that repeated from-scratch BFS on every query is noticeably slow — decide whether that's acceptable or whether some precomputation is warranted

**Suggested structure:**

```
social-network-analyzer/
├── graph_loader.py
├── bfs_degrees.py   # shortest path / degrees of separation
├── union_find.py    # friend cluster detection
├── heap_topk.py      # most-connected users
└── tests/
    └── test_analyzer.py   # isolated node, single-giant-component case
```

---

## Capstone 8: Build Pipeline Simulator

**Combines:** Topological Sort · Graphs · Union-Find · Greedy

**Input:** A task dependency spec; the number of available parallel workers. **Output:** An execution schedule showing which tasks run in which round (parallel batch); total time given per-task duration.

**Edge cases:**

- A circular dependency — must be detected and reported *before* attempting to build any schedule
- More independent, ready tasks at once than available workers — the excess must queue for the next round, not all run simultaneously beyond capacity
- A task with zero duration — should schedule and complete instantly without breaking the timing math
- A pipeline that's fully sequential (no parallelism possible at all) — should still complete correctly, just with worker utilization of 1 throughout

**Suggested structure:**

```
build-pipeline-sim/
├── parser.py         # reads the dependency spec
├── topo_sort.py      # validates DAG, detects cycles
├── union_find.py     # identifies independent task groups (optional optimization)
├── scheduler.py      # assigns tasks to worker-rounds, respecting deps + capacity
└── tests/
    └── test_pipeline.py   # cycle detection, worker-capacity overflow case
```

---

## Capstone 9: Tiny Version Control Tool

**Combines:** Hashing · Graphs/Trees · Topological Sort · LCS

**Input:** `commit(files_snapshot, message)`, `diff(commit_a, commit_b)`, `checkout(commit_id)`. **Output:** A stored commit graph; a diff report between any two commits; restored file state at checkout.

**Edge cases:**

- Committing content identical to what's already stored — should reuse the existing content-hash/blob rather than storing a duplicate (this is literally how Git's content-addressable storage works — worth testing explicitly)
- Diffing two commits with no direct linear history between them — must still produce a valid diff via LCS, regardless of branch topology
- Checking out a commit ID that doesn't exist — clear error, not corrupted state
- A commit with zero file changes from its parent — still a valid, storable commit
- Very large files making LCS-based diffing slow — document this as a real, known limitation (production diff tools fall back to heuristics for exactly this reason)

**Suggested structure:**

```
tiny-vcs/
├── blob_store.py      # content-addressable storage (hash -> content)
├── commit_graph.py    # DAG of commits, parent pointers
├── diff_engine.py     # LCS-based diff between any two commits
├── checkout.py        # restores file state from a commit
└── tests/
    └── test_vcs.py    # duplicate-content dedup, unrelated-commit diff
```

---

## Capstone 10: Real-Time Analytics Dashboard

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
