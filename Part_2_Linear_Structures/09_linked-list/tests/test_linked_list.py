import pytest

import singly_linked_list
import doubly_linked_list


def test_insert_delete_at_head_tail_and_middle():
    # TODO: Insert/delete at the head vs. the tail vs. the middle — head/tail are common off-by-
    #       one traps
    ...


def test_insert_delete_on_empty_and_down_to_empty():
    # TODO: Insert/delete on an empty list, and delete down to an empty list
    ...


def test_reverse_empty_and_single_node_is_noop():
    # TODO: Reversing a list with 0 or 1 nodes — should be a no-op, not an error
    ...


def test_detect_cycle_none_self_loop_and_mid_list():
    # TODO: Cycle detection: no cycle, a self-loop (last node points to itself), and a cycle
    #       starting mid-list (not at the head) — all three must be handled by the same detector
    ...
