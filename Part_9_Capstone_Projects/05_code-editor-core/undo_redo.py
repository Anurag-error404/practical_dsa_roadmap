"""Two-stack undo/redo, invalidated on new edit."""
from models import Edit


class History:
    def __init__(self):
        raise NotImplementedError

    def record(self, edit: Edit) -> None:
        """Push a new edit (and invalidate redo)."""
        raise NotImplementedError

    def undo(self) -> Edit | None:
        raise NotImplementedError

    def redo(self) -> Edit | None:
        raise NotImplementedError
