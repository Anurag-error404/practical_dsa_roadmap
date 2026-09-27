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
