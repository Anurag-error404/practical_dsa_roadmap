from dsl import P

PROJECTS = [
    P(48, "greedy-solvers", {
        "activity_selection.py": r'''
            from dataclasses import dataclass


            @dataclass
            class Activity:
                start: float
                end: float


            def select_activities(activities: list[Activity]) -> list[Activity]:
                """Max set of non-overlapping activities. Document whether touching endpoints overlap."""
                raise NotImplementedError
        ''',
        "huffman_coding.py": r'''
            from dataclasses import dataclass


            @dataclass
            class HuffmanNode:
                freq: int
                symbol: str | None = None
                left: "HuffmanNode | None" = None
                right: "HuffmanNode | None" = None


            def huffman_codes(freqs: dict[str, int]) -> dict[str, str]:
                """Character -> prefix-free bit string."""
                raise NotImplementedError
        ''',
        "fractional_knapsack.py": r'''
            from dataclasses import dataclass


            @dataclass
            class Item:
                weight: float
                value: float


            def fractional_knapsack(items: list[Item], capacity: float) -> float:
                """Max value when items may be taken fractionally."""
                raise NotImplementedError
        ''',
    }, "tests/test_greedy.py", [
        "test_identical_start_end_tie_break",
        "test_touching_activities_overlap_policy",
        "test_single_character_huffman",
        "test_equal_ratio_items_total_value_correct",
        "test_capacity_zero",
    ]),

    P(49, "meeting-scheduler", {
        "models.py": r'''
            from dataclasses import dataclass


            @dataclass
            class Meeting:
                start: float
                end: float
                priority: int = 0
                name: str = ""
        ''',
        "scheduler.py": r'''
            """Greedy interval scheduling."""
            from models import Meeting


            def schedule(meetings: list[Meeting]) -> tuple[list[Meeting], list[Meeting]]:
                """(accepted, rejected): the max conflict-free set, plus everything left out."""
                raise NotImplementedError
        ''',
        "conflict_checker.py": r'''
            from models import Meeting


            def validate(meeting: Meeting) -> None:
                """Reject invalid ranges (end before start)."""
                raise NotImplementedError


            def overlaps(a: Meeting, b: Meeting) -> bool:
                """Document whether back-to-back (a.end == b.start) counts as a conflict."""
                raise NotImplementedError
        ''',
    }, "tests/test_scheduler.py", [
        "test_back_to_back_meetings_policy",
        "test_equal_start_times",
        "test_duplicate_meeting_request",
        "test_large_volume_uses_greedy_not_brute_force",
        "test_invalid_time_range_rejected",
    ]),
]
