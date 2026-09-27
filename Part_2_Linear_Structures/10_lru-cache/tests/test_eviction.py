import pytest

from lru_cache import LRUCache


def test_capacity_zero_and_one():
    # TODO: Capacity of 0 or 1 — the smallest cases are where off-by-one eviction bugs live
    ...


def test_put_existing_key_updates_and_refreshes_recency():
    # TODO: `put()` on a key that already exists — update its value and refresh its recency,
    #       don't create a duplicate entry
    ...


def test_get_on_evicted_key_is_miss():
    # TODO: `get()` on a key that was already evicted
    ...


def test_music_shuffle_no_repeat_until_all_played():
    # TODO: (Music variant) `shuffle()` shouldn't repeat a song until every other song has
    #       played once, unless the user explicitly wants repeats
    ...
