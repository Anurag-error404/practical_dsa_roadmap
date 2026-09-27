import { test } from "node:test";
import assert from "node:assert/strict";

import { ALGORITHMS, getAlgorithm } from "../algorithms.js";
import { timeRun } from "../benchmark-worker.js";
import { GrowthChart } from "../chart.js";

test("large sizes run off the main thread so the UI never freezes", () => {
  // TODO: Very large input size freezing the UI — run benchmarks off the main thread
  //       (worker/async)
});

test("log-scale toggle keeps fast and slow curves both readable", () => {
  // TODO: Comparing an O(n) and an O(n³) algorithm on the same linear axis (one looks flat) —
  //       offer a log-scale toggle
});

test("re-running an existing size follows the overwrite-or-append policy", () => {
  // TODO: User re-runs the same size — decide whether to overwrite or append as a new data
  //       point
});

test("no algorithm selected shows an empty state, not an error", () => {
  // TODO: No algorithm selected yet — show an empty-state, not an error
});
