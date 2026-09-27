import pytest

from grid import Grid
from pathfinder import find_path
from game_loop import Game
from random_graphs import random_grid


def test_unreachable_goal_detected():
    # TODO: No valid path exists between start and goal — this must be explicitly detected and
    #       communicated (e.g., an "unreachable" state), not leave the NPC frozen or the game
    #       crashed
    ...


def test_start_equals_goal():
    # TODO: Start cell equals goal cell
    ...


def test_new_obstacle_triggers_recompute():
    # TODO: The player places a new obstacle mid-game that blocks the currently-computed path —
    #       must trigger a recompute, not keep following a now-invalid route
    ...


def test_recompute_only_when_path_invalidated():
    # TODO: A grid large enough that recomputing a full path every single frame is too slow —
    #       recompute only when necessary (path invalidated) or on a fixed tick, not every frame
    ...
