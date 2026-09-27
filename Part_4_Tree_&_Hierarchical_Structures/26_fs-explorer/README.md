# File-System Explorer (T2)

*Part 4 — Trees & Hierarchical Structures*

## Problem

A folder tree needs fast search without scanning every file linearly.

## Objective

Model folders/files as a tree; support search by name across the whole structure.

---

**Input:** A root path (or a synthetic in-memory file tree); a `search(name)` query. **Output:** Matching file/folder paths.

**Edge cases:**

- Symbolic links that point back up the tree, creating a cycle — this breaks the "it's a tree" assumption; must detect and avoid infinite traversal
- Permission-denied folders encountered mid-traversal — skip and continue, don't crash the whole search
- Case-sensitive vs. case-insensitive search (platform-dependent — decide and document)
- Empty folders
- A search term matching both a file name and a folder name

**Suggested structure:**

```
fs-explorer/
├── tree_builder.py   # builds an in-memory tree from a real or synthetic FS
├── search.py         # name-based search over the tree
└── tests/
    └── test_search.py   # cycle detection specifically
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
