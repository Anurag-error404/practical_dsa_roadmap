# Linked List Suite (T1)

*Part 2 — Linear Structures*

## Problem

Arrays cost O(n) to insert/delete mid-sequence — sometimes you need O(1).

## Objective

Build singly + doubly linked lists: insert, delete, reverse, cycle detection.

---

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

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
