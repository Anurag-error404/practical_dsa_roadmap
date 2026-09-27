import pytest

from huffman_tree import HuffmanNode, build_tree, build_codes
from encoder import encode
from decoder import decode
from tree_debug import binary_children, print_tree


def test_single_distinct_symbol_input():
    # TODO: Input with only one distinct character — a single-symbol Huffman tree can't produce
    #       a normal variable-length code; needs explicit special-case handling
    ...


def test_empty_input():
    # TODO: Empty input
    ...


def test_roundtrip_is_byte_identical():
    # TODO: Round-trip correctness — decompressed output must be byte-for-byte identical to the
    #       original input, always test this explicitly
    ...
