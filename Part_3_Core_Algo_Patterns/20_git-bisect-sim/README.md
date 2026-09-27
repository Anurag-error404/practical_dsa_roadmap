# Git-Bisect Simulator (T2)

*Part 3 — Core Algorithmic Patterns*

## Problem

Finding which of 1,000 commits introduced a bug by checking each one is too slow.

## Objective

Simulate bisecting a commit history to find the first "bad" commit in O(log n) checks.

---

**Input:** A mock, ordered commit history where each commit is secretly marked good/bad, exposed only through a `test_commit(id)` function the algorithm can call. **Output:** The first bad commit, and the number of `test_commit()` calls used to find it.

**Edge cases:**

- The very first commit is already bad — no "good" baseline exists
- The very last commit is the first bad one
- History of length 1
- The history has a bad commit followed by more bad commits — must find the *first transition point*, not just any bad commit encountered

**Suggested structure:**

```
git-bisect-sim/
├── commit_history.py   # generates a mock history with a hidden bad commit
├── bisect.py            # binary-search-based bisection algorithm
└── tests/
    └── test_bisect.py   # asserts call count is O(log n)
```

---

## Scaffold notes

- `bisect.py` is renamed to `git_bisect.py` because a local `bisect.py` shadows the stdlib `bisect` module (which `random` imports).
- `commit_history.py` is finished test plumbing. `find_first_bad` is yours.

---

## Run

Run from this folder:

```bash
pip install -r requirements.txt
pytest
```
