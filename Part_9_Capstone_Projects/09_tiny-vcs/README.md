# Tiny Version Control Tool

*Type 3 — Capstones*

## Problem

Tracking every full copy of every file version wastes enormous space; diffing by eye doesn't scale.

## Objective

Build content-addressable storage for versions, a commit history graph, and a working diff between any two versions.

---

**Combines:** Hashing · Graphs/Trees · Topological Sort · LCS

**Input:** `commit(files_snapshot, message)`, `diff(commit_a, commit_b)`, `checkout(commit_id)`. **Output:** A stored commit graph; a diff report between any two commits; restored file state at checkout.

**Edge cases:**

- Committing content identical to what's already stored — should reuse the existing content-hash/blob rather than storing a duplicate (this is literally how Git's content-addressable storage works — worth testing explicitly)
- Diffing two commits with no direct linear history between them — must still produce a valid diff via LCS, regardless of branch topology
- Checking out a commit ID that doesn't exist — clear error, not corrupted state
- A commit with zero file changes from its parent — still a valid, storable commit
- Very large files making LCS-based diffing slow — document this as a real, known limitation (production diff tools fall back to heuristics for exactly this reason)

**Suggested structure:**

```
tiny-vcs/
├── blob_store.py      # content-addressable storage (hash -> content)
├── commit_graph.py    # DAG of commits, parent pointers
├── diff_engine.py     # LCS-based diff between any two commits
├── checkout.py        # restores file state from a commit
└── tests/
    └── test_vcs.py    # duplicate-content dedup, unrelated-commit diff
```

---

## Scaffold notes

- `models.py` holds the dataclasses shared across modules, so every module speaks the same types.
- Added `repo.py` as the single entry point for commit/diff/checkout.

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
