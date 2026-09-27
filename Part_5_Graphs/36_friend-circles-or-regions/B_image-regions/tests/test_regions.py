import pytest

from union_find import UnionFind
from grid_scanner import foreground_cells, neighbors
from region_counter import regions
from random_graphs import random_grid


def test_fully_disconnected_each_pixel_own_region():
    # TODO: A fully disconnected input — every person/pixel is its own group
    ...


def test_fully_connected_one_region():
    # TODO: A fully connected input — one single giant group
    ...


def test_diagonal_adjacency_rule_documented():
    # TODO: (Image) Diagonal adjacency vs. only up/down/left/right — decide and document which
    #       counts as "connected," since this materially changes the region count
    ...


def test_empty_grid():
    # TODO: An empty input grid or graph
    ...
