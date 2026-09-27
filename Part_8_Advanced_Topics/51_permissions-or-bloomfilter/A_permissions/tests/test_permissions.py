import pytest

from permission_flags import FlagRegistry
from user_permissions import UserPermissions
from bits import bit, fmt_bin


def test_undefined_flag_check_raises():
    # TODO: Checking a permission flag that was never defined — should error, not silently
    #       return false
    ...


def test_grant_or_and_revoke_and_not_bit_logic():
    # TODO: Combining/removing permissions (OR to add, AND-NOT to remove) — a common source of
    #       subtle bugs if the bit logic is inverted
    ...


def test_zero_vs_all_permissions():
    # TODO: A user with zero permissions vs. a user with all permissions
    ...
