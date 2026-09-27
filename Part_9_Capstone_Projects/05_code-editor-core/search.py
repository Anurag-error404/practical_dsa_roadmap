"""Find/replace using string matching."""


def find(text: str, pattern: str) -> list[int]:
    raise NotImplementedError


def replace_all(text: str, pattern: str, replacement: str) -> tuple[str, int]:
    """(new text, replacement count), in a single pass over the original match positions."""
    raise NotImplementedError
