import pytest

from leaderboard import Leaderboard


def test_repeated_user_update_moves_not_duplicates():
    # TODO: A user's score updating multiple times — must update that user's position, not
    #       insert a duplicate entry
    ...


def test_score_ties_follow_defined_rule():
    # TODO: Ties in score — needs a defined tie-breaking rule (e.g., earliest achieved first)
    ...


def test_k_larger_than_user_count_returns_everyone():
    # TODO: `k` larger than the total number of users — return everyone, not an error
    ...
