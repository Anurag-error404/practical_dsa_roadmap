# DSA Project Specs — Part 8 : Advanced Topics

*Full spec for each project: input/output format, edge cases, suggested file structure*

---

# Part 8 — Advanced Topics

## 50. Bitmask Utility Set (T1)

**Input:** Integers for bit operations; a set of elements for bitmask-based subset generation. **Output:** All subsets (via bitmask iteration); the single non-duplicate number in an array; the bit count of a number.

**Edge cases:**

- Empty input set — subset generation should still yield exactly one subset, the empty set
- Very large integers relative to fixed bit-width assumptions (matters especially in 32-bit vs. 64-bit contexts)
- Negative numbers and two's-complement effects on bitwise operations
- Single-number problem given input that violates its precondition (more than one number appears an odd number of times) — document this as an assumption rather than silently returning a wrong answer

**Suggested structure:**

```
bitmask-utils/
├── subset_generator.py   # bitmask iteration, 0 to 2^n - 1
├── single_number.py      # XOR trick
├── bit_counter.py        # Brian Kernighan's algorithm
└── tests/
    └── test_bitmask.py
```

---

## 51. Permissions System / Bloom Filter (T2)

Two directions for this slot — pick one:

### Direction A: Permissions System

**Input:** Defined permission flags (read/write/execute, etc.); assign flags to users via bitmask; `check(user, permission)`. **Output:** Boolean permission check result.

**Edge cases:**

- Checking a permission flag that was never defined — should error, not silently return false
- Combining/removing permissions (OR to add, AND-NOT to remove) — a common source of subtle bugs if the bit logic is inverted
- A user with zero permissions vs. a user with all permissions

### Direction B: Bloom Filter

**Input:** `add(item)`, `might_contain(item)`; configured filter size + number of hash functions. **Output:** Boolean — "definitely not present" or "possibly present."

**Edge cases:**

- False positives are expected and must be *tested for*, not treated as a bug
- False negatives must **never** occur — an item that was explicitly added must always return "might contain" true
- Filter size/hash-count chosen too small for the expected item count — leads to unacceptably high false-positive rates; document the size/accuracy trade-off

**Suggested structure:**

```
permissions-or-bloomfilter/
# Permissions variant:
├── permission_flags.py
├── user_permissions.py
└── tests/
    └── test_permissions.py

# Bloom filter variant:
├── bloom_filter.py   # bit array + multiple hash functions
└── tests/
    └── test_bloom_filter.py   # false-positive rate + false-negative guarantee
```

---

## 52. Segment Tree & Fenwick Tree (T1)

**Input:** An array; `range_query(l, r)` (sum/min/max); `update(index, value)`. **Output:** Correct aggregate for the queried range; a structure reflecting point updates immediately.

**Edge cases:**

- `l > r`, or out-of-bounds indices — should be validated and rejected
- `l == r` (single-element range query)
- Re-updating an index that was already updated before — behavior should be consistent (a "set," not accidentally an "add," unless explicitly built as an add-based Fenwick tree)
- Querying the full array range (a boundary case for the tree's internal structure)
- An empty array (size 0) — handle explicitly or disallow, but don't crash silently

**Suggested structure:**

```
segment-fenwick/
├── segment_tree.py   # range query + point update
├── fenwick_tree.py   # binary indexed tree, prefix-sum based
└── tests/
    └── test_range_queries.py   # l==r, full range, cross-checked against brute-force sum
```

---

## 53. Real-Time Analytics Backend (T2)

**Input:** A stream of `(timestamp, metric_value)` events; range queries like "sum/min/max between time A and B." **Output:** Query results computed efficiently even as new events keep arriving.

**Edge cases:**

- A query range containing no events — return a sensible default (0 for sum; explicit null/error for min/max of an empty set), not a crash
- Events arriving out of chronological order — decide whether to accept and re-index, or reject late data
- High event throughput requiring efficient point updates without full structure rebuilds
- A query range extending into the future (no data there yet) — return what's available, not an error

**Suggested structure:**

```
realtime-analytics/
├── ingest.py         # receives events, updates the underlying structure
├── fenwick_tree.py   # reused/adapted from Project 52
├── query_api.py      # range query endpoint
└── tests/
    └── test_analytics.py   # out-of-order arrival, empty-range query
```

---

## 54. KMP & Rabin-Karp (T1)

**Input:** A text string + a pattern string. **Output:** All starting indices where the pattern occurs in the text.

**Edge cases:**

- Pattern longer than the text — no matches possible, return empty, not an error
- A pattern that overlaps itself in the text (e.g., `"aa"` in `"aaaa"`) — must find *all* overlapping matches, not skip past them
- An empty pattern — decide the convention (matches everywhere, or explicitly rejected) and document it
- Rabin-Karp: a hash collision that isn't an actual character match (a "spurious hit") — must be verified with a direct character comparison before confirming, or the algorithm will report false positives

**Suggested structure:**

```
string-matching/
├── kmp.py          # failure function + search
├── rabin_karp.py   # rolling hash + spurious-hit verification
└── tests/
    └── test_matching.py   # overlapping matches, spurious-hit case, explicitly
```

---

## 55. Catalogue Search Tool (T2)

**Input:** A large document set (e.g., 10,000 files); a search term or phrase query. **Output:** Documents containing the term, with match positions/counts, ranked by relevance.

**Edge cases:**

- Search term found in zero documents — return an empty result, not an error
- A very common term appearing in nearly every document — ranking still needs to mean something (e.g., frequency-based scoring, not just presence/absence)
- Whole-word vs. partial-word matching (should `"cat"` match `"category"`?) — decide and document
- Documents added/updated after the initial index is built — decide whether incremental re-indexing is supported, or a full rebuild is required
- A document set large enough that a linear scan per query is too slow — build an inverted index upfront rather than searching each document at query time

**Suggested structure:**

```
catalogue-search/
├── indexer.py             # builds an inverted index across documents
├── kmp_or_rabinkarp.py    # reused from Project 54, for exact matching within docs
├── ranker.py              # scores/ranks results
├── query_api.py
└── tests/
    └── test_search.py
```

---

## 56. Basic Max-Flow (T1)

**Input:** A directed graph with edge capacities; source and sink nodes. **Output:** The maximum flow value from source to sink; the min-cut edges.

**Edge cases:**

- Source equals sink — degenerate case, should be rejected as invalid input
- No path exists from source to sink at all — max flow is 0
- A graph containing cycles — Ford-Fulkerson must handle this correctly via the residual graph, not loop forever
- Zero-capacity edges — should behave as if the edge doesn't exist
- Verify max-flow value equals min-cut capacity (the max-flow min-cut theorem) as a built-in correctness check

**Suggested structure:**

```
max-flow/
├── graph.py             # capacities + residual graph
├── ford_fulkerson.py    # BFS-based (Edmonds-Karp) for guaranteed termination
├── min_cut.py           # derives min-cut from the final residual graph
└── tests/
    └── test_max_flow.py   # max-flow == min-cut verification
```

---

## 57. Ride/Job Matching Simulator (T2)

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