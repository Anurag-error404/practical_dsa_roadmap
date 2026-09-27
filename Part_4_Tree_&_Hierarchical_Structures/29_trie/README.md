# Trie From Scratch (T1)

*Part 4 — Trees & Hierarchical Structures*

## Problem

Checking "does any word start with 'pre-'" via a hash set means scanning all keys.

## Objective

Implement insert/search/prefix-search/delete on a trie.

---

**Input:** `insert(word)`, `search(word)`, `starts_with(prefix)`, `delete(word)`. **Output:** Boolean from `search()`/`starts_with()`; correct trie structure after `delete()`.

**Edge cases:**

- Deleting a word that is itself a prefix of another stored word — must *not* remove the shared nodes the other word still needs
- Inserting the empty string
- Case sensitivity (decide and document)
- A prefix that exists as an internal path but was never inserted as a complete word — `starts_with()` should return true, `search()` should return false for it
- Deleting a word that was never inserted

**Suggested structure:**

```
trie/
├── trie.py           # insert/search/starts_with/delete
└── tests/
    └── test_trie.py  # shared-prefix deletion specifically
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
