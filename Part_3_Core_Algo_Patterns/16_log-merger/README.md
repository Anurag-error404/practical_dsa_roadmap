# Log Merger (T2)

*Part 3 — Core Algorithmic Patterns*

## Problem

Logs from multiple servers, each sorted, need one merged chronological timeline.

## Objective

Merge N sorted log files into one ordered stream without loading everything into memory at once.

---

**Input:** N sorted log files (each line timestamp-prefixed) + an output path. **Output:** A single file with all lines merged in chronological order.

**Edge cases:**

- A file that *isn't* actually sorted internally — should be detected and flagged, not silently merged wrong
- Files large enough that none can be fully loaded into memory — needs a true k-way merge (read line-by-line, min-heap of "next line per file"), not "load everything, then sort"
- Duplicate timestamps across files — decide tie-breaking order (e.g., preserve file order as a secondary key)
- An empty input file, or a file list of size 1

**Suggested structure:**

```
log-merger/
├── parser.py       # extracts timestamp from a line
├── merger.py       # k-way merge using a min-heap
├── validator.py    # checks each input file is pre-sorted
└── tests/
    └── test_merge.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
