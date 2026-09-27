class HuffmanNode:
    def __init__(self, freq: int, symbol: int | None = None,
                 left: "HuffmanNode | None" = None, right: "HuffmanNode | None" = None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right


def build_tree(data: bytes) -> HuffmanNode | None:
    """Huffman tree from byte frequencies (built with a heap)."""
    raise NotImplementedError


def build_codes(root: HuffmanNode | None) -> dict[int, str]:
    """Byte value -> bit string."""
    raise NotImplementedError
