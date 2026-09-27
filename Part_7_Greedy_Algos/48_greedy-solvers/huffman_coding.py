from dataclasses import dataclass


@dataclass
class HuffmanNode:
    freq: int
    symbol: str | None = None
    left: "HuffmanNode | None" = None
    right: "HuffmanNode | None" = None


def huffman_codes(freqs: dict[str, int]) -> dict[str, str]:
    """Character -> prefix-free bit string."""
    raise NotImplementedError
