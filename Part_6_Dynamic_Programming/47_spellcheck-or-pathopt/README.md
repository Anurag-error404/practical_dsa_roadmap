# Spell-Check / Path Optimizer (T2)

*Part 6 — Dynamic Programming*

## Problem

"Did you mean...?" needs a notion of how *close* two strings are, not just equal/unequal.

## Objective

Build a "did you mean" suggester using edit distance, or a grid robot avoiding obstacles at min cost.

---

Two directions for this slot — pick one:

### Direction A: Spell-Checker

**Input:** A dictionary of correct words; a misspelled word. **Output:** A ranked list of the closest dictionary words by edit distance.

**Edge cases:**

- The input word is already correctly spelled — should still return sensibly (e.g., itself as the top match)
- A large dictionary making per-query full edit-distance comparison against every entry too slow — note this as a known limitation, or note a prefix/BK-tree structure as a future optimization
- Multiple dictionary words tied at the same edit distance — return several, optionally ranked by frequency

### Direction B: Robot Path Optimizer

**Input:** A grid with obstacles and per-cell movement costs; start and end cells. **Output:** The minimum-cost path avoiding obstacles.

**Edge cases:**

- No path exists due to obstacles — report unreachable explicitly
- Zero-cost cells — decide whether these are allowed and how they interact with "shortest" path logic (could create ties)
- Start cell equals end cell

**Suggested structure:**

```
spellcheck-or-pathopt/
# Spell-check variant:
├── dictionary.py
├── edit_distance.py   # reused from Project 46
├── suggester.py       # ranks dictionary words by distance
└── tests/
    └── test_suggester.py

# Path-optimizer variant:
├── grid.py
├── cost_dp.py
└── tests/
    └── test_path_cost.py
```

---

## Run

Run inside the direction folder you keep:

```bash
pip install -r requirements.txt
pytest
```

Shared helpers in `../../_shared/` are already on the pytest path. For scripts: `PYTHONPATH=../../_shared python <script>.py`.

This slot has two directions (`A_spellcheck/`, `B_path-optimizer/`). Pick one and delete the other.
