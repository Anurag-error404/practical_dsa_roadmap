import pytest

from commit_history import CommitHistory
from git_bisect import find_first_bad


def test_first_commit_already_bad():
    # TODO: The very first commit is already bad — no "good" baseline exists
    ...


def test_last_commit_is_first_bad():
    # TODO: The very last commit is the first bad one
    ...


def test_history_of_length_one():
    # TODO: History of length 1
    ...


def test_finds_first_transition_not_any_bad_commit():
    # TODO: The history has a bad commit followed by more bad commits — must find the first
    #       transition point, not just any bad commit encountered
    ...
