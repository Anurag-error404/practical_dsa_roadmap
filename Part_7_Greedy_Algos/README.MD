# DSA Project Specs — Part 7: Greedy & Part 8: Advanced Topics

*Full spec for each project: input/output format, edge cases, suggested file structure*

---

# Part 7 — Greedy Algorithms

## 48. Greedy Solver Set (T1)

**Input:** Activity `(start, end)` list (activity selection); character frequencies (Huffman coding); item weight/value pairs + capacity, with fractional items allowed (fractional knapsack). **Output:** Max non-overlapping activities selected; a Huffman code per character; max achievable value (fractional knapsack allows partial items).

**Edge cases:**

- Activities with identical start/end times — need a consistent tie-break rule (typically: sort by end time, then start time)
- An activity ending exactly when another starts — decide whether this counts as overlapping (inclusive) or not (exclusive), and document it
- A single distinct character for Huffman — same degenerate-tree issue as the compressor project; needs explicit handling
- Fractional knapsack items with identical value-to-weight ratio — order doesn't matter, but total value must still be correct
- Capacity of 0

**Suggested structure:**

```
greedy-solvers/
├── activity_selection.py
├── huffman_coding.py
├── fractional_knapsack.py
└── tests/
    └── test_greedy.py   # boundary-overlap case, explicitly
```

---

## 49. Meeting-Room Scheduler (T2)

**Input:** A list of meeting requests, each with `(start, end)`, possibly a priority. **Output:** The maximum set of meetings schedulable without conflict; the list of rejected meetings.

**Edge cases:**

- Back-to-back meetings (one ends exactly when the next starts) — decide whether this is allowed
- Meetings with equal start times
- A duplicate meeting request
- A large volume of meetings needing the efficient greedy approach (sort by end time) rather than brute-force checking every combination
- Invalid time ranges (end before start) — should be rejected outright

**Suggested structure:**

```
meeting-scheduler/
├── models.py           # Meeting(start, end, priority)
├── scheduler.py        # greedy interval scheduling
├── conflict_checker.py
└── tests/
    └── test_scheduler.py
```

---
