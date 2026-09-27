from dsl import P

PROJECTS = [
    P(15, "two-pointer-toolkit", {
        "merge_sorted.py": r'''
            def merge_sorted(a: list, b: list) -> list:
                """Merge two ascending lists into one ascending list in O(len(a) + len(b))."""
                raise NotImplementedError
        ''',
        "remove_duplicates.py": r'''
            def remove_duplicates(nums: list) -> int:
                """Dedupe a sorted list in place. Return the new logical length k (nums[:k] is the result)."""
                raise NotImplementedError
        ''',
        "container_with_water.py": r'''
            def max_area(heights: list[int]) -> int:
                """Max water held between two lines: (j - i) * min(heights[i], heights[j]), in O(n)."""
                raise NotImplementedError
        ''',
    }, "tests/test_two_pointer.py", [
        "test_merge_with_one_or_both_empty",
        "test_dedup_all_duplicates_gives_length_one",
        "test_container_all_equal_heights_area_from_width",
        "test_container_length_zero_or_one_has_no_pair",
    ]),

    P(16, "log-merger", {
        "parser.py": r'''
            """Extracts the timestamp from a log line."""


            def parse_timestamp(line: str):
                """Sortable timestamp from the line's prefix."""
                raise NotImplementedError
        ''',
        "merger.py": r'''
            """K-way merge using a min-heap."""
            import argparse
            from pathlib import Path

            from parser import parse_timestamp
            from validator import check_sorted


            def merge_logs(paths: list[Path], out_path: Path) -> int:
                """Stream-merge sorted log files into out_path, line by line (never load a whole file).

                Returns the number of lines written.
                """
                raise NotImplementedError


            def main(argv: list[str] | None = None) -> None:
                ap = argparse.ArgumentParser(description="Merge N sorted log files into one chronological file.")
                ap.add_argument("inputs", nargs="+", type=Path, help="sorted log files")
                ap.add_argument("-o", "--output", type=Path, required=True)
                args = ap.parse_args(argv)
                print(f"wrote {merge_logs(args.inputs, args.output)} lines to {args.output}")


            if __name__ == "__main__":
                main()
        ''',
        "validator.py": r'''
            """Checks each input file is pre-sorted."""
            from pathlib import Path


            def check_sorted(path: Path) -> int | None:
                """Line number of the first out-of-order line, or None if the file is sorted."""
                raise NotImplementedError
        ''',
    }, "tests/test_merge.py", [
        "test_unsorted_input_file_is_flagged",
        "test_merge_streams_without_loading_whole_files",
        "test_duplicate_timestamps_tie_breaking",
        "test_empty_file_and_single_file_input",
    ]),

    P(17, "sliding-window", {
        "max_sum_subarray.py": r'''
            def max_sum_subarray(nums: list[int], k: int) -> int | None:
                """Max sum over any contiguous window of size k, in O(n). No valid window: your sentinel."""
                raise NotImplementedError
        ''',
        "longest_substring_no_repeat.py": r'''
            def longest_unique_substring(s: str) -> str:
                """Longest substring without repeated characters, in O(n). Its length is len(result)."""
                raise NotImplementedError
        ''',
    }, "tests/test_sliding_window.py", [
        "test_k_larger_than_array_has_no_window",
        "test_empty_array_and_empty_string",
        "test_all_identical_elements",
        "test_k_zero_and_k_equal_to_length",
    ]),

    P(18, "rate-limiter", {
        "sliding_window_limiter.py": r'''
            """Per-client deque of timestamps."""


            class SlidingWindowLimiter:
                def __init__(self, limit: int, window_seconds: float = 60.0):
                    """Allow at most `limit` requests per client in any rolling `window_seconds`."""
                    raise NotImplementedError

                def allow(self, client_id: str, timestamp: float) -> bool:
                    """Record the request if allowed. True = allow, False = deny."""
                    raise NotImplementedError
        ''',
        "middleware.py": r'''
            """WSGI middleware: intercepts requests, consults the limiter, returns 429 when denied."""
            import argparse
            import time
            from collections.abc import Callable
            from wsgiref.simple_server import make_server

            from sliding_window_limiter import SlidingWindowLimiter


            class RateLimitMiddleware:
                def __init__(self, app: Callable, limiter: SlidingWindowLimiter,
                             client_id: Callable[[dict], str] = lambda environ: environ.get("REMOTE_ADDR", "?"),
                             clock: Callable[[], float] = time.time):
                    self.app = app
                    self.limiter = limiter
                    self.client_id = client_id
                    self.clock = clock

                def __call__(self, environ: dict, start_response: Callable):
                    if self.limiter.allow(self.client_id(environ), self.clock()):
                        return self.app(environ, start_response)
                    start_response("429 Too Many Requests", [("Content-Type", "text/plain")])
                    return [b"rate limit exceeded\n"]


            def hello_app(environ: dict, start_response: Callable):
                start_response("200 OK", [("Content-Type", "text/plain")])
                return [b"ok\n"]


            def main(argv: list[str] | None = None) -> None:
                ap = argparse.ArgumentParser(description="Demo server behind the sliding-window rate limiter.")
                ap.add_argument("--limit", type=int, default=5)
                ap.add_argument("--window", type=float, default=60.0, help="seconds")
                ap.add_argument("--port", type=int, default=8000)
                args = ap.parse_args(argv)
                app = RateLimitMiddleware(hello_app, SlidingWindowLimiter(args.limit, args.window))
                print(f"serving on http://127.0.0.1:{args.port} ({args.limit} req / {args.window}s per client)")
                make_server("127.0.0.1", args.port, app).serve_forever()


            if __name__ == "__main__":
                main()
        ''',
    }, "tests/test_rate_limit.py", [
        "test_burst_in_same_millisecond",
        "test_out_of_order_timestamps",
        "test_old_timestamps_evicted_efficiently",
        "test_clients_have_independent_windows",
    ], notes=["`middleware.py` is finished WSGI plumbing (stdlib `wsgiref`, no framework). The algorithm lives in `sliding_window_limiter.py`."]),

    P(19, "binary-search-lib", {
        "basic_search.py": r'''
            def binary_search(nums: list, target) -> int:
                """Index of target in ascending nums, or -1."""
                raise NotImplementedError
        ''',
        "first_last_occurrence.py": r'''
            def first_occurrence(nums: list, target) -> int:
                """Index of the first target in ascending nums, or -1."""
                raise NotImplementedError


            def last_occurrence(nums: list, target) -> int:
                """Index of the last target in ascending nums, or -1."""
                raise NotImplementedError
        ''',
        "rotated_search.py": r'''
            def search_rotated(nums: list, target) -> int:
                """Index of target in a rotated ascending array (rotation may be 0), or -1. O(log n)."""
                raise NotImplementedError
        ''',
    }, "tests/test_binary_search.py", [
        "test_target_not_present",
        "test_duplicates_first_and_last_differ",
        "test_empty_and_single_element_arrays",
        "test_rotation_point_zero_not_rotated",
        "test_target_equals_pivot_in_rotated",
    ]),

    P(20, "git-bisect-sim", {
        "commit_history.py": r'''
            """Generates a mock history with a hidden first-bad commit."""
            import random


            class CommitHistory:
                """Commits 0..n-1. All commits before `first_bad` are good, all from it onward are bad.

                The algorithm should only learn state through test_commit(); `calls` counts those checks.
                """

                def __init__(self, n: int, first_bad: int | None = None, seed: int | None = None):
                    if n < 1:
                        raise ValueError("history needs at least one commit")
                    self.n = n
                    self.first_bad = random.Random(seed).randrange(n) if first_bad is None else first_bad
                    if not 0 <= self.first_bad < n:
                        raise ValueError(f"first_bad must be in [0, {n})")
                    self.calls = 0

                def test_commit(self, commit_id: int) -> bool:
                    """True if the commit is bad."""
                    if not 0 <= commit_id < self.n:
                        raise IndexError(commit_id)
                    self.calls += 1
                    return commit_id >= self.first_bad

                def __len__(self) -> int:
                    return self.n


            if __name__ == "__main__":
                h = CommitHistory(10, first_bad=3)
                assert [h.test_commit(i) for i in range(10)] == [False] * 3 + [True] * 7 and h.calls == 10
                assert CommitHistory(100, seed=4).first_bad == CommitHistory(100, seed=4).first_bad
                print("commit_history ok")
        ''',
        "git_bisect.py": r'''
            """Binary-search-based bisection."""
            from collections.abc import Callable


            def find_first_bad(n: int, test_commit: Callable[[int], bool]) -> int:
                """Index of the first bad commit in 0..n-1 using O(log n) test_commit() calls."""
                raise NotImplementedError
        ''',
    }, "tests/test_bisect.py", [
        "test_first_commit_already_bad",
        "test_last_commit_is_first_bad",
        "test_history_of_length_one",
        "test_finds_first_transition_not_any_bad_commit",
    ], notes=["`bisect.py` is renamed to `git_bisect.py` because a local `bisect.py` shadows the stdlib `bisect` module (which `random` imports).",
              "`commit_history.py` is finished test plumbing. `find_first_bad` is yours."]),

    P(21, "backtracking-solvers", {
        "n_queens.py": r'''
            def solve_n_queens(n: int) -> list[list[int]]:
                """All solutions; each is a list where index = row and value = queen's column."""
                raise NotImplementedError
        ''',
        "sudoku_solver.py": r'''
            Grid = list[list[int]]


            def solve_sudoku(grid: Grid) -> Grid | None:
                """Solved 9x9 grid (0 = blank), or None if unsolvable/invalid."""
                raise NotImplementedError
        ''',
        "permutations_subsets.py": r'''
            def permutations(items: list) -> list[list]:
                """Every ordering of items."""
                raise NotImplementedError


            def subsets(items: list) -> list[list]:
                """Every subset of items, including the empty set."""
                raise NotImplementedError
        ''',
    }, "tests/test_backtracking.py", [
        "test_n_queens_2_and_3_have_no_solution",
        "test_sudoku_invalid_or_unsolvable_start",
        "test_sudoku_already_solved",
        "test_duplicate_elements_policy",
        "test_empty_set_yields_empty_subset",
    ]),

    P(22, "maze-sudoku-app", {
        "maze/generator.py": r'''
            """Randomized DFS or Prim's-based generation."""
            Grid = list[list[int]]


            def generate_maze(rows: int, cols: int, seed: int | None = None) -> Grid:
                """A maze that is solvable by construction. Grid encoding (cell vs wall grid) is yours."""
                raise NotImplementedError
        ''',
        "maze/solver.py": r'''
            """BFS/DFS solve plus path output."""
            Cell = tuple[int, int]


            def solve_maze(maze: list[list[int]], start: Cell, goal: Cell) -> list[Cell] | None:
                """Path of cells from start to goal, or None."""
                raise NotImplementedError
        ''',
        "sudoku/validator.py": r'''
            def is_valid_board(grid: list[list[int]]) -> bool:
                """No row/column/box contradicts itself (0 = blank)."""
                raise NotImplementedError
        ''',
        "sudoku/solver.py": r'''
            Grid = list[list[int]]


            def solve_sudoku(grid: Grid) -> Grid | None:
                raise NotImplementedError


            def count_solutions(grid: Grid, limit: int = 2) -> int:
                """Number of solutions, stopping at `limit` (2 is enough to flag ambiguity)."""
                raise NotImplementedError


            def hint(grid: Grid) -> tuple[int, int, int]:
                """(row, col, value) for one blank cell. Solved/contradictory puzzles are an invalid state."""
                raise NotImplementedError
        ''',
        "ui/app.py": r'''
            """Front end for maze and/or sudoku. tkinter or curses (both stdlib) keep this dependency-free."""


            def main() -> None:
                raise NotImplementedError


            if __name__ == "__main__":
                main()
        ''',
    }, "tests/test_maze_sudoku.py", [
        "test_generated_maze_always_solvable",
        "test_one_by_one_maze",
        "test_sudoku_multiple_solutions_flagged_ambiguous",
        "test_hint_on_solved_or_contradictory_puzzle_flagged",
    ], notes=["Added `tests/test_maze_sudoku.py`; the suggested structure has no tests folder."]),

    P(23, "sort-bench", {
        "algorithms/merge_sort.py": r'''
            def merge_sort(nums: list) -> list:
                """nums sorted ascending."""
                raise NotImplementedError
        ''',
        "algorithms/quick_sort.py": r'''
            def quick_sort(nums: list) -> list:
                """nums sorted ascending. Pivot choice is where the worst case hides."""
                raise NotImplementedError
        ''',
        "algorithms/heap_sort.py": r'''
            def heap_sort(nums: list) -> list:
                """nums sorted ascending."""
                raise NotImplementedError
        ''',
        "algorithms/counting_sort.py": r'''
            def counting_sort(nums: list[int]) -> list[int]:
                """Non-comparison sort for ints in a bounded range."""
                raise NotImplementedError
        ''',
        "bench.py": r'''
            """Runs all algorithms across all distributions."""
            import random
            from collections.abc import Callable

            from algorithms.counting_sort import counting_sort
            from algorithms.heap_sort import heap_sort
            from algorithms.merge_sort import merge_sort
            from algorithms.quick_sort import quick_sort

            ALGORITHMS: dict[str, Callable[[list], list]] = {
                "merge": merge_sort, "quick": quick_sort, "heap": heap_sort, "counting": counting_sort,
            }
            DISTRIBUTIONS = ("random", "nearly_sorted", "reverse_sorted", "all_duplicates")


            def make_input(distribution: str, n: int, seed: int = 0) -> list[int]:
                """n ints in [0, n) shaped by `distribution`. nearly_sorted = sorted with ~1% random swaps."""
                rng = random.Random(seed)
                if distribution == "all_duplicates":
                    return [7] * n
                xs = [rng.randrange(max(n, 1)) for _ in range(n)]
                if distribution == "random":
                    return xs
                xs.sort(reverse=distribution == "reverse_sorted")
                if distribution == "nearly_sorted":
                    for _ in range(max(1, n // 100) if n > 1 else 0):
                        i, j = rng.randrange(n), rng.randrange(n)
                        xs[i], xs[j] = xs[j], xs[i]
                elif distribution != "reverse_sorted":
                    raise ValueError(f"unknown distribution {distribution!r}")
                return xs


            def run(sizes: list[int], trials: int = 3) -> list[dict]:
                """Rows of {"algorithm", "distribution", "n", "time_ms"} for every combination."""
                raise NotImplementedError


            if __name__ == "__main__":
                for row in run([1_000, 10_000, 100_000]):
                    print(row)
        ''',
    }, "tests/test_correctness.py", [
        "test_sorted_input_with_naive_pivot_worst_case",
        "test_all_identical_elements",
        "test_counting_sort_requires_bounded_range",
        "test_empty_and_single_element_arrays",
    ]),

    P(24, "multi-criteria-sorter", {
        "models.py": r'''
            """Item schema."""
            from dataclasses import dataclass
            from datetime import datetime


            @dataclass
            class Item:
                name: str
                date: datetime | None = None
                size: int | None = None
        ''',
        "comparator.py": r'''
            """Builds a composite comparator from a key order."""
            from collections.abc import Callable
            from functools import cmp_to_key

            from models import Item


            def build_comparator(order: list[str]) -> Callable[[Item, Item], int]:
                """cmp(a, b) -> negative/0/positive, comparing by order[0], then order[1], ..."""
                raise NotImplementedError


            def sort_items(items: list[Item], order: list[str]) -> list[Item]:
                return sorted(items, key=cmp_to_key(build_comparator(order)))
        ''',
        "external_sort.py": r'''
            """Chunked sort-and-merge for inputs bigger than memory."""
            import argparse
            from pathlib import Path


            def external_sort(in_path: Path, out_path: Path, order: list[str], chunk_size: int = 100_000) -> None:
                """Sort items in in_path into out_path using sorted chunks on disk, then a k-way merge."""
                raise NotImplementedError


            def main(argv: list[str] | None = None) -> None:
                ap = argparse.ArgumentParser(description="Sort a file too large for memory by multiple keys.")
                ap.add_argument("input", type=Path)
                ap.add_argument("output", type=Path)
                ap.add_argument("--by", default="name", help="comma-separated key order, e.g. date,name")
                ap.add_argument("--chunk-size", type=int, default=100_000, help="items per in-memory chunk")
                args = ap.parse_args(argv)
                external_sort(args.input, args.output, args.by.split(","), args.chunk_size)


            if __name__ == "__main__":
                main()
        ''',
    }, "tests/test_comparator.py", [
        "test_primary_ties_broken_by_secondary_and_tertiary",
        "test_conflicting_or_duplicate_sort_keys",
        "test_missing_attribute_sort_position",
        "test_external_sort_for_input_larger_than_memory",
    ]),
]
