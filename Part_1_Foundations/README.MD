# DSA Project Specs — Part 1: Foundations

*Full spec for each project: input/output format, edge cases, suggested file structure*

---

## 1. Complexity Benchmark Harness (T1)

**Input:** Two function implementations solving the same task (e.g., dedupe) — one O(n²), one O(n) — plus a list of input sizes to test at. **Output:** A table of `(input_size, algorithm, time_ms)` rows; optionally a rendered chart.

**Edge cases:**

- Input size large enough that the O(n²) version would take minutes — needs a timeout or size cap for that algorithm only
- Single-run timing noise (JIT/cache warm-up) — take multiple trials, report median
- Empty input (size 0) — should still run without error
- Input sizes not in increasing order

**Suggested structure:**

```
complexity-bench/
├── algorithms/
│   ├── naive_dedupe.py       # O(n²) version
│   └── hash_dedupe.py        # O(n) version
├── bench.py                  # runs each algo across sizes, records timing
├── results.csv
└── plot.py                   # optional: renders the growth curve
```

---

## 2. Big-O Visualizer (T2)

**Input:** User picks an algorithm from a list + an input size (or range) and triggers "run." **Output:** A live-updating chart of measured time vs. input size as runs complete.

**Edge cases:**

- Very large input size freezing the UI — run benchmarks off the main thread (worker/async)
- Comparing an O(n) and an O(n³) algorithm on the same linear axis (one looks flat) — offer a log-scale toggle
- User re-runs the same size — decide whether to overwrite or append as a new data point
- No algorithm selected yet — show an empty-state, not an error

**Suggested structure:**

```
bigo-visualizer/
├── algorithms.js          # registry of algorithm implementations
├── benchmark-worker.js    # runs timing off the main thread
├── chart.js               # renders results
└── index.html
```

---

## 3. Dynamic Array (T1)

**Input:** A sequence of operations: `push(value)`, `get(index)`. **Output:** Correct value returned by `get()`; internal `size`/`capacity` inspectable for tests.

**Edge cases:**

- `get()` with an out-of-bounds index — should raise/return a clear error, not read garbage memory
- `push()` exactly at current capacity — must trigger resize (commonly ×2) *before* the write, not after
- Many pushes then many removals — decide whether to shrink capacity back down (and when)
- Pushing zero elements, then calling `get(0)` — should fail cleanly

**Suggested structure:**

```
dynamic-array/
├── dynamic_array.py
└── tests/
    └── test_dynamic_array.py   # capacity growth, bounds checks, amortized cost
```

---

## 4. Columnar Analytics Engine (T2)

**Input:** Rows of structured records (e.g., loaded from CSV) at ingest time; queries like `sum(column)`, `avg(column)`, `filter(column, condition)` at query time. **Output:** A single aggregate value, or a filtered set of row indices/records.

**Edge cases:**

- Column contains missing/null values — decide whether they're skipped or zero-filled in aggregates
- Query references a column name that doesn't exist — clear error, not a silent `None`
- Empty dataset — `sum` should return 0, `avg` should error or return `None` (division by zero)
- A numeric column containing one stray non-numeric value (dirty data) — fail loudly at load time, not silently at query time

**Suggested structure:**

```
columnar-engine/
├── loader.py         # reads CSV into column-oriented store
├── store.py          # column arrays + dtype handling
├── query.py          # sum/avg/filter operations
└── tests/
    └── test_query.py
```

---

## 5. String Utility Library (T1)

**Input:** A single string (reverse, palindrome check, compression) or a pair of strings (anagram check). **Output:** A boolean (palindrome/anagram) or a transformed string (reverse/compressed).

**Edge cases:**

- Empty string and single-character string — both are trivially palindromes
- Case sensitivity — decide and document whether `"Race car"` counts as a palindrome
- Unicode/multi-byte characters — reversing byte-by-byte vs. character-by-character gives different (wrong) results for some scripts
- Compression that would *expand* the string (e.g., `"abcdef"` under naive run-length encoding) — handle the "no benefit, keep original" case

**Suggested structure:**

```
string-utils/
├── reverse.py
├── palindrome.py
├── anagram.py
├── compress.py
└── tests/
    └── test_string_utils.py
```

---

## 6. Duplicate-Content Detector (T2)

**Input:** A folder of text documents (or two pasted texts for a quick check). **Output:** A list of document pairs with a similarity score above a threshold, plus the specific passages that matched.

**Edge cases:**

- Documents of very different lengths (a 200-word excerpt of a 5,000-word article) — length-normalize the score
- Legitimate short quotes/citations triggering a false positive — consider a minimum match-length before counting
- Very short documents (a tweet-length text) giving inflated similarity by chance — set a minimum document length
- Large document sets making all-pairs comparison O(n²) — use shingling + hashing (MinHash/LSH) to avoid full pairwise comparison

**Suggested structure:**

```
dup-detector/
├── ingest.py          # loads and normalizes documents
├── similarity.py      # shingling / hashing / comparison logic
├── report.py          # outputs flagged pairs above threshold
└── tests/
    └── test_similarity.py
```

---

## 7. Hash Table From Scratch (T1)

**Input:** A sequence of `put(key, value)`, `get(key)`, `delete(key)` operations. **Output:** Correct value from `get()`; consistent state after `delete()`; no data loss across an internal resize.

**Edge cases:**

- Two different keys hashing to the same bucket (collision) — must resolve via chaining or open addressing, not silently overwrite
- `delete()` on a key that was never inserted — should be a no-op or clear error, not a crash
- Load factor crossing a threshold (e.g., 0.7) — trigger resize + rehash of *all* existing entries, not just new ones
- Using a mutable object as a key — document that this is unsafe (hash could change after insertion) or disallow it

**Suggested structure:**

```
hash-table/
├── hash_table.py       # core structure: put/get/delete/resize
├── hash_functions.py   # your custom hash function(s)
└── tests/
    └── test_collisions.py   # forces collisions deliberately
```

---

## 8. URL Shortener / In-Memory Cache (T2)

**Input:** `POST /shorten {url}` → returns a short key. `GET /{key}` → redirects to or returns the original value. (Cache variant: `set(key, value, ttl)`, `get(key)`.) **Output:** A short URL string on create; a redirect/value on lookup, or a clear "not found or expired" response.

**Edge cases:**

- Generated short key collides with an existing one — retry generation or widen the keyspace
- TTL expiry — decide lazy (check on read, evict then) vs. active (background sweep) expiration, and be consistent
- `GET` for a key that was never created — 404, not a crash
- High concurrent write volume — the underlying hash table needs to be safe under concurrent access (locking or a concurrency-safe structure)

**Suggested structure:**

```
url-shortener/
├── server.py           # HTTP routes
├── store.py            # hash table + TTL logic
├── key_generator.py    # short key generation (hash-based or random)
└── tests/
    └── test_expiry.py
```

---