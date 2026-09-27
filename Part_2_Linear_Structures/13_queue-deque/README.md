# Circular Queue & Deque (T1)

*Part 2 — Linear Structures*

## Problem

A naive queue wastes array space as items are dequeued from the front.

## Objective

Implement a circular queue and a deque supporting O(1) operations at both ends.

---

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

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
