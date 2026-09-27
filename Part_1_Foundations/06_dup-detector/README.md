# Duplicate-Content Detector (T2)

*Part 1 — Foundations*

## Problem

Near-duplicate text (plagiarism, spun content) evades exact-match checks.

## Objective

Flag paragraphs across documents that are suspiciously similar, not just identical.

---

**Input:** A folder of text documents (or two pasted texts for a quick check). **Output:** A list of document pairs with a similarity score above a threshold, plus the specific passages that matched.

**Edge cases:**

- Documents of very different lengths (a 200-word excerpt of a 5,000-word article) — length-normalize the score
- Legitimate short quotes/citations triggering a false positive — consider a minimum match-length before counting
- Very short documents (a tweet-length text) giving inflated similarity by chance — set a minimum document length
- Large document sets making all-pairs comparison O(n²) — use shingling + hashing (MinHash/LSH) to avoid full pairwise comparison

**Suggested structure:**

```
dup-detector/
├── ingest.py          # loads and normalizes documents
├── similarity.py      # shingling / hashing / comparison logic
├── report.py          # outputs flagged pairs above threshold
└── tests/
    └── test_similarity.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
