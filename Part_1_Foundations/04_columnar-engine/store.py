"""Column arrays plus dtype handling."""
from typing import Any


class ColumnStore:
    def __init__(self):
        raise NotImplementedError

    def add_column(self, name: str, values: list, dtype: type) -> None:
        """Register a column. All columns must have the same length."""
        raise NotImplementedError

    def column(self, name: str) -> list:
        """The values of a column. Unknown names must raise a clear error, not return None."""
        raise NotImplementedError

    def dtype(self, name: str) -> type:
        raise NotImplementedError

    @property
    def columns(self) -> list[str]:
        raise NotImplementedError

    def row(self, index: int) -> dict[str, Any]:
        """Reassemble one record, for returning filter results."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Row count."""
        raise NotImplementedError
