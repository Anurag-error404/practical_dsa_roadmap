# API Rate Limiter (T2)

*Part 3 — Core Algorithmic Patterns*

## Problem

An API needs to cap requests per rolling time window, not a fixed calendar window.

## Objective

Build real middleware enforcing "max N requests per rolling 60s" using a sliding window.

---

**Input:** Incoming requests, each with a client ID and timestamp; a configured limit (e.g., max N requests per rolling 60s). **Output:** Allow/deny decision per request.

**Edge cases:**

- A burst of requests arriving in the same millisecond
- Requests arriving slightly out of chronological order (network jitter/clock skew)
- Old timestamps need to be evicted from each client's window efficiently — not by rescanning full history on every check
- Every client needs an *independent* window — a shared global counter would incorrectly let one client's traffic block another's

**Suggested structure:**

```
rate-limiter/
├── middleware.py                # intercepts requests, consults the limiter
├── sliding_window_limiter.py    # per-client deque of timestamps
└── tests/
    └── test_rate_limit.py
```

---

## Scaffold notes

- `middleware.py` is finished WSGI plumbing (stdlib `wsgiref`, no framework). The algorithm lives in `sliding_window_limiter.py`.

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
