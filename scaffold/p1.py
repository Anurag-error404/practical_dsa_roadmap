from dsl import P

SHARED = {
    "bench_harness.py": r'''
        """Timing harness shared by Part 1 projects. Measurement plumbing only, no algorithm logic.

        Usage:
            @timed(trials=5)
            def run(xs): ...
            result, median_ms = run(data)

            ms = measure(fn, data, trials=5)
            write_rows("results.csv", [{"input_size": 1000, "algorithm": "hash", "time_ms": ms}])
        """
        import csv
        import statistics
        import time
        from collections.abc import Callable, Iterable
        from functools import wraps
        from pathlib import Path

        FIELDS = ("input_size", "algorithm", "time_ms")


        def measure(fn: Callable, *args, trials: int = 5, warmup: int = 1, setup: Callable[[], tuple] | None = None, **kwargs) -> float:
            """Median wall time of fn(*args, **kwargs) in milliseconds.

            `warmup` untimed runs happen first (cache/JIT noise). If `setup` is given it is called
            before every run and its returned tuple replaces `args`; use it when fn mutates its input.
            """
            def once() -> float:
                call_args = setup() if setup else args
                t0 = time.perf_counter()
                fn(*call_args, **kwargs)
                return (time.perf_counter() - t0) * 1000

            for _ in range(warmup):
                once()
            return statistics.median(once() for _ in range(max(1, trials)))


        def timed(trials: int = 5, warmup: int = 1):
            """Decorator: the wrapped fn returns (result, median_ms) instead of result."""
            def deco(fn: Callable):
                @wraps(fn)
                def wrapper(*args, **kwargs):
                    ms = measure(fn, *args, trials=trials, warmup=warmup, **kwargs)
                    return fn(*args, **kwargs), ms
                return wrapper
            return deco


        def write_rows(path: str | Path, rows: Iterable[dict], fieldnames: Iterable[str] = FIELDS, append: bool = False) -> None:
            """Write dict rows to CSV. Header is written unless appending to a non-empty file."""
            path = Path(path)
            fieldnames = list(fieldnames)
            needs_header = not (append and path.exists() and path.stat().st_size > 0)
            with path.open("a" if append else "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=fieldnames)
                if needs_header:
                    w.writeheader()
                w.writerows(rows)


        def read_rows(path: str | Path) -> list[dict]:
            with Path(path).open(newline="") as f:
                return list(csv.DictReader(f))


        if __name__ == "__main__":
            import tempfile

            calls = []
            assert measure(lambda: calls.append(1), trials=3, warmup=2) >= 0 and len(calls) == 5
            fresh = []
            measure(lambda xs: xs.append(0) or fresh.append(len(xs)), trials=3, warmup=0, setup=lambda: ([],))
            assert fresh == [1, 1, 1], fresh
            assert timed(trials=2)(lambda x: x * 2)(21)[0] == 42
            with tempfile.TemporaryDirectory() as d:
                p = Path(d) / "r.csv"
                write_rows(p, [{"input_size": 1, "algorithm": "a", "time_ms": 0.5}])
                write_rows(p, [{"input_size": 2, "algorithm": "b", "time_ms": 1.5}], append=True)
                assert [r["algorithm"] for r in read_rows(p)] == ["a", "b"]
            print("bench_harness ok")
    ''',
}

