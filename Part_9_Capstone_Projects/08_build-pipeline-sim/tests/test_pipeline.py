import pytest

from models import BuildTask, Schedule
from parser import parse_spec, load_spec
from topo_sort import find_cycle, topo_order
from union_find import UnionFind, independent_groups
from scheduler import schedule


def test_cycle_reported_before_scheduling():
    # TODO: A circular dependency — must be detected and reported before attempting to build any
    #       schedule
    ...


def test_ready_tasks_exceeding_workers_queue_next_round():
    # TODO: More independent, ready tasks at once than available workers — the excess must queue
    #       for the next round, not all run simultaneously beyond capacity
    ...


def test_zero_duration_task():
    # TODO: A task with zero duration — should schedule and complete instantly without breaking
    #       the timing math
    ...


def test_fully_sequential_pipeline_utilization_one():
    # TODO: A pipeline that's fully sequential (no parallelism possible at all) — should still
    #       complete correctly, just with worker utilization of 1 throughout
    ...
