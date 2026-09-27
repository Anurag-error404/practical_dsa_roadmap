# Multi-Criteria Sorter (T2)

*Part 3 — Core Algorithmic Patterns*

## Problem

Users want to sort files/playlists by name, then date, then a custom rule — not just one key.

## Objective

Build a sorter accepting custom comparators, or an external sort for a file bigger than memory.

---

**Input:** A list of items (files/playlist entries) with multiple attributes (name, date, size); a user-specified key order (e.g., "sort by date, then name"). **Output:** The list sorted by the specified multi-key order.

**Edge cases:**

- Ties on the primary key that need the secondary (and tertiary) key to break correctly
- User specifies a conflicting or duplicate key in the sort order
- Missing attribute values on some items (e.g., a file with no modified-date) — decide where these sort (first, last, or excluded)
- A file list large enough it doesn't fit in memory — needs an external sort (chunk, sort each chunk, merge from disk)

**Suggested structure:**

```
multi-criteria-sorter/
├── models.py           # item schema (name, date, size, ...)
├── comparator.py       # builds a composite comparator from key order
├── external_sort.py    # chunked sort-and-merge for large inputs
└── tests/
    └── test_comparator.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
