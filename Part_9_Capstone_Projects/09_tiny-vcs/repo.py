"""Public API: commit / diff / checkout."""
from blob_store import BlobStore
from checkout import checkout
from commit_graph import CommitGraph
from diff_engine import DiffOp, diff_commits
from models import Commit, Snapshot


class Repository:
    def __init__(self):
        self.store = BlobStore()
        self.graph = CommitGraph()
        self.head: str | None = None

    def commit(self, files: Snapshot, message: str) -> Commit:
        raise NotImplementedError

    def diff(self, commit_a: str, commit_b: str) -> dict[str, list[DiffOp]]:
        raise NotImplementedError

    def checkout(self, commit_id: str) -> Snapshot:
        raise NotImplementedError
