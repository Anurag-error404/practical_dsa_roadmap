import pytest

from grid import CostGrid
from cost_dp import min_cost_path


def test_no_path_reports_unreachable():
    # TODO: No path exists due to obstacles — report unreachable explicitly
    ...


def test_zero_cost_cells_policy():
    # TODO: Zero-cost cells — decide whether these are allowed and how they interact with
    #       "shortest" path logic (could create ties)
    ...


def test_start_equals_end():
    # TODO: Start cell equals end cell
    ...
