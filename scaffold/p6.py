from dsl import D, DIRS, P

SHARED = {
    "random_cases.py": r'''
        """Small random inputs for cross-checking DP answers against your own brute force.

        Generating cases is plumbing; the brute-force reference and the comparison are yours:

            for weights, values, cap in cases(random_items, count=300):
                assert knapsack_01(weights, values, cap)[0] == my_brute_force(weights, values, cap)

        Sizes default small (empty included) so exhaustive search stays fast.
        """
        import random
        from collections.abc import Callable, Iterator


        def random_ints(n_max: int = 8, lo: int = -5, hi: int = 5, *, seed: int | None = None) -> list[int]:
            """0..n_max ints in [lo, hi] (LIS inputs)."""
            rng = random.Random(seed)
            return [rng.randint(lo, hi) for _ in range(rng.randint(0, n_max))]


        def random_string(n_max: int = 8, alphabet: str = "abc", *, seed: int | None = None) -> str:
            """0..n_max chars from a small alphabet, so collisions/matches are common (LCS, edit distance)."""
            rng = random.Random(seed)
            return "".join(rng.choice(alphabet) for _ in range(rng.randint(0, n_max)))


        def random_string_pair(n_max: int = 8, alphabet: str = "abc", *, seed: int | None = None) -> tuple[str, str]:
            rng = random.Random(seed)
            return random_string(n_max, alphabet, seed=rng.random()), random_string(n_max, alphabet, seed=rng.random())


        def random_coins(max_coins: int = 4, max_value: int = 10, max_amount: int = 30, *, seed: int | None = None) -> tuple[list[int], int]:
            """(denominations, amount). Denominations may repeat; amount may be unreachable."""
            rng = random.Random(seed)
            return [rng.randint(1, max_value) for _ in range(rng.randint(1, max_coins))], rng.randint(0, max_amount)


        def random_items(n_max: int = 6, max_weight: int = 10, max_value: int = 20, *, seed: int | None = None) -> tuple[list[int], list[int], int]:
            """(weights, values, capacity) for knapsack / budget allocation. Items can exceed capacity."""
            rng = random.Random(seed)
            n = rng.randint(0, n_max)
            weights = [rng.randint(1, max_weight) for _ in range(n)]
            values = [rng.randint(0, max_value) for _ in range(n)]
            return weights, values, rng.randint(0, max_weight * 2)


        def random_grid(rows_max: int = 4, cols_max: int = 4, max_cost: int = 9, *, seed: int | None = None) -> list[list[int]]:
            """1..rows_max x 1..cols_max grid of cell costs in [0, max_cost] (min-path-sum)."""
            rng = random.Random(seed)
            rows, cols = rng.randint(1, rows_max), rng.randint(1, cols_max)
            return [[rng.randint(0, max_cost) for _ in range(cols)] for _ in range(rows)]


        def random_obstacle_grid(rows_max: int = 4, cols_max: int = 4, obstacle_p: float = 0.25, *, seed: int | None = None) -> list[list[int]]:
            """Grid of 0 (open) / 1 (obstacle); start/end cells may be blocked (unique-paths)."""
            rng = random.Random(seed)
            rows, cols = rng.randint(1, rows_max), rng.randint(1, cols_max)
            return [[int(rng.random() < obstacle_p) for _ in range(cols)] for _ in range(rows)]


        def random_lines(n_max: int = 8, vocab: tuple[str, ...] = ("a", "b", "c", "d"), *, seed: int | None = None) -> list[str]:
            """Lines drawn from a tiny vocabulary so repeated lines are common (diff)."""
            rng = random.Random(seed)
            return [rng.choice(vocab) for _ in range(rng.randint(0, n_max))]


        def cases(gen: Callable, count: int = 200, seed: int = 0, **kwargs) -> Iterator:
            """Yield `count` reproducible cases: gen(seed=seed + i, **kwargs)."""
            for i in range(count):
                yield gen(seed=seed + i, **kwargs)


        if __name__ == "__main__":
            assert random_items(seed=3) == random_items(seed=3)
            for w, v, c in cases(random_items, 100):
                assert len(w) == len(v) <= 6 and c >= 0
            assert any(len(s) == 0 for s in cases(random_string, 100))
            coins, amount = random_coins(seed=1)
            assert coins and all(c >= 1 for c in coins) and amount >= 0
            g = random_obstacle_grid(seed=2)
            assert g and all(set(r) <= {0, 1} for r in g)
            a, b = random_string_pair(seed=5)
            assert set(a + b) <= set("abc")
            assert all(len(x) <= 8 for x in cases(random_lines, 50)) and all(len(random_grid(seed=i)[0]) >= 1 for i in range(20))
            print("random_cases ok")
    ''',
}

