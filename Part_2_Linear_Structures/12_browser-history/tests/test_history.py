import pytest

from history import BrowserHistory


def test_back_with_no_history_is_noop():
    # TODO: `back()` when there's nothing before the current page — no-op, not a crash
    ...


def test_new_visit_after_back_clears_forward_history():
    # TODO: `forward()` after a new visit was made following a `back()` — the forward history
    #       should be cleared (this is real browser behavior: you can't "redo" into a path you
    #       abandoned)
    ...


def test_repeated_back_past_first_page():
    # TODO: Repeated `back()` calls past the very first page
    ...


def test_same_url_visited_twice_in_a_row_policy():
    # TODO: Visiting the same URL twice in a row — decide whether that pushes a new history
    #       entry or is a no-op
    ...
