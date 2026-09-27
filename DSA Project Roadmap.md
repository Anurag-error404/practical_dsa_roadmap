# DSA Project Roadmap: Build Your Way to Mastery

*A companion to the concept guide — same topics, now as things you build*

---

## The three project types

- **Type 1 — Isolated Build:** Implement the data structure/algorithm itself, from scratch, as a small standalone module or CLI tool. No business logic around it — just the mechanism, built correctly.
- **Type 2 — Applied Build:** The concept becomes the *core engine* of a small real-world-shaped application. You're not implementing Dijkstra's for its own sake — you're building a pathfinding game that *needs* Dijkstra's to function.
- **Type 3 — Capstone Build:** A larger project that only works if 3–5 concepts cooperate correctly — this is where you find out if you actually understand the trade-offs, because a wrong choice in one subsystem breaks another.

**How to move through this:** For a given topic, do Type 1 first (get the mechanism correct in isolation, easy to debug), then Type 2 (see it under real constraints — performance, edge cases, UX). Only attempt Type 3 capstones once the underlying concepts each have a Type 1 + Type 2 behind them — otherwise you're debugging five unknowns at once.

---

## Part 1 — Foundations

| Topic | Type 1 — Isolated Build | Type 2 — Applied Build |
| --- | --- | --- |
| **Complexity Analysis** | Benchmark harness: implement the same task (dedupe, search) an O(n²) way and an O(n) way, time both at increasing input sizes | "Big-O Visualizer" — pick an algorithm + input size, plot real measured execution time as a growth curve |
| **Arrays** | Build a dynamic (resizable) array class from scratch — no built-in push/append | A tiny in-memory columnar analytics engine: rows stored as arrays, supports fast sum/avg/filter over a column |
| **Strings** | A string-utility library from scratch: reverse, palindrome check, anagram check, run-length compression | A near-duplicate/plagiarism detector for text documents (flags paragraphs that are suspiciously similar) |
| **Hashing** | A hash table from scratch — your own hash function + collision handling (chaining or open addressing) | A URL shortener service, or a Redis-style in-memory key-value cache server with TTL expiry |

## Part 2 — Linear Structures

| Topic | Type 1 — Isolated Build | Type 2 — Applied Build |
| --- | --- | --- |
| **Linked Lists** | Singly + doubly linked list with insert/delete/reverse/cycle-detection | An LRU cache (linked list + hash map combo) packaged as a reusable library, or a music-queue app with next/prev/shuffle |
| **Stacks** | A stack-based expression evaluator (infix → postfix → evaluate) | A browser-history simulator with working back/forward, or an undo/redo system for a text/code editor |
| **Queues & Deques** | A circular queue and a deque, implemented from scratch | A background job/task processor with priorities (simulated print queue), or a live "max value in last N events" dashboard |

## Part 3 — Core Algorithmic Patterns

| Topic | Type 1 — Isolated Build | Type 2 — Applied Build |
| --- | --- | --- |
| **Two Pointers** | Solve merge-two-sorted-arrays, remove-duplicates, container-with-most-water as a small CLI toolkit | A log-merger: takes sorted log files from multiple servers and merges them into one chronological timeline |
| **Sliding Window** | A sliding-window solver set: max subarray sum, longest substring without repeats | An API rate-limiter (rolling window) built as real middleware for a small web server |
| **Binary Search** | Binary search + variants: first/last occurrence, search in rotated sorted array | A "which commit broke this" tool — simulate `git bisect` over a mock commit history |
| **Recursion & Backtracking** | N-Queens, Sudoku solver, permutations/subsets generator | A maze generator + solver, or a Sudoku app with a "give me a hint" feature powered by your solver |
| **Sorting** | Implement merge sort, quicksort, heapsort, counting sort; benchmark each on random vs. nearly-sorted data | A "sort my files/playlist" tool with multiple sort criteria, or an external-sort tool for a file too big to fit in memory |

## Part 4 — Trees & Hierarchical Structures

