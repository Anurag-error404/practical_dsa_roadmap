# Autocomplete Engine (T2)

*Part 4 — Trees & Hierarchical Structures*

## Problem

Typing "pre" should surface matching words instantly, not after a full-dictionary scan.

## Objective

Build a live autocomplete/suggestion box backed by your trie.

---

**Input:** A preloaded dictionary of words; a partial string as the user types. **Output:** A ranked list of suggested completions.

**Edge cases:**

- No matches for the given prefix — return an empty list cleanly, not an error
- A very short prefix (single letter) matching thousands of words — cap the number of suggestions returned, and rank by something meaningful (frequency/popularity), since raw trie traversal order isn't inherently useful
- Case mismatch between user input and stored dictionary casing
- Updating suggestion ranking as words get "used" more over time (optional enhancement, not required for a working version)

**Suggested structure:**

```
autocomplete/
├── trie.py         # reuses/extends the trie from Project 29
├── ranker.py       # frequency-based suggestion ranking
├── api.py          # query(prefix) -> ranked suggestions
└── tests/
    └── test_autocomplete.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
