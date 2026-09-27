"""Optional: renders the growth curve from results.csv."""
from pathlib import Path

from bench_harness import read_rows

RESULTS = Path(__file__).parent / "results.csv"


def plot(rows: list[dict], log_scale: bool = False, out: str | None = None) -> None:
    """Plot time_ms against input_size, one line per algorithm. Save to `out` or show."""
    raise NotImplementedError


if __name__ == "__main__":
    plot(read_rows(RESULTS))
