"""Query interface."""
import argparse

from bfs_path import shortest_path
from graph_loader import load_edges


def format_result(a: str, b: str, path: list[str] | None) -> str:
    """Degree count and path, or an explicit "not connected"."""
    raise NotImplementedError


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description="Degrees of separation between two users.")
    ap.add_argument("edges", help="file of 'a b' friendship pairs")
    ap.add_argument("a")
    ap.add_argument("b")
    args = ap.parse_args(argv)
    print(format_result(args.a, args.b, shortest_path(load_edges(args.edges), args.a, args.b)))


if __name__ == "__main__":
    main()
