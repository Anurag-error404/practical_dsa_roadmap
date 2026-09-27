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
