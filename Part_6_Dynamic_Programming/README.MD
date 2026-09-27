# DSA Project Specs — Part 6: Dynamic Programming

*Full spec for each project: input/output format, edge cases, suggested file structure*

---

## 41. DP Fundamentals Bench (T1)

**Input:** `n` (Fibonacci, climbing stairs), or a coin denomination list + target amount (coin change). **Output:** The computed value (nth Fibonacci number, ways to climb, minimum coins needed); timing comparison against naive recursion.

**Edge cases:**

- n = 0 or n = 1 — base cases that are easy to get subtly wrong
- Negative n — invalid input, should be rejected explicitly
- Coin change where no valid combination reaches the target — return -1/"impossible," don't crash
- n large enough that naive recursion would hang for minutes — cap or timeout the naive version specifically when benchmarking
- Duplicate denominations in the coin list

**Suggested structure:**

```
dp-fundamentals/
├── naive_recursive.py   # baseline, exponential
├── memoized.py          # top-down with cache
├── tabulated.py         # bottom-up
├── bench.py
└── tests/
    └── test_dp_basics.py
```

---

## 42. Knapsack Solvers (T1)

**Input:** Item weights + values, capacity W; a flag for 0/1 vs. unbounded. **Output:** Max achievable value; optionally, the selected item set.

**Edge cases:**

- Capacity 0 — no items fit, value 0
- A single item heavier than the entire capacity — must be excluded, not crash
- All items with zero weight — value could be "unbounded" in a naive model; this degenerate case is worth flagging explicitly rather than silently mishandling
- Empty item list
- Unbounded knapsack: verify the capacity constraint is respected even when the same high-value/low-weight item is theoretically selectable many times over

**Suggested structure:**

```
knapsack/
├── knapsack_01.py
├── knapsack_unbounded.py
├── reconstruct_selection.py   # traces back which items were chosen
└── tests/
    └── test_knapsack.py       # verify against brute force on small cases
```

---

## 43. Budget Allocator (T2)

**Input:** A list of projects, each with `(cost, value)`; a total budget. **Output:** The subset of projects to fund that maximizes total value within budget, plus leftover unused budget.

**Edge cases:**

- A single project costing more than the entire budget — must be excluded from consideration
- Multiple projects with identical cost and value — any valid optimal selection is fine, but total value must be exactly correct
- Budget of 0 — fund nothing, don't error
- Multiple different subsets tying at the same max value — the tool should return one *consistently*, not vary between runs on the same input

**Suggested structure:**

```
budget-allocator/
├── models.py            # Project schema (cost, value)
├── knapsack_solver.py   # reused from Project 42
├── report.py            # shows selected projects + leftover budget
└── tests/
    └── test_allocator.py
```

---

## 44. LCS/LIS With Reconstruction (T1)

**Input:** Two strings (LCS), or one array of numbers (LIS). **Output:** The length of the LCS/LIS, *and* the actual subsequence itself.

**Edge cases:**

- One or both inputs empty — result is empty, length 0 (not `None`/an error)
- No common subsequence at all between two strings — still returns an explicit empty result
- LIS on a strictly decreasing array — longest increasing subsequence has length 1
- LIS with duplicate values — decide strictly-increasing vs. non-decreasing and be consistent, since this changes the answer
- Multiple LCS/LIS of the same max length exist — only one is needed, but it must be programmatically verified as an actual valid subsequence of the input, not just a length match

**Suggested structure:**

```
lcs-lis/
├── lcs.py   # DP table + backtrack reconstruction
├── lis.py   # O(n log n) or O(n²) + reconstruction
└── tests/
    └── test_reconstruction.py   # verifies reconstructed sequence is genuinely valid
```

---

## 45. Mini Diff Tool (T2)

**Input:** Two text files (or strings), split into lines. **Output:** A diff report showing added/removed/unchanged lines, in order.

**Edge cases:**

- Identical files — diff should show zero changes
- Completely different files — every line shows as changed, not an error
- Files of very different lengths
- A line appearing multiple times in both files — must correctly track which specific occurrence maps to which, not just match by content globally (a classic diff-algorithm subtlety)
- Files large enough that a naive O(n·m) LCS is too slow/memory-heavy — document this limitation explicitly rather than silently hanging on large inputs

**Suggested structure:**

```
mini-diff/
├── line_splitter.py
├── lcs_diff.py            # reused/adapted from Project 44
├── report_formatter.py    # renders +/- style diff output
└── tests/
    └── test_diff.py
```

---

## 46. Grid/Path DP Solvers (T1)

**Input:** An m×n grid (with obstacle markers for the obstacle variant); two strings (edit distance). **Output:** Number of unique paths, minimum path sum, or minimum edit distance.

**Edge cases:**

- The start or end cell itself is an obstacle — 0 valid paths
- A 1×1 grid — trivially 1 path, cost equal to the single cell's value
- Edit distance between two identical strings — 0
- Edit distance where one string is empty — distance equals the length of the other string
- An obstacle configuration that fully blocks every path — must return 0, not crash

**Suggested structure:**

```
grid-path-dp/
├── unique_paths.py
├── min_path_sum.py
├── edit_distance.py
└── tests/
    └── test_grid_dp.py   # fully-blocked-path case, explicitly
```

---

## 47. Spell-Check / Path Optimizer (T2)

Two directions for this slot — pick one:

### Direction A: Spell-Checker

**Input:** A dictionary of correct words; a misspelled word. **Output:** A ranked list of the closest dictionary words by edit distance.

**Edge cases:**

- The input word is already correctly spelled — should still return sensibly (e.g., itself as the top match)
- A large dictionary making per-query full edit-distance comparison against every entry too slow — note this as a known limitation, or note a prefix/BK-tree structure as a future optimization
- Multiple dictionary words tied at the same edit distance — return several, optionally ranked by frequency

### Direction B: Robot Path Optimizer

**Input:** A grid with obstacles and per-cell movement costs; start and end cells. **Output:** The minimum-cost path avoiding obstacles.

**Edge cases:**

- No path exists due to obstacles — report unreachable explicitly
- Zero-cost cells — decide whether these are allowed and how they interact with "shortest" path logic (could create ties)
- Start cell equals end cell

**Suggested structure:**

```
spellcheck-or-pathopt/
# Spell-check variant:
├── dictionary.py
├── edit_distance.py   # reused from Project 46
├── suggester.py       # ranks dictionary words by distance
└── tests/
    └── test_suggester.py

# Path-optimizer variant:
├── grid.py
├── cost_dp.py
└── tests/
    └── test_path_cost.py
```

---