"""DAG of commits with parent pointers."""
from models import Commit


class CommitGraph:
    def __init__(self):
        raise NotImplementedError

    def add(self, commit: Commit) -> None:
        raise NotImplementedError

    def get(self, commit_id: str) -> Commit:
        """Unknown id: clear error."""
        raise NotImplementedError

    def history(self, commit_id: str) -> list[Commit]:
        """Ancestors in topological order."""
        raise NotImplementedError
