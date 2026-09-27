# DSA Project Specs — Part 5: Graphs

*Full spec for each project: input/output format, edge cases, suggested file structure*

---

## 31. Graph Traversal Library (T1)

**Input:** A graph as an adjacency list (nodes + edges, directed or undirected); a start node for BFS/DFS. **Output:** Traversal order; boolean for cycle detection; list of connected components.

**Edge cases:**

- A disconnected graph — traversal from one node won't reach every node, so full connected-component detection needs to loop over *all* nodes, not just start once
- Self-loops (a node with an edge to itself)
- Parallel edges (multiple edges between the same pair of nodes)
- Cycle detection differs between directed and undirected graphs — these need genuinely separate logic, not one function reused for both
- An empty graph, and a single node with no edges

**Suggested structure:**

```
graph-traversal/
├── graph.py                   # adjacency list representation
├── bfs.py
├── dfs.py
├── cycle_detection.py         # separate directed/undirected logic
├── connected_components.py
└── tests/
    └── test_traversal.py
```

---

## 32. Degrees-of-Separation Tool (T2)

**Input:** A friend-graph dataset (edges as pairs); two user IDs to query. **Output:** The shortest path length (degrees) between them, and the path itself.

**Edge cases:**

- The two users are the same person — degree 0
- No path exists (they're in disconnected parts of the graph) — report "not connected" explicitly, don't error or loop forever
- A graph large enough that naive re-scans per query are too slow — BFS should be efficient, not O(V²)
- Multiple shortest paths of equal length — only one needs to be returned, but the choice should be deterministic and reproducible

**Suggested structure:**

```
degrees-of-separation/
├── graph_loader.py   # loads edges into an adjacency list
├── bfs_path.py        # shortest path + degree count
├── cli.py             # query interface
└── tests/
    └── test_bfs_path.py
```

---

## 33. Topological Sort (T1)

**Input:** A DAG as an adjacency list or edge list of dependencies. **Output:** A valid topological order, or a clear cycle-detected report if the graph isn't actually a DAG.

**Edge cases:**

- A cycle present — must be detected and reported, not silently produce a wrong or partial ordering
- Multiple valid topological orders exist — any one is acceptable, but verify it by checking every edge points forward in the output order
- Disconnected components within the same graph — every node must still appear in the final order
- A node with no edges at all (isolated)

**Suggested structure:**

```
topo-sort/
├── graph.py
├── kahns_algorithm.py   # BFS-based, in-degree tracking
├── dfs_based.py         # DFS + stack-based approach
└── tests/
    └── test_topo_sort.py   # cycle detection, explicitly
```

---

## 34. Build-System Simulator (T2)

**Input:** A dependency spec (task → list of tasks it depends on). **Output:** A valid execution order, or a reported circular dependency showing which tasks are involved.

**Edge cases:**

- A circular dependency — report *which tasks* form the cycle, not just "a cycle exists somewhere"
- A task listed as a dependency but never itself defined — decide whether this is an error or gets auto-included as a no-op task
- Duplicate dependency declarations for the same pair
- A fully independent task with no dependencies and nothing depending on it — should still appear in the output, order-agnostic

**Suggested structure:**

```
build-system-sim/
├── parser.py           # reads the dependency spec file
├── topo_sort.py         # reused from Project 33
├── cycle_reporter.py     # extracts and displays the actual cycle path
└── tests/
    └── test_build_order.py
```

---

## 35. Union-Find (T1)

**Input:** A sequence of `union(a, b)` and `find(a)` / `connected(a, b)` operations. **Output:** Correct connectivity answers after every union.

**Edge cases:**

- `union(a, a)` — unioning an element with itself
- `find()` on an element never explicitly added — decide whether it auto-initializes or errors
- Calling `union()` on the same pair repeatedly — should be idempotent, without incorrectly inflating rank/size bookkeeping
- Path compression must not corrupt the rank/size values used by union-by-rank
- A long chain built before path compression runs — a good stress test to confirm the optimization is actually reducing lookup depth, not just present in the code

**Suggested structure:**

```
union-find/
├── union_find.py   # path compression + union by rank
└── tests/
    └── test_union_find.py   # performance comparison with/without optimizations
```

---

## 36. Friend-Circles / Image Regions (T2)

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

## 37. Shortest-Path Comparison (T1)

**Input:** A weighted graph (possibly with negative weights, to exercise Bellman-Ford); a source node (and target, or none for Floyd-Warshall's all-pairs mode). **Output:** Shortest distances from source to all nodes (Dijkstra/Bellman-Ford); the full all-pairs distance matrix (Floyd-Warshall).

**Edge cases:**

- Negative edge weights fed to Dijkstra — Dijkstra assumes non-negative weights and will silently give a wrong answer; either reject negative weights explicitly or document the limitation
- A negative cycle present — Bellman-Ford must *detect and report* this, not return a plausible-looking but wrong finite distance
- A disconnected graph — unreachable nodes should report infinity/unreachable, not error
- A graph with a single node; self-loops with a weight attached

**Suggested structure:**

```
shortest-path-comparison/
├── graph.py
├── dijkstra.py          # heap-based
├── bellman_ford.py      # includes negative-cycle detection
├── floyd_warshall.py    # all-pairs
└── tests/
    └── test_shortest_path.py   # cross-checks all three agree where valid
```

---

## 38. Pathfinding Game (T2)

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

## 39. MST Implementation (T1)

**Input:** A weighted, undirected, connected graph. **Output:** The set of edges forming the MST, and its total cost.

**Edge cases:**

- A disconnected graph — no single spanning tree exists; detect this and either return a minimum spanning forest or an explicit error, rather than a partial/wrong tree
- Duplicate-weight edges — multiple valid MSTs may exist with the same total cost; any one is acceptable, but total cost must be correct
- A graph with only one node — trivial MST, no edges, cost 0
- Prim's and Kruskal's must agree on total cost, even when they select different edges to get there

**Suggested structure:**

```
mst/
├── graph.py
├── prims.py       # heap-based
├── kruskals.py    # union-find based, sorts edges by weight
└── tests/
    └── test_mst.py   # verifies matching total cost between both algorithms
```

---

## 40. Network Design Tool (T2)

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