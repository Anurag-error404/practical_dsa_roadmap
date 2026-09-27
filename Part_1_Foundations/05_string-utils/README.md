# String Utility Library (T1)

*Part 1 — Foundations*

## Problem

You call `.reverse()`/`.isPalindrome()` without knowing what's underneath.

## Objective

Implement reverse, palindrome check, anagram check, run-length compression — no built-ins.

---

**Input:** A single string (reverse, palindrome check, compression) or a pair of strings (anagram check). **Output:** A boolean (palindrome/anagram) or a transformed string (reverse/compressed).

**Edge cases:**

- Empty string and single-character string — both are trivially palindromes
- Case sensitivity — decide and document whether `"Race car"` counts as a palindrome
- Unicode/multi-byte characters — reversing byte-by-byte vs. character-by-character gives different (wrong) results for some scripts
- Compression that would *expand* the string (e.g., `"abcdef"` under naive run-length encoding) — handle the "no benefit, keep original" case

**Suggested structure:**

```
string-utils/
├── reverse.py
├── palindrome.py
├── anagram.py
├── compress.py
└── tests/
    └── test_string_utils.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
