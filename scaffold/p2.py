from dsl import D, DIRS, P

PROJECTS = [
    P(9, "linked-list", {
        "singly_linked_list.py": r'''
            from typing import Any


            class Node:
                def __init__(self, value: Any, next: "Node | None" = None):
                    self.value = value
                    self.next = next


            class SinglyLinkedList:
                def __init__(self):
                    raise NotImplementedError

                def insert(self, value: Any, position: int) -> None:
                    """Insert so value ends up at `position` (0 = head, len = tail)."""
                    raise NotImplementedError

                def delete(self, position: int) -> Any:
                    """Remove and return the value at `position`."""
                    raise NotImplementedError

                def reverse(self) -> None:
                    """Reverse in place. 0 or 1 nodes is a no-op."""
                    raise NotImplementedError

                def detect_cycle(self) -> bool:
                    """True if following .next ever revisits a node (self-loop and mid-list cycles included)."""
                    raise NotImplementedError

                def to_list(self) -> list:
                    """Values head -> tail, for assertions."""
                    raise NotImplementedError

                def __len__(self) -> int:
                    raise NotImplementedError
        ''',
        "doubly_linked_list.py": r'''
            from typing import Any


            class Node:
                def __init__(self, value: Any, prev: "Node | None" = None, next: "Node | None" = None):
                    self.value = value
                    self.prev = prev
                    self.next = next


            class DoublyLinkedList:
                def __init__(self):
                    raise NotImplementedError

                def insert(self, value: Any, position: int) -> None:
                    """Insert so value ends up at `position` (0 = head, len = tail). Keep prev/next consistent."""
                    raise NotImplementedError

                def delete(self, position: int) -> Any:
                    """Remove and return the value at `position`."""
                    raise NotImplementedError

                def reverse(self) -> None:
                    """Reverse in place. 0 or 1 nodes is a no-op."""
                    raise NotImplementedError

                def detect_cycle(self) -> bool:
                    raise NotImplementedError

                def to_list(self) -> list:
                    """Values head -> tail, for assertions."""
                    raise NotImplementedError

                def __len__(self) -> int:
                    raise NotImplementedError
        ''',
    }, "tests/test_linked_list.py", [
        "test_insert_delete_at_head_tail_and_middle",
        "test_insert_delete_on_empty_and_down_to_empty",
        "test_reverse_empty_and_single_node_is_noop",
        "test_detect_cycle_none_self_loop_and_mid_list",
    ]),

    P(10, "lru-cache", {
        "lru_cache.py": r'''
            """Doubly linked list + hash map combo."""
            from typing import Any


            class _Node:
                def __init__(self, key: Any, value: Any):
                    self.key = key
                    self.value = value
                    self.prev: "_Node | None" = None
                    self.next: "_Node | None" = None


            class LRUCache:
                def __init__(self, capacity: int):
                    raise NotImplementedError

                def get(self, key: Any) -> Any:
                    """Value for key (and mark it most recent), or a clear miss."""
                    raise NotImplementedError

                def put(self, key: Any, value: Any) -> None:
                    """Insert/update and mark most recent. Over capacity: evict the least recently used."""
                    raise NotImplementedError

                def __len__(self) -> int:
                    raise NotImplementedError
        ''',
    }, "tests/test_eviction.py", [
        "test_capacity_zero_and_one",
        "test_put_existing_key_updates_and_refreshes_recency",
        "test_get_on_evicted_key_is_miss",
        "test_music_shuffle_no_repeat_until_all_played",
    ], notes=["The last test stub is for the music-queue variant. Delete it if you build the LRU cache."]),

    P(11, "expr-evaluator", {
        "tokenizer.py": r'''
            """Splits an expression string into tokens."""


            class ParseError(ValueError):
                """Malformed expression (unbalanced parentheses, stray characters, ...)."""


            def tokenize(expr: str) -> list[str]:
                """Numbers (multi-digit, decimals), operators, and parens, ignoring spacing."""
                raise NotImplementedError
        ''',
        "infix_to_postfix.py": r'''
            """Shunting-yard (or equivalent)."""


            def to_postfix(tokens: list[str]) -> list[str]:
                """Infix tokens -> postfix tokens, honoring precedence and associativity (^ is right-assoc)."""
                raise NotImplementedError
        ''',
        "evaluator.py": r'''
            """Evaluates postfix using a stack."""
            from infix_to_postfix import to_postfix
            from tokenizer import tokenize


            def eval_postfix(postfix: list[str]) -> float:
                """Evaluate postfix tokens with a stack."""
                raise NotImplementedError


            def evaluate(expr: str) -> float:
                return eval_postfix(to_postfix(tokenize(expr)))
        ''',
    }, "tests/test_evaluator.py", [
        "test_unbalanced_parentheses_raise_parse_error",
        "test_exponent_precedence_is_right_associative",
        "test_unary_minus_vs_binary_minus",
        "test_division_by_zero",
        "test_multi_digit_decimals_and_irregular_spacing",
    ]),

    P(12, "browser-history", {
        "history.py": r'''
            """Two stacks: back_stack, forward_stack."""


            class BrowserHistory:
                def __init__(self, homepage: str):
                    raise NotImplementedError

                @property
                def current(self) -> str:
                    raise NotImplementedError

                def visit(self, url: str) -> None:
                    """Navigate to url. Clears forward history."""
                    raise NotImplementedError

                def back(self) -> str:
                    """Go back one page and return the current page. Nothing before: no-op."""
                    raise NotImplementedError

                def forward(self) -> str:
                    """Go forward one page and return the current page. Nothing ahead: no-op."""
                    raise NotImplementedError
        ''',
    }, "tests/test_history.py", [
        "test_back_with_no_history_is_noop",
        "test_new_visit_after_back_clears_forward_history",
        "test_repeated_back_past_first_page",
        "test_same_url_visited_twice_in_a_row_policy",
    ]),

    P(13, "queue-deque", {
        "circular_queue.py": r'''
            from typing import Any


            class CircularQueue:
                """Fixed-size array with wrapping front/rear indices."""

                def __init__(self, capacity: int):
                    raise NotImplementedError

                def enqueue(self, value: Any) -> None:
                    """Add at rear. When full: reject or overwrite oldest, your documented policy."""
                    raise NotImplementedError

                def dequeue(self) -> Any:
                    """Remove from front (FIFO)."""
                    raise NotImplementedError

                def peek(self) -> Any:
                    raise NotImplementedError

                def is_full(self) -> bool:
                    raise NotImplementedError

                def is_empty(self) -> bool:
                    raise NotImplementedError

                def __len__(self) -> int:
                    raise NotImplementedError
        ''',
        "deque.py": r'''
            from typing import Any


            class Deque:
                """O(1) push/pop at both ends."""

                def __init__(self, capacity: int | None = None):
                    raise NotImplementedError

                def push_front(self, value: Any) -> None:
                    raise NotImplementedError

                def push_back(self, value: Any) -> None:
                    raise NotImplementedError

                def pop_front(self) -> Any:
                    raise NotImplementedError

                def pop_back(self) -> Any:
                    raise NotImplementedError

                def is_empty(self) -> bool:
                    raise NotImplementedError

                def __len__(self) -> int:
                    raise NotImplementedError
        ''',
    }, "tests/test_wraparound.py", [
        "test_enqueue_on_full_queue_follows_policy",
        "test_dequeue_on_empty_queue",
        "test_front_rear_wraparound_past_array_end",
        "test_capacity_boundary_n_minus_1_vs_n_items",
    ]),

    DIRS(14, "job-processor-or-sliding-max",
        D("A_job-processor", {
            "job_queue.py": r'''
                """Heap-based priority queue."""
                from dataclasses import dataclass
                from typing import Any


                @dataclass
                class Job:
                    id: int
                    priority: int
                    payload: Any = None


                class JobQueue:
                    def __init__(self):
                        raise NotImplementedError

                    def submit_job(self, priority: int, payload: Any = None) -> Job:
                        """Enqueue a new job and return it (with its assigned id)."""
                        raise NotImplementedError

                    def process_next(self) -> Job:
                        """Remove and return the highest-priority job."""
                        raise NotImplementedError

                    def update_priority(self, job_id: int, priority: int) -> None:
                        """Change a queued job's priority (heaps have no update-in-place, so you need a workaround)."""
                        raise NotImplementedError

                    def __len__(self) -> int:
                        raise NotImplementedError
            ''',
        }, "tests/test_priority_order.py", [
            "test_equal_priority_tie_breaking",
            "test_process_next_on_empty_queue",
            "test_priority_change_after_submission",
        ], edge=0),
        D("B_sliding-max-dashboard", {
            "sliding_window_max.py": r'''
                """Monotonic deque."""


                class SlidingWindowMax:
                    def __init__(self, window: int):
                        """Track the max over the last `window` events."""
                        raise NotImplementedError

                    def push(self, timestamp: float, value: float) -> None:
                        raise NotImplementedError

                    def current_max(self) -> float | None:
                        """Max within the current (possibly partial) window."""
                        raise NotImplementedError
            ''',
            "stream_simulator.py": r'''
                """Generates the event feed for testing."""
                import random


                def generate_events(n: int, *, seed: int | None = None, start: float = 0.0, max_gap: float = 1.0,
                                    value_range: tuple[int, int] = (0, 100)) -> list[tuple[float, int]]:
                    """n (timestamp, value) events with increasing timestamps and random int values."""
                    rng = random.Random(seed)
                    t, events = start, []
                    for _ in range(n):
                        t += rng.uniform(0, max_gap)
                        events.append((t, rng.randint(*value_range)))
                    return events


                if __name__ == "__main__":
                    ev = generate_events(50, seed=1, value_range=(0, 3))
                    assert len(ev) == 50 and all(a[0] <= b[0] for a, b in zip(ev, ev[1:]))
                    assert generate_events(5, seed=7) == generate_events(5, seed=7)
                    print("stream_simulator ok")
            ''',
        }, "tests/test_window_max.py", [
            "test_partial_window_before_n_events",
            "test_max_evicted_when_it_leaves_window",
            "test_duplicate_max_values_evicted_correctly",
        ], edge=1),
    ),
]