| Topic | Type 1 — Isolated Build | Type 2 — Applied Build |
| --- | --- | --- |
| **Binary Trees / BST** | A BST with insert/delete/search/traversals + a balance checker | A file-system explorer (folders/files as a tree) with fast search |
| **Heaps** | A min-heap and max-heap from scratch, with heapify | A "trending now" / leaderboard service returning top-K efficiently, or a file compressor using your own Huffman coding |
| **Tries** | A trie with insert/search/prefix-search/delete | An autocomplete/search-suggestion engine for a text box, or an IP-routing longest-prefix matcher |

## Part 5 — Graphs

| Topic | Type 1 — Isolated Build | Type 2 — Applied Build |
| --- | --- | --- |
| **Graph Representations + BFS/DFS** | A graph class (adjacency list) with BFS, DFS, cycle detection, connected components | A "degrees of separation" tool on a small social-graph dataset, or a depth-limited web crawler |
| **Topological Sort** | Topological sort via Kahn's algorithm and via DFS, with cycle detection | A mini build-system simulator — reads a dependency file, outputs valid task execution order (like a toy Make/Webpack) |
| **Union-Find** | Union-Find with path compression + union by rank | A "friend circles" / network-connectivity checker, or a connected-regions detector for a simple image (basic segmentation) |
| **Shortest Path (Dijkstra, Bellman-Ford, Floyd-Warshall)** | Implement all three on the same weighted graph, compare outputs and runtime | **A grid-based pathfinding game** — player/NPC navigates obstacles using Dijkstra or A\*; or a mini GPS-style route planner over a city-graph |
| **Minimum Spanning Tree (Prim's, Kruskal's)** | Implement both MST algorithms, verify they agree on total cost | A "cheapest network design" tool — given cities + cable costs, output the minimum-cost way to connect them all |

## Part 6 — Dynamic Programming

| Topic | Type 1 — Isolated Build | Type 2 — Applied Build |
| --- | --- | --- |
| **DP Fundamentals** | Fibonacci, climbing stairs, coin change — memoization vs. tabulation, benchmarked against naive recursion | *(fold into the applied builds below — this is the mechanism, not a standalone product)* |
| **Knapsack** | 0/1 and unbounded knapsack solvers | A "budget allocator": given projects/features with cost + value, output the optimal set to fund within budget |
| **LCS / LIS** | LCS and LIS with actual sequence reconstruction, not just length | **A diff tool** — a simplified `git diff` showing line-by-line changes between two text files |
| **Grid / Path DP** | Unique-paths, min-path-sum, edit-distance solvers | A spell-check "did you mean" tool using edit distance, or a robot path-cost optimizer on a grid with obstacles |

## Part 7 — Greedy Algorithms

| Topic | Type 1 — Isolated Build | Type 2 — Applied Build |
| --- | --- | --- |
| **Greedy** | Activity selection, Huffman coding, fractional knapsack | A meeting-room/calendar conflict scheduler (max non-overlapping meetings), or a file-compressor using your Huffman implementation |

## Part 8 — Advanced Topics

| Topic | Type 1 — Isolated Build | Type 2 — Applied Build |
| --- | --- | --- |
| **Bit Manipulation** | Bitmask subset generator, single-number finder, bit-counting utilities | A Unix-style permissions/flags system using bitmasks, or a Bloom filter for "have I seen this URL before" |
| **Segment Trees / Fenwick Trees** | A segment tree and a Fenwick tree, both supporting range queries + point updates | A real-time analytics backend answering "sum/min/max of metric X between time A and B" on a live-updating stream |
| **String Matching (KMP, Rabin-Karp)** | Implement both from scratch, verify against brute-force search | **A search tool for a huge document catalogue** — "find every occurrence of this term across 10,000 files," fast |
| **Flow / Bipartite Matching** | Basic max-flow (Ford-Fulkerson) on a small graph | A ride-matching simulator (drivers ↔ riders) or a job-assignment tool (workers ↔ tasks) |

---

## Type 3 — Multi-Concept Capstones

