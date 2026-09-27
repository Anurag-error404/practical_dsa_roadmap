# KMP & Rabin-Karp (T1)

*Part 8 — Advanced Topics*

## Problem

Naive substring search is O(n·m) — checking every position character-by-character.

## Objective

Implement both algorithms; verify they match brute-force results but run faster on large text.

---

**Input:** A text string + a pattern string. **Output:** All starting indices where the pattern occurs in the text.

**Edge cases:**

- Pattern longer than the text — no matches possible, return empty, not an error
- A pattern that overlaps itself in the text (e.g., `"aa"` in `"aaaa"`) — must find *all* overlapping matches, not skip past them
- An empty pattern — decide the convention (matches everywhere, or explicitly rejected) and document it
- Rabin-Karp: a hash collision that isn't an actual character match (a "spurious hit") — must be verified with a direct character comparison before confirming, or the algorithm will report false positives

**Suggested structure:**

```
string-matching/
├── kmp.py          # failure function + search
├── rabin_karp.py   # rolling hash + spurious-hit verification
└── tests/
    └── test_matching.py   # overlapping matches, spurious-hit case, explicitly
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
