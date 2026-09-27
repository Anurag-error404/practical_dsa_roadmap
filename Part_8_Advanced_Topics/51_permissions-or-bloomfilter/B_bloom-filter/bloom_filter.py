"""Bit array plus multiple hash functions."""


class BloomFilter:
    def __init__(self, size_bits: int, num_hashes: int):
        raise NotImplementedError

    def add(self, item: str) -> None:
        raise NotImplementedError

    def might_contain(self, item: str) -> bool:
        """False = definitely absent; True = possibly present. Added items must always be True."""
        raise NotImplementedError
