# Columnar Analytics Engine (T2)

*Part 1 — Foundations*

## Problem

Aggregating a large dataset by scanning rows one at a time doesn't scale.

## Objective

Store data column-wise; support fast sum/avg/filter over a chosen column.

---

**Input:** Rows of structured records (e.g., loaded from CSV) at ingest time; queries like `sum(column)`, `avg(column)`, `filter(column, condition)` at query time. **Output:** A single aggregate value, or a filtered set of row indices/records.

**Edge cases:**

- Column contains missing/null values — decide whether they're skipped or zero-filled in aggregates
- Query references a column name that doesn't exist — clear error, not a silent `None`
- Empty dataset — `sum` should return 0, `avg` should error or return `None` (division by zero)
- A numeric column containing one stray non-numeric value (dirty data) — fail loudly at load time, not silently at query time

**Suggested structure:**

```
columnar-engine/
├── loader.py         # reads CSV into column-oriented store
├── store.py          # column arrays + dtype handling
├── query.py          # sum/avg/filter operations
└── tests/
    └── test_query.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
