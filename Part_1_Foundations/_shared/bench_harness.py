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
