# DSA Project Specs — Part 3: Core Algorithmic Patterns

*Full spec for each project: input/output format, edge cases, suggested file structure*

---

## 15. Two-Pointer Toolkit (T1)

**Input:** Sorted array(s) — two sorted arrays (merge), one sorted array (remove duplicates), or an array of heights (container-with-most-water). **Output:** Merged sorted array; deduplicated array with new logical length; max water area (integer).

**Edge cases:**

- One or both arrays empty (merge)
- Array where every element is a duplicate (dedup result should be length 1)
- All-equal heights for the container problem (area is determined purely by width)
- Array of length 0 or 1 for the container problem — no valid pair exists

**Suggested structure:**

```
two-pointer-toolkit/
├── merge_sorted.py
├── remove_duplicates.py
├── container_with_water.py
└── tests/
    └── test_two_pointer.py
```

---

## 16. Log Merger (T2)

**Input:** N sorted log files (each line timestamp-prefixed) + an output path. **Output:** A single file with all lines merged in chronological order.

**Edge cases:**

- A file that *isn't* actually sorted internally — should be detected and flagged, not silently merged wrong
- Files large enough that none can be fully loaded into memory — needs a true k-way merge (read line-by-line, min-heap of "next line per file"), not "load everything, then sort"
- Duplicate timestamps across files — decide tie-breaking order (e.g., preserve file order as a secondary key)
- An empty input file, or a file list of size 1

**Suggested structure:**

```
log-merger/
├── parser.py       # extracts timestamp from a line
├── merger.py       # k-way merge using a min-heap
├── validator.py    # checks each input file is pre-sorted
└── tests/
    └── test_merge.py
```

---

## 17. Sliding-Window Solver Set (T1)

**Input:** An array + window size k (max-sum-subarray), or a string (longest-substring-without-repeats). **Output:** The max sum (number), or the length/actual substring.

**Edge cases:**

- k larger than the array length — no valid window exists
- Empty array or empty string
- All identical elements (max sum is trivial; longest-no-repeat substring has length 1)
- k = 0 or k equal to the full array length exactly

**Suggested structure:**

```
sliding-window/
├── max_sum_subarray.py
├── longest_substring_no_repeat.py
└── tests/
    └── test_sliding_window.py
```

---

## 18. API Rate Limiter (T2)

**Input:** Incoming requests, each with a client ID and timestamp; a configured limit (e.g., max N requests per rolling 60s). **Output:** Allow/deny decision per request.

**Edge cases:**

- A burst of requests arriving in the same millisecond
- Requests arriving slightly out of chronological order (network jitter/clock skew)
- Old timestamps need to be evicted from each client's window efficiently — not by rescanning full history on every check
- Every client needs an *independent* window — a shared global counter would incorrectly let one client's traffic block another's

**Suggested structure:**

```
rate-limiter/
├── middleware.py                # intercepts requests, consults the limiter
├── sliding_window_limiter.py    # per-client deque of timestamps
└── tests/
    └── test_rate_limit.py
```

---

## 19. Binary Search Library (T1)

**Input:** A sorted array + target (basic search, first/last occurrence); a rotated sorted array + target (rotated search). **Output:** Index of the target, or a clear "not found" (-1); correct boundary index for first/last occurrence.

**Edge cases:**

- Target not present in the array at all
- Duplicates present — first-occurrence and last-occurrence must return *different, correct* indices
- Empty array, and array of size exactly 1
- Rotated array where the rotation point is 0 (i.e., not actually rotated) — must still work
- Target equal to the pivot element in a rotated search

**Suggested structure:**

```
binary-search-lib/
├── basic_search.py
├── first_last_occurrence.py
├── rotated_search.py
└── tests/
    └── test_binary_search.py
```

---

## 20. Git-Bisect Simulator (T2)

**Input:** A mock, ordered commit history where each commit is secretly marked good/bad, exposed only through a `test_commit(id)` function the algorithm can call. **Output:** The first bad commit, and the number of `test_commit()` calls used to find it.

**Edge cases:**

- The very first commit is already bad — no "good" baseline exists
- The very last commit is the first bad one
- History of length 1
- The history has a bad commit followed by more bad commits — must find the *first transition point*, not just any bad commit encountered

