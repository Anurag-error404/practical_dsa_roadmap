import pytest

from parser import parse_spec, load_spec
from topo_sort import build_order
from cycle_reporter import find_cycle, format_cycle


def test_circular_dependency_reports_involved_tasks():
    # TODO: A circular dependency — report which tasks form the cycle, not just "a cycle exists
    #       somewhere"
    ...


def test_undefined_dependency_policy():
    # TODO: A task listed as a dependency but never itself defined — decide whether this is an
    #       error or gets auto-included as a no-op task
    ...


def test_duplicate_dependency_declarations():
    # TODO: Duplicate dependency declarations for the same pair
    ...


def test_independent_task_still_in_output():
    # TODO: A fully independent task with no dependencies and nothing depending on it — should
    #       still appear in the output, order-agnostic
    ...
