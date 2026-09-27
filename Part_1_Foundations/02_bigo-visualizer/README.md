# Big-O Visualizer (T2)

*Part 1 — Foundations*

## Problem

Big-O feels abstract until you can watch the gap widen live.

## Objective

Build a UI: pick algorithm + input size, render measured time as an interactive growth chart.

---

**Input:** User picks an algorithm from a list + an input size (or range) and triggers "run." **Output:** A live-updating chart of measured time vs. input size as runs complete.

**Edge cases:**

- Very large input size freezing the UI — run benchmarks off the main thread (worker/async)
- Comparing an O(n) and an O(n³) algorithm on the same linear axis (one looks flat) — offer a log-scale toggle
- User re-runs the same size — decide whether to overwrite or append as a new data point
- No algorithm selected yet — show an empty-state, not an error

**Suggested structure:**

```
bigo-visualizer/
├── algorithms.js          # registry of algorithm implementations
├── benchmark-worker.js    # runs timing off the main thread
├── chart.js               # renders results
└── index.html
```

---

## Scaffold notes

- JavaScript project with no dependencies. `package.json` exists only so `npm test` runs `node --test`.
- Added `tests/visualizer.test.js`; the suggested structure has no tests folder.

---

## Run

```bash
npm test                    # node --test, no dependencies
python3 -m http.server     # then open http://localhost:8000 (module workers need http://, not file://)
```
