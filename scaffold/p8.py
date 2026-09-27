from dsl import D, DIRS, FENWICK_REUSE, P

SHARED = {
    "bits.py": r'''
        """Bitmask constants and display helpers. Deliberately no set/clear/count logic; that's the exercise."""
        MASK32 = (1 << 32) - 1
        MASK64 = (1 << 64) - 1
        INT32_MIN, INT32_MAX = -(1 << 31), (1 << 31) - 1


        def bit(i: int) -> int:
            """Mask with only bit i set."""
            return 1 << i


        def fmt_bin(x: int, width: int = 8) -> str:
            """x as a fixed-width binary string, grouped by nibble. Negatives show their two's-complement bits;
            bits above `width` are dropped (display only)."""
            s = format(x & ((1 << width) - 1), f"0{width}b")
            return "_".join(s[i:i + 4] for i in range(0, width, 4)) if width % 4 == 0 else s


        if __name__ == "__main__":
            assert bit(0) == 1 and bit(5) == 32
            assert fmt_bin(5) == "0000_0101" and fmt_bin(-1) == "1111_1111" and fmt_bin(5, 3) == "101"
            assert MASK32 == 0xFFFFFFFF and INT32_MAX == 2**31 - 1
            print("bits ok")
    ''',
    "fixtures.py": r'''
        """Save/replay range-query fixtures (array + op sequence) as JSON, for segment/Fenwick tree tests.

        Ops are ("update", index, value) or ("query", left, right) with 0 <= left <= right < n.
        Invalid ranges are yours to construct by hand in tests.
        """
        import json
        import random
        from pathlib import Path

        Op = tuple


        def random_array(n: int, max_value: int = 100, *, seed: int | None = None) -> list[int]:
            rng = random.Random(seed)
            return [rng.randint(0, max_value) for _ in range(n)]


        def random_ops(n: int, count: int, *, max_value: int = 100, update_p: float = 0.5, seed: int | None = None) -> list[Op]:
            """`count` valid ops over an array of length n (none if n == 0)."""
            rng = random.Random(seed)
            ops: list[Op] = []
            for _ in range(count if n else 0):
                if rng.random() < update_p:
                    ops.append(("update", rng.randrange(n), rng.randint(0, max_value)))
                else:
                    left = rng.randrange(n)
                    ops.append(("query", left, rng.randrange(left, n)))
            return ops


        def save_fixture(path: str | Path, array: list, ops: list[Op]) -> None:
            Path(path).write_text(json.dumps({"array": array, "ops": [list(op) for op in ops]}, indent=1))


        def load_fixture(path: str | Path) -> tuple[list, list[Op]]:
            data = json.loads(Path(path).read_text())
            return data["array"], [tuple(op) for op in data["ops"]]


        if __name__ == "__main__":
            import tempfile

            arr, ops = random_array(10, seed=1), random_ops(10, 50, seed=1)
            assert all(0 <= a < 10 and (kind == "update" or a <= b < 10) for kind, a, b in ops)
            assert random_ops(0, 5) == [] and random_ops(1, 3, seed=2) == random_ops(1, 3, seed=2)
            with tempfile.TemporaryDirectory() as d:
                save_fixture(Path(d) / "f.json", arr, ops)
                assert load_fixture(Path(d) / "f.json") == (arr, ops)
            print("fixtures ok")
    ''',
}

