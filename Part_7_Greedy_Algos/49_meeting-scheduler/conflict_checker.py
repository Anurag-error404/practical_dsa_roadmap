from models import Meeting


def validate(meeting: Meeting) -> None:
    """Reject invalid ranges (end before start)."""
    raise NotImplementedError


def overlaps(a: Meeting, b: Meeting) -> bool:
    """Document whether back-to-back (a.end == b.start) counts as a conflict."""
    raise NotImplementedError
