# Mini Search Engine

*Type 3 — Capstones*

## Problem

Search needs to be fast, ranked, and forgiving of partial input — not just exact string match.

## Objective

Build search over a document set with autocomplete, ranked results, and exact-phrase matching.

---

**Combines:** Tries · Hashing · KMP/Rabin-Karp · Heaps · Sorting

**Input:** A document set to index; `query(text)` — phrase or keyword. **Output:** Ranked matching documents with snippet/match locations.

**Edge cases:**

- A query term appearing in zero documents — return empty, not an error
- A query mixing an exact phrase with loose keywords — decide how these combine (must-match phrase + optional keyword boost, or something simpler)
- A document set large enough that the inverted index must be built incrementally rather than all at once
- Autocomplete for a prefix with zero matches — empty list, not an error
- Two documents tied on relevance score — needs a defined tie-break for stable ranking

**Suggested structure:**

```
mini-search-engine/
├── indexer.py       # inverted index (hashing)
├── trie.py          # autocomplete over indexed terms
├── matcher.py       # KMP/Rabin-Karp for exact phrase matching within candidates
├── ranker.py        # heap-based top-K relevance ranking
├── query_api.py
└── tests/
    └── test_search_engine.py   # index + ranking + autocomplete together
```

---

## Scaffold notes

- `models.py` holds the dataclasses shared across modules, so every module speaks the same types.

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
