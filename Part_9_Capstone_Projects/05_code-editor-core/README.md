# Code Editor Core

*Type 3 — Capstones*

## Problem

A text editor needs efficient edits, reversible history, and smart suggestions simultaneously.

## Objective

Build a minimal editor: efficient text buffer, working undo/redo, find-and-replace, and autocomplete.

---

**Combines:** Linked Lists/Rope · Stacks · Tries · String Matching

**Input:** Text edits (insert/delete at cursor); `undo()`; `redo()`; `find(text)`; `replace(text, new_text)`. **Output:** Current buffer content; undo/redo result; find match positions; replace count.

**Edge cases:**

- Undo used, then a *new* edit is made — the redo stack must be cleared (same rule as the browser-history project), not left stale
- `find()` on an empty buffer or with an empty search string
- Replace-all where the replacement text itself contains the search text — a naive "find-and-replace repeatedly" approach can loop forever; must be done in a single pass over the original positions
- A file large enough that a plain array-based buffer is slow for mid-document inserts — worth documenting this trade-off even if you choose a simpler structure over a full rope
- Autocomplete triggering on a partial word with zero dictionary matches

**Suggested structure:**

```
code-editor-core/
├── text_buffer.py   # linked-list/rope-based buffer
├── undo_redo.py     # two-stack undo/redo, invalidated on new edit
├── trie.py          # autocomplete for known identifiers/words
├── search.py        # find/replace using string matching
└── tests/
    └── test_editor_core.py   # undo-after-redo-invalidation case, explicitly
```

---

## Scaffold notes

- `models.py` holds the dataclasses shared across modules, so every module speaks the same types.
- Added `editor.py` as the single entry point for the spec's insert/delete/undo/redo/find/replace API.

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
