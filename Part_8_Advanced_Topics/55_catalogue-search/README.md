# Catalogue Search Tool (T2)

*Part 8 — Advanced Topics*

## Problem

Finding every occurrence of a term across 10,000 documents by naive scan is too slow to feel interactive.

## Objective

Build a fast "find all occurrences of X" search over a large document set.

---

**Input:** A large document set (e.g., 10,000 files); a search term or phrase query. **Output:** Documents containing the term, with match positions/counts, ranked by relevance.

**Edge cases:**

- Search term found in zero documents — return an empty result, not an error
- A very common term appearing in nearly every document — ranking still needs to mean something (e.g., frequency-based scoring, not just presence/absence)
- Whole-word vs. partial-word matching (should `"cat"` match `"category"`?) — decide and document
- Documents added/updated after the initial index is built — decide whether incremental re-indexing is supported, or a full rebuild is required
- A document set large enough that a linear scan per query is too slow — build an inverted index upfront rather than searching each document at query time

**Suggested structure:**

```
catalogue-search/
├── indexer.py             # builds an inverted index across documents
├── kmp_or_rabinkarp.py    # reused from Project 54, for exact matching within docs
├── ranker.py              # scores/ranks results
├── query_api.py
└── tests/
    └── test_search.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
