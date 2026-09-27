"""LCS-based diff between any two commits."""
from blob_store import BlobStore
from commit_graph import CommitGraph

DiffOp = tuple[str, str]


def diff_lines(a: list[str], b: list[str]) -> list[DiffOp]:
    raise NotImplementedError


def diff_commits(store: BlobStore, graph: CommitGraph, a: str, b: str) -> dict[str, list[DiffOp]]:
    """path -> line ops, regardless of branch topology between a and b."""
    raise NotImplementedError
