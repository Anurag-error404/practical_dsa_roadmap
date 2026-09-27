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
