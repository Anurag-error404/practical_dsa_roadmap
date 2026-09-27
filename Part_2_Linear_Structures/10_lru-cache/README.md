# LRU Cache / Music Queue (T2)

*Part 2 — Linear Structures*

## Problem

A cache with unlimited size eventually exhausts memory.

## Objective

Combine a linked list + hash map so both "most recent" and "lookup by key" are O(1).

---

**Input:** `get(key)`, `put(key, value)` against a fixed capacity. *(Music-queue variant: `add(song)`, `next()`, `prev()`, `shuffle()`.)* **Output:** `get()` returns the value or a clear "miss"; `put()` evicts the least-recently-used entry once over capacity.

**Edge cases:**

- Capacity of 0 or 1 — the smallest cases are where off-by-one eviction bugs live
- `put()` on a key that already exists — update its value *and* refresh its recency, don't create a duplicate entry
- `get()` on a key that was already evicted
- *(Music variant)* `shuffle()` shouldn't repeat a song until every other song has played once, unless the user explicitly wants repeats

**Suggested structure:**

```
lru-cache/
├── lru_cache.py       # doubly linked list + hash map combo
└── tests/
    └── test_eviction.py   # capacity edge cases, recency updates
```

---

## Scaffold notes

- The last test stub is for the music-queue variant. Delete it if you build the LRU cache.

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
