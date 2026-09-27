import pytest

from server import ShortenerHandler, run
from store import TTLStore
from key_generator import generate_key


def test_key_collision_retries_or_widens_keyspace():
    # TODO: Generated short key collides with an existing one — retry generation or widen the
    #       keyspace
    ...


def test_ttl_expiration_policy_is_consistent():
    # TODO: TTL expiry — decide lazy (check on read, evict then) vs. active (background sweep)
    #       expiration, and be consistent
    ...


def test_get_unknown_key_returns_not_found():
    # TODO: `GET` for a key that was never created — 404, not a crash
    ...


def test_concurrent_writes_are_safe():
    # TODO: High concurrent write volume — the underlying hash table needs to be safe under
    #       concurrent access (locking or a concurrency-safe structure)
    ...
