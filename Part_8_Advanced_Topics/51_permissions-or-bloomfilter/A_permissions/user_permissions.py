from permission_flags import FlagRegistry


class UserPermissions:
    def __init__(self, registry: FlagRegistry):
        raise NotImplementedError

    def grant(self, user: str, *flags: str) -> None:
        """OR the flags in."""
        raise NotImplementedError

    def revoke(self, user: str, *flags: str) -> None:
        """AND-NOT the flags out."""
        raise NotImplementedError

    def check(self, user: str, flag: str) -> bool:
        raise NotImplementedError

    def mask(self, user: str) -> int:
        raise NotImplementedError
