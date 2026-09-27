import pytest

from models import Status, Task
from dependency_graph import DependencyGraph
from priority_queue import ReadyQueue
from scheduler import TaskManager


def test_self_dependency_rejected_at_creation():
    # TODO: A task depending on itself — a self-cycle, must be detected and rejected at
    #       creation, not discovered later
    ...


def test_multi_task_cycle_rejected_before_added():
    # TODO: A circular dependency across multiple tasks (A→B→A) — detect via cycle check before
    #       allowing the dependency to be added, not just at query time
    ...


def test_completing_task_unblocks_dependents():
    # TODO: Completing a task that others depend on — verify dependents actually get unblocked
    #       and become eligible for `get_next_task()`
    ...


def test_priority_tie_broken_by_deadline_then_creation():
    # TODO: Two unblocked tasks tied on priority — needs a defined tie-break (deadline, then
    #       creation order)
    ...


def test_past_deadline_at_creation_policy():
    # TODO: A deadline set in the past at creation time — decide whether this is allowed, auto-
    #       flagged as overdue, or rejected
    ...