PROJECTS = [
    P(1, "complexity-bench", {
        "algorithms/naive_dedupe.py": r'''
            def naive_dedupe(items: list) -> list:
                """O(n^2) dedupe: return `items` with duplicates removed.

                Compare each item against everything kept so far. No set/dict.
                Must return exactly what hash_dedupe returns for the same input.
                """
                raise NotImplementedError
        ''',
        "algorithms/hash_dedupe.py": r'''
            def hash_dedupe(items: list) -> list:
                """O(n) dedupe: return `items` with duplicates removed, using hashing.

                Must return exactly what naive_dedupe returns for the same input.
                """
                raise NotImplementedError
        ''',
        "bench.py": r'''
            """Runs each algorithm across input sizes and records timing to results.csv."""
            import random
            from collections.abc import Callable
            from pathlib import Path

            from algorithms.hash_dedupe import hash_dedupe
            from algorithms.naive_dedupe import naive_dedupe
            from bench_harness import measure, write_rows

            ALGORITHMS: dict[str, Callable[[list], list]] = {"naive": naive_dedupe, "hash": hash_dedupe}
            SIZES = [10**3, 10**5, 10**7]
            RESULTS = Path(__file__).parent / "results.csv"


            def make_input(size: int, seed: int = 0) -> list[int]:
                """`size` random ints drawn from [0, size), so roughly a third are duplicates."""
                rng = random.Random(seed)
                return [rng.randrange(max(size, 1)) for _ in range(size)]


            def run(sizes: list[int], algorithms: dict[str, Callable], trials: int = 5) -> list[dict]:
                """Time every algorithm at every size.

                Returns rows of {"input_size", "algorithm", "time_ms"} (median of `trials`).
                """
                raise NotImplementedError


            def main() -> None:
                write_rows(RESULTS, run(SIZES, ALGORITHMS))


            if __name__ == "__main__":
                main()
        ''',
        "results.csv": "input_size,algorithm,time_ms\n",
        "plot.py": r'''
            """Optional: renders the growth curve from results.csv."""
            from pathlib import Path

            from bench_harness import read_rows

            RESULTS = Path(__file__).parent / "results.csv"


            def plot(rows: list[dict], log_scale: bool = False, out: str | None = None) -> None:
                """Plot time_ms against input_size, one line per algorithm. Save to `out` or show."""
                raise NotImplementedError


            if __name__ == "__main__":
                plot(read_rows(RESULTS))
        ''',
    }, "tests/test_bench.py", [
        "test_quadratic_algorithm_capped_at_large_sizes",
        "test_timing_reports_median_of_multiple_trials",
        "test_empty_input_runs_without_error",
        "test_unordered_input_sizes_handled",
    ], requirements=["matplotlib  # plot.py only"],
       notes=["Added `tests/test_bench.py`; the suggested structure has no tests folder.",
              "`bench.py` and `plot.py` use the shared timing harness in `../_shared/bench_harness.py`."]),

    P(2, "bigo-visualizer", {
        "algorithms.js": r'''
            /**
             * Registry of benchmarkable algorithms.
             * Each entry: { id, label, complexity, makeInput(n) -> input, run(input) -> any }
             */
            export const ALGORITHMS = [];

            /** @param {string} id */
            export function getAlgorithm(id) {
              return ALGORITHMS.find((a) => a.id === id);
            }
        ''',
        "benchmark-worker.js": r'''
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
        ''',
        "chart.js": r'''
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
        ''',
        "index.html": r'''
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8" />
                <title>Big-O Visualizer</title>
              </head>
              <body>
                <label>Algorithm <select id="algorithm"></select></label>
                <label>Input sizes (comma-separated) <input id="sizes" value="1000,10000,100000" /></label>
                <label><input type="checkbox" id="log-scale" /> Log scale</label>
                <button id="run">Run</button>
                <canvas id="chart" width="800" height="400"></canvas>

                <script type="module">
                  import { ALGORITHMS } from "./algorithms.js";
                  import { GrowthChart } from "./chart.js";

                  const select = document.getElementById("algorithm");
                  for (const a of ALGORITHMS) select.add(new Option(a.label, a.id));

                  const chart = new GrowthChart(document.getElementById("chart"));
                  const worker = new Worker("./benchmark-worker.js", { type: "module" });
                  worker.onmessage = ({ data }) => {
                    chart.addPoint(data.algorithmId, data.size, data.timeMs);
                    chart.render();
                  };

                  document.getElementById("log-scale").onchange = (e) => {
                    chart.setLogScale(e.target.checked);
                    chart.render();
                  };
                  document.getElementById("run").onclick = () => {
                    const sizes = document.getElementById("sizes").value.split(",").map(Number);
                    worker.postMessage({ algorithmId: select.value, sizes, trials: 5 });
                  };
                  chart.render();
                </script>
              </body>
            </html>
        ''',
        "package.json": r'''
            {
              "name": "bigo-visualizer",
              "private": true,
              "type": "module",
              "scripts": {
                "test": "node --test"
              }
            }
        ''',
    }, "tests/visualizer.test.js", [
        "large sizes run off the main thread so the UI never freezes",
        "log-scale toggle keeps fast and slow curves both readable",
        "re-running an existing size follows the overwrite-or-append policy",
        "no algorithm selected shows an empty state, not an error",
    ], js=True, extra_imports=[
        'import { ALGORITHMS, getAlgorithm } from "../algorithms.js";',
        'import { timeRun } from "../benchmark-worker.js";',
        'import { GrowthChart } from "../chart.js";',
    ], notes=["JavaScript project with no dependencies. `package.json` exists only so `npm test` runs `node --test`.",
              "Added `tests/visualizer.test.js`; the suggested structure has no tests folder."]),

    P(3, "dynamic-array", {
        "dynamic_array.py": r'''
            from typing import Any


            class DynamicArray:
                """Resizable array on a fixed-size backing block (e.g. `[None] * capacity`). No list growth."""

                def __init__(self, capacity: int = 1):
                    """Start empty with the given backing capacity."""
                    raise NotImplementedError

                @property
                def size(self) -> int:
                    """Number of stored elements."""
                    raise NotImplementedError

                @property
                def capacity(self) -> int:
                    """Length of the backing block."""
                    raise NotImplementedError

                def push(self, value: Any) -> None:
                    """Append in amortized O(1). At size == capacity, resize (commonly x2) before the write."""
                    raise NotImplementedError

                def get(self, index: int) -> Any:
                    """Element at index. Out-of-bounds must raise a clear error, never read stale slots."""
                    raise NotImplementedError

                def pop(self) -> Any:
                    """Remove and return the last element. Whether/when capacity shrinks is your policy."""
                    raise NotImplementedError

                def __len__(self) -> int:
                    raise NotImplementedError
        ''',
    }, "tests/test_dynamic_array.py", [
        "test_get_out_of_bounds_raises_clear_error",
        "test_push_at_capacity_resizes_before_write",
        "test_capacity_policy_after_many_removals",
        "test_get_zero_on_empty_array_fails_cleanly",
    ], extra_imports=["from bench_harness import measure"]),

    P(4, "columnar-engine", {
        "loader.py": r'''
            """Reads CSV into a column-oriented store."""
            from pathlib import Path

            from store import ColumnStore


            def load_csv(path: str | Path) -> ColumnStore:
                """Load CSV rows into a ColumnStore.

                Dirty data (a stray non-numeric value in a numeric column) must fail loudly here,
                not later at query time.
                """
                raise NotImplementedError
        ''',
        "store.py": r'''
            """Column arrays plus dtype handling."""
            from typing import Any


            class ColumnStore:
                def __init__(self):
                    raise NotImplementedError

                def add_column(self, name: str, values: list, dtype: type) -> None:
                    """Register a column. All columns must have the same length."""
                    raise NotImplementedError

                def column(self, name: str) -> list:
                    """The values of a column. Unknown names must raise a clear error, not return None."""
                    raise NotImplementedError

                def dtype(self, name: str) -> type:
                    raise NotImplementedError

                @property
                def columns(self) -> list[str]:
                    raise NotImplementedError

                def row(self, index: int) -> dict[str, Any]:
                    """Reassemble one record, for returning filter results."""
                    raise NotImplementedError

                def __len__(self) -> int:
                    """Row count."""
                    raise NotImplementedError
        ''',
        "query.py": r'''
            """sum/avg/filter over a single column."""
            from collections.abc import Callable
            from typing import Any

            from store import ColumnStore


            def col_sum(store: ColumnStore, column: str) -> float:
                """Sum of a column. An empty dataset sums to 0."""
                raise NotImplementedError


            def col_avg(store: ColumnStore, column: str) -> float | None:
                """Average of a column. Empty dataset: error or None, your call."""
                raise NotImplementedError


            def col_filter(store: ColumnStore, column: str, predicate: Callable[[Any], bool]) -> list[int]:
                """Row indices whose value in `column` satisfies `predicate`."""
                raise NotImplementedError
        ''',
    }, "tests/test_query.py", [
        "test_null_values_policy_in_aggregates",
        "test_unknown_column_raises_clear_error",
        "test_empty_dataset_sum_zero_avg_undefined",
        "test_dirty_numeric_column_fails_at_load_time",
    ]),

    P(5, "string-utils", {
        "reverse.py": r'''
            def reverse(s: str) -> str:
                """Reverse s character by character (not byte by byte). No slicing tricks or reversed()."""
                raise NotImplementedError
        ''',
        "palindrome.py": r'''
            def is_palindrome(s: str) -> bool:
                """True if s reads the same both ways. Document your case/whitespace policy."""
                raise NotImplementedError
        ''',
        "anagram.py": r'''
            def is_anagram(a: str, b: str) -> bool:
                """True if a and b use exactly the same characters with the same counts."""
                raise NotImplementedError
        ''',
        "compress.py": r'''
            def rle_compress(s: str) -> str:
                """Run-length encode s (e.g. "aaab" -> "a3b1"). If encoding wouldn't shrink it, keep the original."""
                raise NotImplementedError
        ''',
    }, "tests/test_string_utils.py", [
        "test_empty_and_single_char_are_palindromes",
        "test_case_sensitivity_policy_documented",
        "test_unicode_reversed_by_character_not_byte",
        "test_compression_keeps_original_when_no_benefit",
    ]),

    P(6, "dup-detector", {
        "ingest.py": r'''
            """Loads and normalizes documents."""
            from pathlib import Path


            def load_documents(folder: str | Path) -> dict[str, str]:
                """Map document name to raw text for every document in `folder`."""
                raise NotImplementedError


            def normalize(text: str) -> str:
                """Canonical form used for comparison (casing, punctuation, whitespace)."""
                raise NotImplementedError
        ''',
        "similarity.py": r'''
            """Shingling, hashing, and comparison logic."""


            def shingles(text: str, k: int = 5) -> set:
                """The k-shingles (overlapping k-word or k-char windows) of normalized text."""
                raise NotImplementedError


            def similarity(a: set, b: set) -> float:
                """Score in [0, 1] for two shingle sets, normalized for length differences."""
                raise NotImplementedError


            def find_similar_pairs(docs: dict[str, str], threshold: float) -> list[tuple[str, str, float]]:
                """(doc_a, doc_b, score) for every pair scoring >= threshold, without an all-pairs scan."""
                raise NotImplementedError


            def matching_passages(a: str, b: str, min_length: int) -> list[str]:
                """Passages shared by a and b that are at least `min_length` long."""
                raise NotImplementedError
        ''',
        "report.py": r'''
            """Outputs flagged pairs above threshold."""


            def format_report(pairs: list[tuple[str, str, float]], passages: dict[tuple[str, str], list[str]]) -> str:
                """Human-readable list of flagged pairs, their scores, and the matched passages."""
                raise NotImplementedError
        ''',
    }, "tests/test_similarity.py", [
        "test_length_normalized_score_for_excerpt_vs_full",
        "test_short_quotes_below_min_match_length_ignored",
        "test_very_short_documents_not_flagged",
        "test_large_set_avoids_all_pairs_comparison",
    ]),

    P(7, "hash-table", {
        "hash_table.py": r'''
            """Core structure: put/get/delete/resize."""
            from typing import Any

            from hash_functions import hash_key


            class HashTable:
                def __init__(self, capacity: int = 8):
                    """Initialize with given capacity. Resize when load factor exceeds ~0.7."""
                    raise NotImplementedError

                def put(self, key, value: Any) -> None:
                    """Insert or update. Must resolve collisions (chaining or open addressing)."""
                    raise NotImplementedError

                def get(self, key) -> Any:
                    """Return value for key, or raise/return sentinel if not found."""
                    raise NotImplementedError

                def delete(self, key) -> None:
                    """Remove key. Missing key: no-op or clear error, never a crash."""
                    raise NotImplementedError

                @property
                def capacity(self) -> int:
                    raise NotImplementedError

                @property
                def load_factor(self) -> float:
                    raise NotImplementedError

                def __len__(self) -> int:
                    raise NotImplementedError

                def __contains__(self, key) -> bool:
                    raise NotImplementedError
        ''',
        "hash_functions.py": r'''
            """Your custom hash function(s)."""


            def hash_key(key, capacity: int) -> int:
                """Map key to a bucket index in [0, capacity). Your own function."""
                raise NotImplementedError
        ''',
    }, "tests/test_collisions.py", [
        "test_collision_is_resolved_not_overwritten",
        "test_delete_missing_key_is_noop_or_clear_error",
        "test_resize_preserves_all_entries",
        "test_mutable_key_policy_documented",
    ]),

    P(8, "url-shortener", {
        "server.py": r'''
            """HTTP routes (stdlib only): POST /shorten {"url": ...} -> short key; GET /<key> -> redirect."""
            from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

            from key_generator import generate_key
            from store import TTLStore

            class ShortenerHandler(BaseHTTPRequestHandler):
                store: TTLStore

                def do_POST(self) -> None:
                    """/shorten: read JSON {"url"}, store under a fresh key, respond with the short key."""
                    raise NotImplementedError

                def do_GET(self) -> None:
                    """/<key>: redirect (or return the value). Unknown or expired key -> 404."""
                    raise NotImplementedError


            def run(host: str = "127.0.0.1", port: int = 8000) -> None:
                ShortenerHandler.store = TTLStore()
                ThreadingHTTPServer((host, port), ShortenerHandler).serve_forever()


            if __name__ == "__main__":
                run()
        ''',
        "store.py": r'''
            """Hash table plus TTL logic. Must be safe under concurrent access (ThreadingHTTPServer)."""
            import time
            from collections.abc import Callable
            from typing import Any


            class TTLStore:
                def __init__(self, clock: Callable[[], float] = time.monotonic):
                    """`clock` is injectable so tests can fake time passing."""
                    raise NotImplementedError

                def set(self, key: str, value: Any, ttl: float | None = None) -> None:
                    """Store value; ttl in seconds, None = never expires."""
                    raise NotImplementedError

                def get(self, key: str) -> Any:
                    """Value for key, or a clear not-found result if missing or expired."""
                    raise NotImplementedError

                def delete(self, key: str) -> None:
                    raise NotImplementedError

                def __contains__(self, key: str) -> bool:
                    raise NotImplementedError
        ''',
        "key_generator.py": r'''
            """Short key generation (hash-based or random)."""


            def generate_key(url: str, length: int = 7, attempt: int = 0) -> str:
                """A short key for url. `attempt` lets the caller retry after a collision."""
                raise NotImplementedError
        ''',
    }, "tests/test_expiry.py", [
        "test_key_collision_retries_or_widens_keyspace",
        "test_ttl_expiration_policy_is_consistent",
        "test_get_unknown_key_returns_not_found",
        "test_concurrent_writes_are_safe",
    ]),
]
