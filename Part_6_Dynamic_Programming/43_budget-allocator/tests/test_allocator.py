import pytest

from models import Project
from knapsack_solver import allocate
from report import format_report
from random_cases import cases, random_items


def test_project_costing_more_than_budget_excluded():
    # TODO: A single project costing more than the entire budget — must be excluded from
    #       consideration
    ...


def test_identical_projects_total_value_exact():
    # TODO: Multiple projects with identical cost and value — any valid optimal selection is
    #       fine, but total value must be exactly correct
    ...


def test_zero_budget_funds_nothing():
    # TODO: Budget of 0 — fund nothing, don't error
    ...


def test_tied_subsets_returned_consistently():
    # TODO: Multiple different subsets tying at the same max value — the tool should return one
    #       consistently, not vary between runs on the same input
    ...
