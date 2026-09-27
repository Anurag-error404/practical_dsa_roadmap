# Browser-History / Undo-Redo (T2)

*Part 2 — Linear Structures*

## Problem

"Go back" needs to remember exactly what came before, in order.

## Objective

Implement back/forward or undo/redo using two stacks (history + future).

---

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

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
