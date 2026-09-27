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
