"""Assigns tasks to worker rounds, respecting deps plus capacity."""
from models import BuildTask, Schedule


def schedule(tasks: dict[str, BuildTask], workers: int) -> Schedule:
    """Rounds of at most `workers` tasks, each only after its deps finish, plus total time."""
    raise NotImplementedError