**Suggested structure:**

```
git-bisect-sim/
├── commit_history.py   # generates a mock history with a hidden bad commit
├── bisect.py            # binary-search-based bisection algorithm
└── tests/
    └── test_bisect.py   # asserts call count is O(log n)
```

---

## 21. Backtracking Solver Set (T1)

**Input:** N (N-Queens); a 9×9 grid with some cells pre-filled (Sudoku); a set of distinct elements (permutations/subsets). **Output:** All valid solutions (or one); all permutations/subsets.

**Edge cases:**

- N-Queens for N=2 or N=3 — provably has *no* solution; must return empty, not crash or loop
- A Sudoku puzzle that's invalid or unsolvable from the start (contradictory pre-filled cells)
- A Sudoku puzzle that's already fully solved (no blanks to fill)
- Duplicate elements in the permutation/subset input — decide whether duplicate results should be filtered
- Empty input set for subsets — the empty set itself is a valid subset and should appear in the output

**Suggested structure:**

```
backtracking-solvers/
├── n_queens.py
├── sudoku_solver.py
├── permutations_subsets.py
└── tests/
    └── test_backtracking.py
```

---

## 22. Maze/Sudoku App (T2)

**Input:** *(Maze)* grid dimensions + optional random seed. *(Sudoku)* a user-entered puzzle, or a "generate new" request. **Output:** *(Maze)* a generated maze guaranteed to have a solvable path, plus the solved path. *(Sudoku)* a puzzle, plus hint/solve output.

**Edge cases:**

- Maze generation must *guarantee* solvability — use a generation method that inherently guarantees connectivity (e.g., randomized DFS or Prim's-based carving) rather than generating random walls and hoping
- A 1×1 maze (degenerate case)
- A Sudoku puzzle with multiple valid solutions — flag it as ambiguous rather than silently returning one
- User requests a hint on an already-solved or contradictory puzzle — this is an invalid state to flag, not solve around

**Suggested structure:**

```
maze-sudoku-app/
├── maze/
│   ├── generator.py    # randomized DFS or Prim's-based generation
│   └── solver.py        # BFS/DFS solve + path output
├── sudoku/
│   ├── validator.py
│   └── solver.py
└── ui/
    └── app.py
```

---

## 23. Sort Algorithm Bench (T1)

**Input:** An unsorted array; a chosen algorithm (merge/quick/heap/counting); a data distribution to test against (random, nearly-sorted, reverse-sorted, all-duplicates). **Output:** The sorted array; timing per algorithm per distribution.

**Edge cases:**

- Already-sorted input fed to a naive quicksort with a poor (e.g., first-element) pivot choice — this is the classic worst-case that degrades to O(n²) and can even stack-overflow a recursive implementation
- An array where every element is identical
- Counting sort given a huge value range relative to array size — memory blows up; document that counting sort needs a *bounded* range to be viable
- Empty array, and array of size 1

**Suggested structure:**

```
sort-bench/
├── algorithms/
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── heap_sort.py
│   └── counting_sort.py
├── bench.py                    # runs all algos across all distributions
└── tests/
    └── test_correctness.py     # verifies sorted output for every algorithm
```

---

## 24. Multi-Criteria Sorter (T2)

**Input:** A list of items (files/playlist entries) with multiple attributes (name, date, size); a user-specified key order (e.g., "sort by date, then name"). **Output:** The list sorted by the specified multi-key order.

**Edge cases:**

- Ties on the primary key that need the secondary (and tertiary) key to break correctly
- User specifies a conflicting or duplicate key in the sort order
- Missing attribute values on some items (e.g., a file with no modified-date) — decide where these sort (first, last, or excluded)
- A file list large enough it doesn't fit in memory — needs an external sort (chunk, sort each chunk, merge from disk)

**Suggested structure:**

```
multi-criteria-sorter/
├── models.py           # item schema (name, date, size, ...)
├── comparator.py       # builds a composite comparator from key order
├── external_sort.py    # chunked sort-and-merge for large inputs
└── tests/
    └── test_comparator.py
```

---