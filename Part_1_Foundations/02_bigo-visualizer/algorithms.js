/**
 * Registry of benchmarkable algorithms.
 * Each entry: { id, label, complexity, makeInput(n) -> input, run(input) -> any }
 */
export const ALGORITHMS = [];

/** @param {string} id */
export function getAlgorithm(id) {
  return ALGORITHMS.find((a) => a.id === id);
}
