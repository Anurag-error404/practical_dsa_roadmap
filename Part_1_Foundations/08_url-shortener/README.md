# URL Shortener / In-Memory Cache (T2)

*Part 1 — Foundations*

## Problem

Long URLs (or slow repeated lookups) need an O(1) short-key system.

## Objective

Generate short keys via hashing; support create/lookup/expiry (TTL) end-to-end.

---

**Input:** `POST /shorten {url}` → returns a short key. `GET /{key}` → redirects to or returns the original value. (Cache variant: `set(key, value, ttl)`, `get(key)`.) **Output:** A short URL string on create; a redirect/value on lookup, or a clear "not found or expired" response.

**Edge cases:**

- Generated short key collides with an existing one — retry generation or widen the keyspace
- TTL expiry — decide lazy (check on read, evict then) vs. active (background sweep) expiration, and be consistent
- `GET` for a key that was never created — 404, not a crash
- High concurrent write volume — the underlying hash table needs to be safe under concurrent access (locking or a concurrency-safe structure)

**Suggested structure:**

```
url-shortener/
├── server.py           # HTTP routes
├── store.py            # hash table + TTL logic
├── key_generator.py    # short key generation (hash-based or random)
└── tests/
    └── test_expiry.py
```

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../_shared python <script>.py`.
