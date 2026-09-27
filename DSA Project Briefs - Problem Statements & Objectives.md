# DSA Project Roadmap: Problem Statements & Objectives

*A companion to the project roadmap — every project, framed as a brief*

Each entry: the **problem** that motivates building it, and the **objective** — what "done" looks like.

---

## Part 1 — Foundations

| Project | Problem Statement | Objective |
| --- | --- | --- |
| Complexity Benchmark Harness (T1) | You've read that O(n²) is "slow," but never watched it actually fail at scale. | Implement the same task two ways; measure real runtime at 10³/10⁵/10⁷ inputs; plot the curve. |
| Big-O Visualizer (T2) | Big-O feels abstract until you can watch the gap widen live. | Build a UI: pick algorithm + input size, render measured time as an interactive growth chart. |
| Dynamic Array (T1) | Built-in arrays hide their resize logic — you don't know what happens on overflow. | Implement push/get/resize-on-overflow; verify amortized O(1) append via benchmark. |
| Columnar Analytics Engine (T2) | Aggregating a large dataset by scanning rows one at a time doesn't scale. | Store data column-wise; support fast sum/avg/filter over a chosen column. |
| String Utility Library (T1) | You call `.reverse()`/`.isPalindrome()` without knowing what's underneath. | Implement reverse, palindrome check, anagram check, run-length compression — no built-ins. |
| Duplicate-Content Detector (T2) | Near-duplicate text (plagiarism, spun content) evades exact-match checks. | Flag paragraphs across documents that are suspiciously similar, not just identical. |
| Hash Table From Scratch (T1) | Hash maps feel magic until you've handled a collision yourself. | Implement your own hash function + chaining or open addressing; test collision-heavy input. |
| URL Shortener / KV Cache (T2) | Long URLs (or slow repeated lookups) need an O(1) short-key system. | Generate short keys via hashing; support create/lookup/expiry (TTL) end-to-end. |

## Part 2 — Linear Structures

| Project | Problem Statement | Objective |
| --- | --- | --- |
| Linked List Suite (T1) | Arrays cost O(n) to insert/delete mid-sequence — sometimes you need O(1). | Build singly + doubly linked lists: insert, delete, reverse, cycle detection. |
| LRU Cache / Music Queue (T2) | A cache with unlimited size eventually exhausts memory. | Combine a linked list + hash map so both "most recent" and "lookup by key" are O(1). |
| Expression Evaluator (T1) | `"3 + 4 * 2"` isn't evaluable by reading left to right without a structure for precedence. | Convert infix → postfix using a stack, then evaluate the postfix expression. |
| Browser-History / Undo-Redo (T2) | "Go back" needs to remember exactly what came before, in order. | Implement back/forward or undo/redo using two stacks (history + future). |
| Circular Queue & Deque (T1) | A naive queue wastes array space as items are dequeued from the front. | Implement a circular queue and a deque supporting O(1) operations at both ends. |
| Job Processor / Sliding-Max Dashboard (T2) | Tasks arrive faster than they can run, or you need the max over a moving window. | Build a priority-aware job queue, or a live dashboard showing max-in-last-N-events. |

## Part 3 — Core Algorithmic Patterns

| Project | Problem Statement | Objective |
| --- | --- | --- |
| Two-Pointer Toolkit (T1) | Naive pair-finding in sorted data is O(n²) when O(n) is possible. | Solve merge-two-sorted-arrays, remove-duplicates, and container-with-most-water. |
| Log Merger (T2) | Logs from multiple servers, each sorted, need one merged chronological timeline. | Merge N sorted log files into one ordered stream without loading everything into memory at once. |
| Sliding-Window Solver Set (T1) | Recomputing a window sum/count from scratch each shift is wasteful. | Solve max-subarray-sum and longest-substring-without-repeats in O(n). |
| API Rate Limiter (T2) | An API needs to cap requests per rolling time window, not a fixed calendar window. | Build real middleware enforcing "max N requests per rolling 60s" using a sliding window. |
| Binary Search Library (T1) | Standard binary search breaks on duplicates or rotated arrays without care. | Implement search, first/last-occurrence, and search-in-rotated-sorted-array. |
| Git-Bisect Simulator (T2) | Finding which of 1,000 commits introduced a bug by checking each one is too slow. | Simulate bisecting a commit history to find the first "bad" commit in O(log n) checks. |
| Backtracking Solver Set (T1) | Some problems (N-Queens, Sudoku) have no formula — only systematic trial and undo. | Solve N-Queens, a Sudoku solver, and a permutations/subsets generator. |
| Maze/Sudoku App (T2) | A puzzle generator needs to guarantee the puzzle it creates is actually solvable. | Build a maze generator + solver, or a Sudoku app with a solve/hint feature. |
| Sort Algorithm Bench (T1) | "Which sort is fastest" depends entirely on the data — nobody believes this until they measure it. | Implement merge/quick/heap/counting sort; benchmark each on random vs. nearly-sorted input. |
| Multi-Criteria Sorter (T2) | Users want to sort files/playlists by name, then date, then a custom rule — not just one key. | Build a sorter accepting custom comparators, or an external sort for a file bigger than memory. |

