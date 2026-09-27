"""Bitmask constants and display helpers. Deliberately no set/clear/count logic; that's the exercise."""
MASK32 = (1 << 32) - 1
MASK64 = (1 << 64) - 1
INT32_MIN, INT32_MAX = -(1 << 31), (1 << 31) - 1


def bit(i: int) -> int:
    """Mask with only bit i set."""
    return 1 << i


def fmt_bin(x: int, width: int = 8) -> str:
    """x as a fixed-width binary string, grouped by nibble. Negatives show their two's-complement bits;
    bits above `width` are dropped (display only)."""
    s = format(x & ((1 << width) - 1), f"0{width}b")
    return "_".join(s[i:i + 4] for i in range(0, width, 4)) if width % 4 == 0 else s


if __name__ == "__main__":
    assert bit(0) == 1 and bit(5) == 32
    assert fmt_bin(5) == "0000_0101" and fmt_bin(-1) == "1111_1111" and fmt_bin(5, 3) == "101"
    assert MASK32 == 0xFFFFFFFF and INT32_MAX == 2**31 - 1
    print("bits ok")
