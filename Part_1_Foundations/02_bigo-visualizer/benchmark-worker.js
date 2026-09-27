/**
 * Web Worker. Receives { algorithmId, sizes, trials } and posts back one
 * { algorithmId, size, timeMs } message per completed size, so the UI thread never blocks.
 */
import { getAlgorithm } from "./algorithms.js";

/** Median wall time in ms of `trials` runs of algo at size n (fresh input per run). */
export function timeRun(algo, n, trials = 5) {
  const times = [];
  for (let i = 0; i < trials; i++) {
    const input = algo.makeInput(n);
    const t0 = performance.now();
    algo.run(input);
    times.push(performance.now() - t0);
  }
  times.sort((a, b) => a - b);
  return times[Math.floor(times.length / 2)];
}

if (typeof self !== "undefined" && typeof window === "undefined") {
  self.onmessage = ({ data: { algorithmId, sizes, trials } }) => {
    const algo = getAlgorithm(algorithmId);
    for (const size of sizes) {
      self.postMessage({ algorithmId, size, timeMs: timeRun(algo, size, trials) });
    }
  };
}