PROJECTS = [
    P(50, "bitmask-utils", {
        "subset_generator.py": r'''
            """Bitmask iteration, 0 to 2^n - 1."""


            def subsets(items: list) -> list[list]:
                """Every subset, one per mask in range(2 ** len(items))."""
                raise NotImplementedError
        ''',
        "single_number.py": r'''
            """XOR trick."""


            def single_number(nums: list[int]) -> int:
                """The one value appearing an odd number of times (precondition: exactly one such value)."""
                raise NotImplementedError
        ''',
        "bit_counter.py": r'''
            """Brian Kernighan's algorithm."""


            def count_bits(x: int) -> int:
                """Number of set bits. Negative-number convention is yours to document."""
                raise NotImplementedError
        ''',
    }, "tests/test_bitmask.py", [
        "test_empty_set_yields_only_empty_subset",
        "test_large_ints_vs_fixed_bit_width",
        "test_negative_numbers_twos_complement",
        "test_single_number_precondition_violation_documented",
    ], extra_imports=["from bits import MASK32, MASK64, bit, fmt_bin"]),

    DIRS(51, "permissions-or-bloomfilter",
        D("A_permissions", {
            "permission_flags.py": r'''
                class FlagRegistry:
                    """Named permission flags, each owning one bit."""

                    def __init__(self, names: tuple[str, ...] = ()):
                        raise NotImplementedError

                    def define(self, name: str) -> int:
                        """Allocate the next free bit to `name` and return its mask."""
                        raise NotImplementedError

                    def mask(self, name: str) -> int:
                        """Mask for a defined flag. Undefined flags must raise, not return 0."""
                        raise NotImplementedError

                    def names(self, mask: int) -> list[str]:
                        """Flag names set in mask (for display)."""
                        raise NotImplementedError
            ''',
            "user_permissions.py": r'''
                from permission_flags import FlagRegistry


                class UserPermissions:
                    def __init__(self, registry: FlagRegistry):
                        raise NotImplementedError

                    def grant(self, user: str, *flags: str) -> None:
                        """OR the flags in."""
                        raise NotImplementedError

                    def revoke(self, user: str, *flags: str) -> None:
                        """AND-NOT the flags out."""
                        raise NotImplementedError

                    def check(self, user: str, flag: str) -> bool:
                        raise NotImplementedError

                    def mask(self, user: str) -> int:
                        raise NotImplementedError
            ''',
        }, "tests/test_permissions.py", [
            "test_undefined_flag_check_raises",
            "test_grant_or_and_revoke_and_not_bit_logic",
            "test_zero_vs_all_permissions",
        ], edge=0, extra_imports=["from bits import bit, fmt_bin"]),
        D("B_bloom-filter", {
            "bloom_filter.py": r'''
                """Bit array plus multiple hash functions."""


                class BloomFilter:
                    def __init__(self, size_bits: int, num_hashes: int):
                        raise NotImplementedError

                    def add(self, item: str) -> None:
                        raise NotImplementedError

                    def might_contain(self, item: str) -> bool:
                        """False = definitely absent; True = possibly present. Added items must always be True."""
                        raise NotImplementedError
            ''',
        }, "tests/test_bloom_filter.py", [
            "test_false_positive_rate_measured",
            "test_no_false_negatives_ever",
            "test_undersized_filter_tradeoff_documented",
        ], edge=1),
    ),

    P(52, "segment-fenwick", {
        "segment_tree.py": r'''
            """Range query plus point update."""
            import operator
            from collections.abc import Callable


            class SegmentTree:
                def __init__(self, values: list[int], combine: Callable[[int, int], int] = operator.add, identity: int = 0):
                    """combine/identity select the aggregate: (add, 0) = sum, (min, inf) = min, (max, -inf) = max."""
                    raise NotImplementedError

                def query(self, left: int, right: int) -> int:
                    """Aggregate over values[left..right] inclusive, in O(log n)."""
                    raise NotImplementedError

                def update(self, index: int, value: int) -> None:
                    """Set values[index] = value (set, not add), in O(log n)."""
                    raise NotImplementedError
        ''',
        "fenwick_tree.py": r'''
            """Binary indexed tree, prefix-sum based."""


            class FenwickTree:
                def __init__(self, values: list[int]):
                    raise NotImplementedError

                def update(self, index: int, value: int) -> None:
                    """Set values[index] = value (not add), in O(log n)."""
                    raise NotImplementedError

                def prefix_sum(self, index: int) -> int:
                    """Sum of values[0..index] inclusive."""
                    raise NotImplementedError

                def query(self, left: int, right: int) -> int:
                    """Sum of values[left..right] inclusive."""
                    raise NotImplementedError
        ''',
    }, "tests/test_range_queries.py", [
        "test_invalid_range_or_out_of_bounds_rejected",
        "test_single_element_range",
        "test_re_update_is_set_not_add",
        "test_full_array_range",
        "test_empty_array",
    ], extra_imports=["from fixtures import load_fixture, random_array, random_ops, save_fixture"]),

    P(53, "realtime-analytics", {
        "ingest.py": r'''
            """Receives events and updates the underlying structure."""
            from fenwick_tree import FenwickTree


            class Ingestor:
                def __init__(self, start_time: float, bucket_seconds: float = 1.0, capacity: int = 86_400):
                    """Events map to time buckets of `bucket_seconds`, starting at start_time."""
                    raise NotImplementedError

                def bucket(self, timestamp: float) -> int:
                    """Time bucket index for a timestamp."""
                    raise NotImplementedError

                def ingest(self, timestamp: float, value: float) -> None:
                    """Point-update the structure. Late (out-of-order) events: accept or reject, documented."""
                    raise NotImplementedError
        ''',
        "fenwick_tree.py": FENWICK_REUSE,
        "query_api.py": r'''
            """Range query endpoint."""
            from ingest import Ingestor


            class QueryAPI:
                def __init__(self, ingestor: Ingestor):
                    self.ingestor = ingestor

                def range_sum(self, t0: float, t1: float) -> float:
                    """Sum of values in [t0, t1]. No events there: 0."""
                    raise NotImplementedError

                def range_min(self, t0: float, t1: float) -> float | None:
                    """Min in [t0, t1]; empty range is an explicit null/error. (Fenwick can't do min alone.)"""
                    raise NotImplementedError

                def range_max(self, t0: float, t1: float) -> float | None:
                    raise NotImplementedError
        ''',
    }, "tests/test_analytics.py", [
        "test_empty_range_returns_default",
        "test_out_of_order_event_policy",
        "test_high_throughput_point_updates_no_rebuild",
        "test_future_range_returns_available_data",
    ]),

    P(54, "string-matching", {
        "kmp.py": r'''
            """Failure function plus search."""


            def failure_function(pattern: str) -> list[int]:
                """lps[i] = length of the longest proper prefix of pattern[:i+1] that is also a suffix."""
                raise NotImplementedError


            def kmp_search(text: str, pattern: str) -> list[int]:
                """Every start index of pattern in text, overlapping matches included."""
                raise NotImplementedError
        ''',
        "rabin_karp.py": r'''
            """Rolling hash plus spurious-hit verification."""


            def rabin_karp_search(text: str, pattern: str, base: int = 256, mod: int = 1_000_000_007) -> list[int]:
                """Every start index of pattern in text. A small `mod` in tests forces spurious hash hits."""
                raise NotImplementedError
        ''',
    }, "tests/test_matching.py", [
        "test_pattern_longer_than_text_returns_empty",
        "test_overlapping_matches_all_found",
        "test_empty_pattern_convention",
        "test_rabin_karp_spurious_hit_verified",
    ]),

    P(55, "catalogue-search", {
        "indexer.py": r'''
            """Builds an inverted index across documents."""
            from pathlib import Path


            def load_documents(folder: str | Path) -> dict[str, str]:
                """doc_id -> text for every document in folder."""
                raise NotImplementedError


            def tokenize(text: str) -> list[str]:
                """Terms as indexed. Whole-word vs partial matching is decided here."""
                raise NotImplementedError


            class InvertedIndex:
                def __init__(self):
                    raise NotImplementedError

                def add_document(self, doc_id: str, text: str) -> None:
                    """Index one document (incremental add/update policy is yours)."""
                    raise NotImplementedError

                def postings(self, term: str) -> dict[str, list[int]]:
                    """doc_id -> positions of term."""
                    raise NotImplementedError
        ''',
        "kmp_or_rabinkarp.py": r'''
            """Copy in your Project 54 matcher, for exact phrase matching within candidate docs."""


            def find_all(text: str, pattern: str) -> list[int]:
                raise NotImplementedError
        ''',
        "ranker.py": r'''
            """Scores and ranks results."""


            def rank(hits: dict[str, list[int]], doc_lengths: dict[str, int], limit: int | None = None) -> list[tuple[str, float]]:
                """(doc_id, score) best first, from each doc's match positions."""
                raise NotImplementedError
        ''',
        "query_api.py": r'''
            from dataclasses import dataclass

            from indexer import InvertedIndex


            @dataclass
            class SearchResult:
                doc_id: str
                score: float
                positions: list[int]


            class CatalogueSearch:
                def __init__(self, documents: dict[str, str]):
                    self.documents = dict(documents)
                    self.index = InvertedIndex()
                    for doc_id, text in self.documents.items():
                        self.index.add_document(doc_id, text)

                def search(self, query: str, limit: int = 10) -> list[SearchResult]:
                    """Ranked documents containing the term/phrase. No hits: empty list."""
                    raise NotImplementedError
        ''',
    }, "tests/test_search.py", [
        "test_term_in_zero_documents_returns_empty",
        "test_very_common_term_ranking_meaningful",
        "test_whole_word_vs_partial_match_policy",
        "test_documents_added_after_index_built",
        "test_large_set_uses_inverted_index_not_scan",
    ]),

    P(56, "max-flow", {
        "graph.py": r'''
            """Capacities plus residual graph."""
            from collections.abc import Hashable


            class FlowGraph:
                def __init__(self):
                    self.capacity: dict[Hashable, dict[Hashable, float]] = {}

                def add_node(self, u: Hashable) -> None:
                    self.capacity.setdefault(u, {})

                def add_edge(self, u: Hashable, v: Hashable, capacity: float) -> None:
                    """Directed u->v. Parallel edges merge by summing capacity."""
                    self.add_node(u)
                    self.add_node(v)
                    self.capacity[u][v] = self.capacity[u].get(v, 0) + capacity

                def nodes(self) -> list[Hashable]:
                    return list(self.capacity)

                def residual(self) -> dict[Hashable, dict[Hashable, float]]:
                    """Initial residual graph, reverse edges included."""
                    raise NotImplementedError
        ''',
        "ford_fulkerson.py": r'''
            """BFS-based (Edmonds-Karp) for guaranteed termination."""
            from collections.abc import Hashable

            from graph import FlowGraph


            def max_flow(graph: FlowGraph, source: Hashable, sink: Hashable) -> tuple[float, dict]:
                """(max flow value, final residual graph)."""
                raise NotImplementedError
        ''',
        "min_cut.py": r'''
            """Derives the min cut from the final residual graph."""
            from collections.abc import Hashable

            from graph import FlowGraph


            def min_cut(graph: FlowGraph, residual: dict, source: Hashable) -> list[tuple[Hashable, Hashable]]:
                """Edges crossing from the source-reachable side to the rest."""
                raise NotImplementedError
        ''',
    }, "tests/test_max_flow.py", [
        "test_source_equals_sink_rejected",
        "test_no_path_max_flow_zero",
        "test_cycles_handled_via_residual_graph",
        "test_zero_capacity_edges_ignored",
        "test_max_flow_equals_min_cut_capacity",
    ]),

    P(57, "ride-job-matching", {
        "models.py": r'''
            """Riders/tasks are Requests; drivers/workers are Resources."""
            from dataclasses import dataclass, field

            Location = tuple[float, float]


            @dataclass
            class Request:
                id: str
                location: Location
                required_skill: str | None = None
                requested_at: float = 0.0


            @dataclass
            class Resource:
                id: str
                location: Location
                available: bool = True
                skills: frozenset[str] = frozenset()


            @dataclass
            class Assignment:
                request_id: str
                resource_id: str
                cost: float


            @dataclass
            class MatchResult:
                assignments: list[Assignment] = field(default_factory=list)
                unmatched_requests: list[str] = field(default_factory=list)
                idle_resources: list[str] = field(default_factory=list)
        ''',
        "matcher.py": r'''
            """Bipartite matching (greedy or Hopcroft-Karp)."""
            from models import MatchResult, Request, Resource


            def cost(request: Request, resource: Resource) -> float | None:
                """Match cost (distance, wait, ...), or None if incompatible."""
                raise NotImplementedError


            def match(requests: list[Request], resources: list[Resource]) -> MatchResult:
                """Deterministic assignment. Unmatched requests and idle resources are reported, not dropped."""
                raise NotImplementedError
        ''',
        "simulator.py": r'''
            """Runs matching over simulated requests."""
            import random

            from models import MatchResult, Request, Resource


            def random_requests(n: int, *, bounds: float = 10.0, skills: tuple[str, ...] = (), seed: int | None = None) -> list[Request]:
                rng = random.Random(seed)
                return [Request(f"r{i}", (rng.uniform(0, bounds), rng.uniform(0, bounds)),
                                rng.choice(skills) if skills else None, float(i)) for i in range(n)]


            def random_resources(n: int, *, bounds: float = 10.0, skills: tuple[str, ...] = (), seed: int | None = None) -> list[Resource]:
                rng = random.Random(seed)
                return [Resource(f"d{i}", (rng.uniform(0, bounds), rng.uniform(0, bounds)), True,
                                 frozenset(rng.sample(skills, rng.randint(1, len(skills)))) if skills else frozenset())
                        for i in range(n)]


            class Simulator:
                def __init__(self, resources: list[Resource]):
                    self.resources = {r.id: r for r in resources}

                def step(self, new_requests: list[Request]) -> MatchResult:
                    """Match a batch of new requests against currently available resources."""
                    raise NotImplementedError

                def set_unavailable(self, resource_id: str) -> None:
                    """Take a resource out mid-simulation (re-matching policy is yours)."""
                    raise NotImplementedError


            if __name__ == "__main__":
                rs = random_requests(5, skills=("a", "b"), seed=1)
                ds = random_resources(3, skills=("a", "b"), seed=1)
                assert len(rs) == 5 and all(r.required_skill in ("a", "b") for r in rs)
                assert all(d.skills and d.skills <= {"a", "b"} for d in ds)
                assert random_requests(3, seed=9) == random_requests(3, seed=9)
                print("simulator plumbing ok")
        ''',
    }, "tests/test_matching.py", [
        "test_more_requests_than_resources_reports_unmatched",
        "test_incompatible_resource_reported_idle",
        "test_quality_ties_resolved_deterministically",
        "test_resource_unavailable_mid_simulation",
    ]),
]
