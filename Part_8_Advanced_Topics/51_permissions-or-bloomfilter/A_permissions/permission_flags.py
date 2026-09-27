class FlagRegistry:
    """Named permission flags, each owning one bit."""

    def __init__(self, names: tuple[str, ...] = ()):
        raise NotImplementedError

    def define(self, name: str) -> int:
        """Allocate the next free bit to `name` and return its mask."""
        raise NotImplementedError

    def mask(self, name: str) -> int:
        """Mask for a defined flag. Undefined flags must raise, not return 0."""
        raise NotImplementedError

    def names(self, mask: int) -> list[str]:
        """Flag names set in mask (for display)."""
        raise NotImplementedError
