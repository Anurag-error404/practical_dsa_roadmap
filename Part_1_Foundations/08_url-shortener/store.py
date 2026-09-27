"""Hash table plus TTL logic. Must be safe under concurrent access (ThreadingHTTPServer)."""
import time
from collections.abc import Callable
from typing import Any


class TTLStore:
    def __init__(self, clock: Callable[[], float] = time.monotonic):
        """`clock` is injectable so tests can fake time passing."""
        raise NotImplementedError

    def set(self, key: str, value: Any, ttl: float | None = None) -> None:
        """Store value; ttl in seconds, None = never expires."""
        raise NotImplementedError

    def get(self, key: str) -> Any:
        """Value for key, or a clear not-found result if missing or expired."""
        raise NotImplementedError

    def delete(self, key: str) -> None:
        raise NotImplementedError

    def __contains__(self, key: str) -> bool:
        raise NotImplementedError
