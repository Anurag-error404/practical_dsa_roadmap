"""Save/replay range-query fixtures (array + op sequence) as JSON, for segment/Fenwick tree tests.

Ops are ("update", index, value) or ("query", left, right) with 0 <= left <= right < n.
Invalid ranges are yours to construct by hand in tests.
"""
import json
import random
from pathlib import Path

Op = tuple


def random_array(n: int, max_value: int = 100, *, seed: int | None = None) -> list[int]:
    rng = random.Random(seed)
    return [rng.randint(0, max_value) for _ in range(n)]


def random_ops(n: int, count: int, *, max_value: int = 100, update_p: float = 0.5, seed: int | None = None) -> list[Op]:
    """`count` valid ops over an array of length n (none if n == 0)."""
    rng = random.Random(seed)
    ops: list[Op] = []
    for _ in range(count if n else 0):
        if rng.random() < update_p:
            ops.append(("update", rng.randrange(n), rng.randint(0, max_value)))
        else:
            left = rng.randrange(n)
            ops.append(("query", left, rng.randrange(left, n)))
    return ops


def save_fixture(path: str | Path, array: list, ops: list[Op]) -> None:
    Path(path).write_text(json.dumps({"array": array, "ops": [list(op) for op in ops]}, indent=1))


def load_fixture(path: str | Path) -> tuple[list, list[Op]]:
    data = json.loads(Path(path).read_text())
    return data["array"], [tuple(op) for op in data["ops"]]


if __name__ == "__main__":
    import tempfile

    arr, ops = random_array(10, seed=1), random_ops(10, 50, seed=1)
    assert all(0 <= a < 10 and (kind == "update" or a <= b < 10) for kind, a, b in ops)
    assert random_ops(0, 5) == [] and random_ops(1, 3, seed=2) == random_ops(1, 3, seed=2)
    with tempfile.TemporaryDirectory() as d:
        save_fixture(Path(d) / "f.json", arr, ops)
        assert load_fixture(Path(d) / "f.json") == (arr, ops)
    print("fixtures ok")