## Part 4 — Trees & Hierarchical Structures

| Project | Problem Statement | Objective |
| --- | --- | --- |
| BST From Scratch (T1) | Keeping a growing dataset sorted via re-sorting on every insert is wasteful. | Implement insert/delete/search + in/pre/post-order traversal; add a balance checker. |
| File-System Explorer (T2) | A folder tree needs fast search without scanning every file linearly. | Model folders/files as a tree; support search by name across the whole structure. |
| Heap From Scratch (T1) | Finding "the current max/min" by scanning is O(n) every time; it should be O(1). | Implement heapify, insert, and extract-min/max for a binary heap. |
| Leaderboard / Compressor (T2) | "Top 10 right now" shouldn't require re-sorting the entire dataset on every update. | Build a top-K service using a heap, or a file compressor using your own Huffman coding. |
| Trie From Scratch (T1) | Checking "does any word start with 'pre-'" via a hash set means scanning all keys. | Implement insert/search/prefix-search/delete on a trie. |
| Autocomplete Engine (T2) | Typing "pre" should surface matching words instantly, not after a full-dictionary scan. | Build a live autocomplete/suggestion box backed by your trie. |

## Part 5 — Graphs

| Project | Problem Statement | Objective |
| --- | --- | --- |
| Graph Traversal Library (T1) | "Is there a path from A to B" and "are these all connected" need systematic traversal. | Implement BFS, DFS, cycle detection, and connected-components on an adjacency-list graph. |
| Degrees-of-Separation Tool (T2) | "How is person A connected to person B" isn't answerable by inspection on a real network. | Given a friend-graph dataset, compute shortest connection path via BFS. |
| Topological Sort (T1) | Some tasks must run before others — an arbitrary order breaks dependencies. | Implement topo sort via Kahn's algorithm and via DFS; detect impossible (cyclic) orderings. |
| Build-System Simulator (T2) | A dependency file needs to become a valid, deterministic execution order. | Read task dependencies from a file; output a valid build order (or report a cycle). |
| Union-Find (T1) | Repeatedly checking "are these two nodes connected" via full traversal is slow at scale. | Implement Union-Find with path compression + union by rank; benchmark vs. naive BFS checks. |
| Friend-Circles / Image Regions (T2) | Determining which users (or pixels) form a connected group needs fast grouping, not per-pair checks. | Detect friend groups in a social graph, or connected regions in a simple 2D image grid. |
| Shortest-Path Comparison (T1) | Dijkstra, Bellman-Ford, and Floyd-Warshall solve "shortest path" differently — the differences matter. | Run all three on the same weighted graph; confirm they agree; time each. |
| Pathfinding Game (T2) | A game character needs to navigate around obstacles toward a goal, not walk through walls. | Build a grid game where an NPC/player pathfinds live via Dijkstra or A\*. |
| MST Implementation (T1) | Connecting all nodes cheaply isn't the same as connecting them at all. | Implement Prim's and Kruskal's; verify both produce the same total minimum cost. |
| Network Design Tool (T2) | Given cities and cable costs, wiring everything to everything is needlessly expensive. | Given nodes + edge costs, output the minimum-cost way to connect all of them. |

## Part 6 — Dynamic Programming

| Project | Problem Statement | Objective |
| --- | --- | --- |
| DP Fundamentals Bench (T1) | Naive recursive Fibonacci/coin-change recomputes the same subproblem exponentially many times. | Implement memoized and tabulated versions; benchmark against naive recursion at n=35+. |
| Knapsack Solvers (T1) | Choosing items under a hard capacity constraint isn't solvable by sorting alone. | Implement 0/1 knapsack and unbounded knapsack; verify against brute force on small cases. |
| Budget Allocator (T2) | A team has limited budget and more good ideas than it can fund. | Given projects with cost + value, output the value-maximizing subset within budget. |
| LCS/LIS With Reconstruction (T1) | Knowing the *length* of the longest common subsequence isn't the same as knowing *what it is*. | Implement LCS and LIS, and reconstruct the actual sequence, not just its length. |
| Mini Diff Tool (T2) | Comparing two file versions line-by-line by eye doesn't scale past a few lines. | Build a tool that outputs line-level insertions/deletions between two text files, like `git diff`. |
| Grid/Path DP Solvers (T1) | Counting paths or minimum cost through a grid by brute-force enumeration is exponential. | Implement unique-paths, min-path-sum, and edit-distance. |
| Spell-Check / Path Optimizer (T2) | "Did you mean...?" needs a notion of how *close* two strings are, not just equal/unequal. | Build a "did you mean" suggester using edit distance, or a grid robot avoiding obstacles at min cost. |

