# BST From Scratch (T1)

*Part 4 — Trees & Hierarchical Structures*

## Problem

Keeping a growing dataset sorted via re-sorting on every insert is wasteful.

## Objective

Implement insert/delete/search + in/pre/post-order traversal; add a balance checker.

---

**Input:** `insert(value)`, `delete(value)`, `search(value)`; traversal requests (in/pre/post-order). **Output:** Correct traversal orderings; boolean from `search()`; a tree that remains a valid BST after every delete.

**Edge cases:**

- Deleting a node with 0, 1, or 2 children — the 2-children case (replace with in-order successor/predecessor) is where almost every BST bug lives
- Deleting the root node specifically
- Inserting a duplicate value — decide the policy (reject, insert as right child, or maintain a count) and be consistent
- `search()` on an empty tree
- Deleting a value that doesn't exist in the tree
- A degenerate tree (all left or all right children only, effectively a linked list) — your balance checker should correctly flag this

**Suggested structure:**

```
bst/
├── bst.py              # insert/delete/search
├── traversals.py       # in/pre/post-order
├── balance_checker.py  # height-based balance check
└── tests/
    └── test_bst.py     # all three delete cases, explicitly
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