PROJECTS = [
    P(41, "dp-fundamentals", {
        "naive_recursive.py": r'''
            """Baseline, exponential."""


            def fib(n: int) -> int:
                raise NotImplementedError


            def climb_stairs(n: int) -> int:
                """Ways to climb n stairs taking 1 or 2 steps at a time."""
                raise NotImplementedError


            def coin_change(coins: list[int], amount: int) -> int:
                """Fewest coins summing to amount, or -1 if impossible."""
                raise NotImplementedError
        ''',
        "memoized.py": r'''
            """Top-down with a cache."""


            def fib(n: int) -> int:
                raise NotImplementedError


            def climb_stairs(n: int) -> int:
                raise NotImplementedError


            def coin_change(coins: list[int], amount: int) -> int:
                raise NotImplementedError
        ''',
        "tabulated.py": r'''
            """Bottom-up."""


            def fib(n: int) -> int:
                raise NotImplementedError


            def climb_stairs(n: int) -> int:
                raise NotImplementedError


            def coin_change(coins: list[int], amount: int) -> int:
                raise NotImplementedError
        ''',
        "bench.py": r'''
            """Times naive vs memoized vs tabulated."""
            import memoized
            import naive_recursive
            import tabulated

            IMPLEMENTATIONS = {"naive": naive_recursive, "memoized": memoized, "tabulated": tabulated}


            def run(n_values: list[int], trials: int = 3) -> list[dict]:
                """Rows of {"impl", "problem", "n", "time_ms"}. Cap or time out the naive version at large n."""
                raise NotImplementedError


            if __name__ == "__main__":
                for row in run([10, 20, 30, 35]):
                    print(row)
        ''',
    }, "tests/test_dp_basics.py", [
        "test_base_cases_n_zero_and_one",
        "test_negative_n_rejected",
        "test_coin_change_impossible_returns_minus_one",
        "test_naive_version_capped_for_large_n",
        "test_duplicate_denominations",
    ], extra_imports=["from random_cases import cases, random_coins"]),

    P(42, "knapsack", {
        "knapsack_01.py": r'''
            def knapsack_01(weights: list[int], values: list[int], capacity: int) -> tuple[int, list[list[int]]]:
                """(max value, dp table). Each item used at most once. reconstruct_01 traces the table."""
                raise NotImplementedError
        ''',
        "knapsack_unbounded.py": r'''
            def knapsack_unbounded(weights: list[int], values: list[int], capacity: int) -> tuple[int, list[int]]:
                """(max value, dp table). Items reusable any number of times; capacity still binds."""
                raise NotImplementedError
        ''',
        "reconstruct_selection.py": r'''
            """Traces back which items were chosen."""


            def reconstruct_01(dp: list[list[int]], weights: list[int], capacity: int) -> list[int]:
                """Indices of the chosen items."""
                raise NotImplementedError


            def reconstruct_unbounded(dp: list[int], weights: list[int], values: list[int], capacity: int) -> list[int]:
                """Indices of the chosen items (repeats allowed)."""
                raise NotImplementedError
        ''',
    }, "tests/test_knapsack.py", [
        "test_capacity_zero_gives_value_zero",
        "test_item_heavier_than_capacity_excluded",
        "test_all_zero_weight_items_flagged",
        "test_empty_item_list",
        "test_unbounded_respects_capacity_with_repeated_item",
    ], extra_imports=["from random_cases import cases, random_items"]),

    P(43, "budget-allocator", {
        "models.py": r'''
            """Project schema."""
            from dataclasses import dataclass


            @dataclass
            class Project:
                name: str
                cost: int
                value: int
        ''',
        "knapsack_solver.py": r'''
            """Copy in or adapt your Project 42 0/1 knapsack."""
            from models import Project


            def allocate(projects: list[Project], budget: int) -> list[Project]:
                """The value-maximizing subset within budget, returned the same way every run."""
                raise NotImplementedError
        ''',
        "report.py": r'''
            """Shows selected projects plus leftover budget."""
            from models import Project


            def format_report(selected: list[Project], budget: int) -> str:
                raise NotImplementedError
        ''',
    }, "tests/test_allocator.py", [
        "test_project_costing_more_than_budget_excluded",
        "test_identical_projects_total_value_exact",
        "test_zero_budget_funds_nothing",
        "test_tied_subsets_returned_consistently",
    ], extra_imports=["from random_cases import cases, random_items"]),

    P(44, "lcs-lis", {
        "lcs.py": r'''
            """DP table plus backtrack reconstruction."""
            from collections.abc import Sequence


            def lcs(a: Sequence, b: Sequence) -> list:
                """One longest common subsequence itself (its length is len(result))."""
                raise NotImplementedError
        ''',
        "lis.py": r'''
            """O(n log n) or O(n^2), plus reconstruction."""


            def lis(nums: list) -> list:
                """One longest increasing subsequence itself. Strict vs non-decreasing: decide and document."""
                raise NotImplementedError
        ''',
    }, "tests/test_reconstruction.py", [
        "test_empty_inputs_give_empty_result",
        "test_no_common_subsequence_explicit_empty",
        "test_lis_strictly_decreasing_length_one",
        "test_lis_duplicates_strict_vs_non_decreasing",
        "test_reconstruction_is_valid_subsequence",
    ], extra_imports=["from random_cases import cases, random_ints, random_string_pair"]),

    P(45, "mini-diff", {
        "line_splitter.py": r'''
            from pathlib import Path


            def split_lines(text: str) -> list[str]:
                """Lines for diffing. Trailing-newline and line-ending handling is yours."""
                raise NotImplementedError


            def read_lines(path: str | Path) -> list[str]:
                return split_lines(Path(path).read_text())
        ''',
        "lcs_diff.py": r'''
            """Reuses/adapts the LCS from Project 44."""

            DiffOp = tuple[str, str]


            def diff(a: list[str], b: list[str]) -> list[DiffOp]:
                """Ordered ops: (" ", line) unchanged, ("-", line) removed from a, ("+", line) added in b."""
                raise NotImplementedError
        ''',
        "report_formatter.py": r'''
            """Renders +/- style diff output."""
            import argparse

            from lcs_diff import DiffOp, diff
            from line_splitter import read_lines


            def format_diff(ops: list[DiffOp]) -> str:
                raise NotImplementedError


            def main(argv: list[str] | None = None) -> None:
                ap = argparse.ArgumentParser(description="Line-level diff of two text files.")
                ap.add_argument("old")
                ap.add_argument("new")
                args = ap.parse_args(argv)
                print(format_diff(diff(read_lines(args.old), read_lines(args.new))))


            if __name__ == "__main__":
                main()
        ''',
    }, "tests/test_diff.py", [
        "test_identical_files_zero_changes",
        "test_completely_different_files_all_changed",
        "test_very_different_lengths",
        "test_repeated_lines_mapped_to_correct_occurrence",
        "test_large_input_limitation_documented",
    ], extra_imports=["from random_cases import cases, random_lines"]),

    P(46, "grid-path-dp", {
        "unique_paths.py": r'''
            def unique_paths(m: int, n: int) -> int:
                """Paths from top-left to bottom-right of an m x n grid moving only right/down."""
                raise NotImplementedError


            def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
                """Same, where 1 marks an obstacle."""
                raise NotImplementedError
        ''',
        "min_path_sum.py": r'''
            def min_path_sum(grid: list[list[int]]) -> int:
                """Min total cost top-left to bottom-right moving only right/down."""
                raise NotImplementedError
        ''',
        "edit_distance.py": r'''
            def edit_distance(a: str, b: str) -> int:
                """Min insertions/deletions/substitutions turning a into b."""
                raise NotImplementedError
        ''',
    }, "tests/test_grid_dp.py", [
        "test_start_or_end_is_obstacle_zero_paths",
        "test_one_by_one_grid",
        "test_edit_distance_identical_strings_zero",
        "test_edit_distance_empty_string_equals_other_length",
        "test_fully_blocked_grid_zero_paths",
    ], extra_imports=["from random_cases import cases, random_grid, random_obstacle_grid, random_string_pair"]),

    DIRS(47, "spellcheck-or-pathopt",
        D("A_spellcheck", {
            "dictionary.py": r'''
                from pathlib import Path


                def load_dictionary(path: str | Path) -> dict[str, int]:
                    """word -> frequency (for tie-break ranking)."""
                    raise NotImplementedError
            ''',
            "edit_distance.py": r'''
                """Copy in your Project 46 edit distance."""


                def edit_distance(a: str, b: str) -> int:
                    raise NotImplementedError
            ''',
            "suggester.py": r'''
                """Ranks dictionary words by distance."""


                def suggest(word: str, dictionary: dict[str, int], limit: int = 5) -> list[str]:
                    """Closest dictionary words to `word`, best first."""
                    raise NotImplementedError
            ''',
        }, "tests/test_suggester.py", [
            "test_correct_word_returns_itself_first",
            "test_large_dictionary_limitation_noted",
            "test_ties_at_same_distance_return_several",
        ], edge=0),
        D("B_path-optimizer", {
            "grid.py": r'''
                """Per-cell movement costs; None marks an obstacle. Storage only."""
                Cell = tuple[int, int]


                class CostGrid:
                    def __init__(self, costs: list[list[float | None]]):
                        self.costs = costs
                        self.rows = len(costs)
                        self.cols = len(costs[0]) if costs else 0

                    def in_bounds(self, cell: Cell) -> bool:
                        r, c = cell
                        return 0 <= r < self.rows and 0 <= c < self.cols

                    def is_obstacle(self, cell: Cell) -> bool:
                        r, c = cell
                        return self.costs[r][c] is None

                    def cost(self, cell: Cell) -> float | None:
                        r, c = cell
                        return self.costs[r][c]
            ''',
            "cost_dp.py": r'''
                from grid import Cell, CostGrid


                def min_cost_path(grid: CostGrid, start: Cell, end: Cell) -> tuple[float, list[Cell]] | None:
                    """(total cost, path) avoiding obstacles, or None when unreachable."""
                    raise NotImplementedError
            ''',
        }, "tests/test_path_cost.py", [
            "test_no_path_reports_unreachable",
            "test_zero_cost_cells_policy",
            "test_start_equals_end",
        ], edge=1),
    ),
]
