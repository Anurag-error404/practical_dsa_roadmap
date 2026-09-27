import pytest

from unique_paths import unique_paths, unique_paths_with_obstacles
from min_path_sum import min_path_sum
from edit_distance import edit_distance
from random_cases import cases, random_grid, random_obstacle_grid, random_string_pair


def test_start_or_end_is_obstacle_zero_paths():
    # TODO: The start or end cell itself is an obstacle — 0 valid paths
    ...


def test_one_by_one_grid():
    # TODO: A 1×1 grid — trivially 1 path, cost equal to the single cell's value
    ...


def test_edit_distance_identical_strings_zero():
    # TODO: Edit distance between two identical strings — 0
    ...


def test_edit_distance_empty_string_equals_other_length():
    # TODO: Edit distance where one string is empty — distance equals the length of the other
    #       string
    ...


def test_fully_blocked_grid_zero_paths():
    # TODO: An obstacle configuration that fully blocks every path — must return 0, not crash
    ...
