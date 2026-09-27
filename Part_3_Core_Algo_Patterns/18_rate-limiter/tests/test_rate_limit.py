import pytest

from sliding_window_limiter import SlidingWindowLimiter
from middleware import RateLimitMiddleware, hello_app


def test_burst_in_same_millisecond():
    # TODO: A burst of requests arriving in the same millisecond
    ...


def test_out_of_order_timestamps():
    # TODO: Requests arriving slightly out of chronological order (network jitter/clock skew)
    ...


def test_old_timestamps_evicted_efficiently():
    # TODO: Old timestamps need to be evicted from each client's window efficiently — not by
    #       rescanning full history on every check
    ...


def test_clients_have_independent_windows():
    # TODO: Every client needs an independent window — a shared global counter would incorrectly
    #       let one client's traffic block another's
    ...
