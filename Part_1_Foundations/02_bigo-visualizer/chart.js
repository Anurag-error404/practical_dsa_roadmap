/** Renders measured (size, timeMs) points as one growth curve per algorithm. */
export class GrowthChart {
  /** @param {HTMLCanvasElement} canvas */
  constructor(canvas) {
    throw new Error("Not implemented");
  }

  /** Record a measured point for an algorithm. */
  addPoint(algorithmId, size, timeMs) {
    throw new Error("Not implemented");
  }

  /** Switch the y-axis between linear and log scale. */
  setLogScale(enabled) {
    throw new Error("Not implemented");
  }

  clear() {
    throw new Error("Not implemented");
  }

  /** Draw the current state, including an empty state when there is no data. */
  render() {
    throw new Error("Not implemented");
  }
}
