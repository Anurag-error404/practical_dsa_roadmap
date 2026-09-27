import pytest

from job_queue import Job, JobQueue


def test_equal_priority_tie_breaking():
    # TODO: Multiple jobs with the same priority — decide tie-breaking (typically FIFO among
    #       equal priority)
    ...


def test_process_next_on_empty_queue():
    # TODO: `process_next()` on an empty queue
    ...


def test_priority_change_after_submission():
    # TODO: A job's priority changing after submission (priority queues don't support update-in-
    #       place natively — you'd need a workaround, e.g. lazy deletion)
    ...
