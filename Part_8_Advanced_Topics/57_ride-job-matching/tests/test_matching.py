import pytest

from models import Request, Resource, Assignment, MatchResult
from matcher import cost, match
from simulator import random_requests, random_resources, Simulator


def test_more_requests_than_resources_reports_unmatched():
    # TODO: More riders/tasks than available drivers/workers — some requests go unmatched; this
    #       must be reported explicitly, not silently dropped
    ...


def test_incompatible_resource_reported_idle():
    # TODO: A driver/worker with no compatible match at all (skill or location mismatch) —
    #       reported as idle, not an error
    ...


def test_quality_ties_resolved_deterministically():
    # TODO: Ties in matching quality — the algorithm should pick one assignment
    #       deterministically, not arbitrarily
    ...


def test_resource_unavailable_mid_simulation():
    # TODO: A driver/worker becoming unavailable mid-simulation — decide whether already-
    #       assigned-but-not-started matches need to be re-matched
    ...
