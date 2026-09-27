"""Short key generation (hash-based or random)."""


def generate_key(url: str, length: int = 7, attempt: int = 0) -> str:
    """A short key for url. `attempt` lets the caller retry after a collision."""
    raise NotImplementedError
