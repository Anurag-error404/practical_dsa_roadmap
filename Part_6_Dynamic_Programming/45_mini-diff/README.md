# Mini Diff Tool (T2)

*Part 6 — Dynamic Programming*

## Problem

Comparing two file versions line-by-line by eye doesn't scale past a few lines.

## Objective

Build a tool that outputs line-level insertions/deletions between two text files, like `git diff`.

---

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

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
