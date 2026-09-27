import pytest

from models import Meeting
from scheduler import schedule
from conflict_checker import validate, overlaps


def test_back_to_back_meetings_policy():
    # TODO: Back-to-back meetings (one ends exactly when the next starts) — decide whether this
    #       is allowed
    ...


def test_equal_start_times():
    # TODO: Meetings with equal start times
    ...


def test_duplicate_meeting_request():
    # TODO: A duplicate meeting request
    ...


def test_large_volume_uses_greedy_not_brute_force():
    # TODO: A large volume of meetings needing the efficient greedy approach (sort by end time)
    #       rather than brute-force checking every combination
    ...


def test_invalid_time_range_rejected():
    # TODO: Invalid time ranges (end before start) — should be rejected outright
    ...
