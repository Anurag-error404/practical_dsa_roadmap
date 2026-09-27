import pytest

from hash_table import HashTable
from hash_functions import hash_key


def test_collision_is_resolved_not_overwritten():
    # TODO: Two different keys hashing to the same bucket (collision) — must resolve via
    #       chaining or open addressing, not silently overwrite
    ...


def test_delete_missing_key_is_noop_or_clear_error():
    # TODO: `delete()` on a key that was never inserted — should be a no-op or clear error, not
    #       a crash
    ...


def test_resize_preserves_all_entries():
    # TODO: Load factor crossing a threshold (e.g., 0.7) — trigger resize + rehash of all
    #       existing entries, not just new ones
    ...


def test_mutable_key_policy_documented():
    # TODO: Using a mutable object as a key — document that this is unsafe (hash could change
    #       after insertion) or disallow it
    ...