## Part 7 — Greedy Algorithms

| Project | Problem Statement | Objective |
| --- | --- | --- |
| Greedy Solver Set (T1) | Some optimization problems have a provably-correct "always pick the best option now" shortcut. | Implement activity selection, Huffman coding, and fractional knapsack. |
| Meeting-Room Scheduler (T2) | Overlapping meeting requests need the maximum non-conflicting subset selected automatically. | Given meeting time ranges, output the max number schedulable without conflict. |

## Part 8 — Advanced Topics

| Project | Problem Statement | Objective |
| --- | --- | --- |
| Bitmask Utility Set (T1) | Storing 8 boolean flags as 8 separate variables wastes space and is error-prone to check. | Implement subset generation, single-number-finder, and bit-counting via bitmasks. |
| Permissions System / Bloom Filter (T2) | Checking "have I seen this before" across millions of items shouldn't need to store them all. | Build a Unix-style flags/permissions system, or a Bloom filter for approximate membership testing. |
| Segment/Fenwick Trees (T1) | Range-sum queries over frequently-updated data are slow both to read (recompute) and write (naive) naively. | Implement both structures supporting O(log n) range query and point update. |
| Real-Time Analytics Backend (T2) | A live dashboard needs "sum between time A and B" answered fast on constantly-changing data. | Build a backend answering range-aggregate queries over a streaming metric feed. |
| KMP & Rabin-Karp (T1) | Naive substring search is O(n·m) — checking every position character-by-character. | Implement both algorithms; verify they match brute-force results but run faster on large text. |
| Catalogue Search Tool (T2) | Finding every occurrence of a term across 10,000 documents by naive scan is too slow to feel interactive. | Build a fast "find all occurrences of X" search over a large document set. |
| Basic Max-Flow (T1) | "How much can flow through this network given capacity limits" isn't answerable by inspection. | Implement Ford-Fulkerson; verify max-flow equals min-cut on a small test graph. |
| Ride/Job Matching Simulator (T2) | Assigning many requests to many resources (riders↔drivers, tasks↔workers) needs more than first-come-first-served. | Build a simulator that matches requests to resources via bipartite matching or greedy assignment. |

---

## Type 3 — Capstone Briefs

| Capstone | Problem Statement | Objective |
| --- | --- | --- |
| 1. Smart Task Manager | Tasks have priorities *and* dependencies *and* deadlines — no single structure handles all three. | Build a task manager where urgent tasks surface first, blocked tasks wait for dependencies, and conflicts get resolved automatically. |
| 2. Mini Search Engine | Search needs to be fast, ranked, and forgiving of partial input — not just exact string match. | Build search over a document set with autocomplete, ranked results, and exact-phrase matching. |
| 3. Pathfinding Game | A game world needs to be different every playthrough, and its inhabitants need to navigate it intelligently. | Build a game with procedurally generated mazes and an NPC that pathfinds around the player in real time. |
| 4. Ride-Sharing Dispatch | Matching riders to drivers needs both "who's closest" and "who's actually reachable fastest." | Simulate dispatch: nearest-driver lookup, real ETA via shortest-path, and rider-driver assignment. |
| 5. Code Editor Core | A text editor needs efficient edits, reversible history, and smart suggestions simultaneously. | Build a minimal editor: efficient text buffer, working undo/redo, find-and-replace, and autocomplete. |
| 6. E-Commerce Catalogue | Browsing a large catalogue needs hierarchy, filtering, sorting, and bundling — all fast, all at once. | Build a catalogue with category browsing, price filtering, multi-key sorting, and value-optimized bundle suggestions. |
| 7. Social Network Analyzer | A friend-graph hides its structure — who's central, who's clustered, who's how far apart. | Compute degrees of separation, detect friend clusters, and rank most-connected users on a real graph dataset. |
| 8. Build Pipeline Simulator | Build tasks with dependencies waste time if run sequentially when some could run in parallel. | Compute valid execution order, detect independent task groups, and maximize parallel scheduling. |
| 9. Tiny Version Control Tool | Tracking every full copy of every file version wastes enormous space; diffing by eye doesn't scale. | Build content-addressable storage for versions, a commit history graph, and a working diff between any two versions. |
| 10. Real-Time Analytics Dashboard | A live stream of events needs instant rolling metrics *and* historical range queries, without re-scanning everything. | Build a dashboard showing rolling window metrics, range-aggregate queries, and live top-K trending items. |

---