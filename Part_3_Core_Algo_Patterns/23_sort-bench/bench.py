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
