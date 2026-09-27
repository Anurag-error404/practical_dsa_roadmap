# DSA Project Specs — Part 2: Linear Structures

*Full spec for each project: input/output format, edge cases, suggested file structure*

---

## 9. Linked List Suite (T1)

**Input:** A sequence of operations: `insert(value, position)`, `delete(position)`, `reverse()`, `detect_cycle()`. **Output:** Correct list state after each op; boolean result for `detect_cycle()`.

**Edge cases:**

- Insert/delete at the head vs. the tail vs. the middle — head/tail are common off-by-one traps
- Insert/delete on an empty list, and delete down to an empty list
- Reversing a list with 0 or 1 nodes — should be a no-op, not an error
- Cycle detection: no cycle, a self-loop (last node points to itself), and a cycle starting mid-list (not at the head) — all three must be handled by the same detector

**Suggested structure:**

```
linked-list/
├── singly_linked_list.py
├── doubly_linked_list.py
└── tests/
    └── test_linked_list.py   # cycle detection variants, edge insert/delete
```

---

## 10. LRU Cache / Music Queue (T2)

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

## 11. Expression Evaluator (T1)

**Input:** A string expression, e.g. `"3 + 4 * 2 - (1 + 5)"`. **Output:** The evaluated numeric result (and, as an intermediate step, the postfix form).

**Edge cases:**

- Unbalanced parentheses — should raise a clear parse error, not crash mid-evaluation
- Operator precedence including `^` (exponent, right-associative — different from `+`/`-`/`*`/`/`)
- Unary minus, e.g. `"-3 + 5"` vs. binary minus in `"5 - 3"`
- Division by zero
- Multi-digit numbers and decimals (`"12.5 + 3"`), and inputs with inconsistent spacing

**Suggested structure:**

```
expr-evaluator/
├── tokenizer.py           # splits string into tokens
├── infix_to_postfix.py    # shunting-yard or equivalent
├── evaluator.py           # evaluates postfix using a stack
└── tests/
    └── test_evaluator.py
```

---

## 12. Browser-History / Undo-Redo (T2)

**Input:** `visit(url)` (or `action(state)`), `back()`, `forward()`. **Output:** The current page/state after each navigation call.

**Edge cases:**

- `back()` when there's nothing before the current page — no-op, not a crash
- `forward()` after a *new* visit was made following a `back()` — the forward history should be cleared (this is real browser behavior: you can't "redo" into a path you abandoned)
- Repeated `back()` calls past the very first page
- Visiting the same URL twice in a row — decide whether that pushes a new history entry or is a no-op

**Suggested structure:**

```
browser-history/
├── history.py         # two stacks: back_stack, forward_stack
└── tests/
    └── test_history.py   # forward-clearing behavior specifically
```

---

## 13. Circular Queue & Deque (T1)

**Input:** `enqueue(value)`, `dequeue()`. *(Deque adds `push_front`, `push_back`, `pop_front`, `pop_back`.)* **Output:** Correct FIFO order (or deque order); `is_full()` / `is_empty()` status.

**Edge cases:**

- `enqueue()` on a full circular queue — decide the policy (reject the write, or overwrite the oldest entry) and document it
- `dequeue()` on an empty queue
- Wraparound index math — front/rear pointers crossing past the end of the underlying array back to index 0 is where most bugs live
- Fixed-capacity vs. resizable circular queue — pick one and test exactly at the capacity boundary (n-1 items vs. n items)

**Suggested structure:**

```
queue-deque/
├── circular_queue.py
├── deque.py
└── tests/
    └── test_wraparound.py   # front/rear index math specifically
```

---

## 14. Job Processor / Sliding-Max Dashboard (T2)

Two directions for this slot — pick one:

### Direction A: Priority Job Processor

**Input:** `submit_job(priority)`, `process_next()`. **Output:** Jobs processed in priority order (highest first).

**Edge cases:**

- Multiple jobs with the same priority — decide tie-breaking (typically FIFO among equal priority)
- `process_next()` on an empty queue
- A job's priority changing after submission (priority queues don't support update-in-place natively — you'd need a workaround, e.g. lazy deletion)

**Suggested structure:**

```
job-processor/
├── job_queue.py         # heap-based priority queue
└── tests/
    └── test_priority_order.py   # tie-breaking behavior specifically
```

### Direction B: Sliding-Window-Max Dashboard

**Input:** A stream of `(timestamp, value)` events + a window size N. **Output:** The current max value within the last N events (or last N seconds).

**Edge cases:**

- Fewer than N events have arrived yet — the window is partial, not an error
- A value that was the max *leaves* the window — it must be evicted from the internal deque even though it's still the largest value seen overall
- Duplicate max values in the window — the deque needs to handle ties correctly on eviction, not just distinct values

**Suggested structure:**

```
sliding-max-dashboard/
├── sliding_window_max.py   # monotonic deque
├── stream_simulator.py     # generates the event feed for testing
└── tests/
    └── test_window_max.py
```

---