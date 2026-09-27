"""Restores file state from a commit."""
from blob_store import BlobStore
from commit_graph import CommitGraph
from models import Snapshot


def checkout(store: BlobStore, graph: CommitGraph, commit_id: str) -> Snapshot:
    raise NotImplementedError