These only work if several subsystems cooperate. Each one lists exactly which concepts it forces you to combine — that mapping is the point; if you can't say which concept is doing which job in your own project, that's the signal to slow down.

### 1. Smart Task Manager

Task manager with priority-based scheduling and dependency-aware ordering (some tasks block others). **Combines:** Hashing (task lookup) · Heaps (priority queue for urgent items) · Topological Sort (dependency ordering) · Greedy (calendar conflict resolution)

### 2. Mini Search Engine

Search across a document set with autocomplete, ranked results, and exact-phrase matching. **Combines:** Tries (autocomplete) · Hashing (inverted index) · KMP/Rabin-Karp (exact phrase search) · Heaps (top-K ranked results) · Sorting (result ranking)

### 3. Pathfinding Game with Procedural Mazes

A grid game where mazes are procedurally generated and an NPC/enemy chases the player using real pathfinding. **Combines:** Backtracking (maze generation) · Graphs + Dijkstra/A\* (pathfinding) · Heaps (priority queue inside A\*) · BFS (reachability checks)

### 4. Ride-Sharing Dispatch Simulator

Simulates matching riders to nearby drivers and computing ETAs on a city road network. **Combines:** Graphs (road network) · Dijkstra (ETA/shortest route) · Heaps (nearest-driver queue) · Bipartite Matching or Greedy (rider-driver assignment)

### 5. Code Editor Core

A minimal text editor engine: efficient text buffer, undo/redo, find-and-replace, variable-name autocomplete. **Combines:** Linked Lists or a rope-like structure (text buffer) · Stacks (undo/redo) · Tries (autocomplete) · String Matching (find/replace)

### 6. E-Commerce Catalogue Engine

Product catalogue with category browsing, price-range filtering, sorting, and "frequently bought together" bundles. **Combines:** Hashing (product lookup) · BST/Trees (category hierarchy) · Two Pointers/Sliding Window (price-range filter) · Sorting (rank by price/rating) · Knapsack DP (best-value bundle suggestions)

### 7. Social Network Analyzer

Analyze a friend-graph dataset: degrees of separation, friend clusters, most-connected users. **Combines:** Graphs + BFS (degrees of separation) · Union-Find (friend groups/communities) · Heaps (top-K most-connected users)

### 8. Build Pipeline Simulator

Given a dependency file for a set of build tasks, compute execution order and maximize parallelization. **Combines:** Topological Sort (valid ordering) · Graphs (dependency DAG) · Union-Find (independent groups that can run in parallel) · Greedy (parallel scheduling)

### 9. Tiny Version Control Tool

A stripped-down Git: content-addressable storage, commit history, and a working diff between versions. **Combines:** Hashing (content-addressable blob storage, like Git's SHA objects) · Graphs/Trees (commit DAG) · Topological Sort (history traversal) · LCS (diff algorithm)

### 10. Real-Time Analytics Dashboard

Live dashboard showing rolling metrics, top trending items, and range-based aggregate queries over a streaming data feed. **Combines:** Sliding Window (rolling metrics) · Segment/Fenwick Tree (range queries) · Heaps (top-K trending) · Hashing (per-user/per-event counters)

---

## Suggested build order

**Phase 1 — Mechanism fluency (Parts 1–3, Type 1 only):** Get every foundational structure and pattern working in isolation. Don't skip this even though it's the least exciting — every later project's bugs trace back here if it's shaky.

**Phase 2 — Applied fluency (Parts 1–3, Type 2 + Parts 4–5, Type 1):** Start seeing structures under real constraints (performance, edge cases, concurrent access) while building fluency in trees/graphs at the mechanism level.

**Phase 3 — Full coverage (Parts 4–8, Type 1 + Type 2):** Round out DP, greedy, and advanced topics the same way — mechanism, then applied.

**Phase 4 — Capstones (Type 3, in the order listed above):** The list above is roughly ordered by complexity — #1–3 combine 3 concepts, #8–10 combine 4. Don't jump to #9 or #10 until at least 2–3 earlier capstones are done; the debugging skill of "which of my 4 subsystems has the bug" is itself something you build up.

---