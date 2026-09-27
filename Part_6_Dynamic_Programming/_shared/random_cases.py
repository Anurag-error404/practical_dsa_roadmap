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
