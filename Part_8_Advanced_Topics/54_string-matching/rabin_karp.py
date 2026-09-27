"""Rolling hash plus spurious-hit verification."""


def rabin_karp_search(text: str, pattern: str, base: int = 256, mod: int = 1_000_000_007) -> list[int]:
    """Every start index of pattern in text. A small `mod` in tests forces spurious hash hits."""
    raise NotImplementedError
