from dsl import D, DIRS, GRAPH, UNION_FIND_REUSE, P

SHARED = {
    "random_graphs.py": r'''
        """Random graph generators for stress tests. Nodes are ints 0..n-1; edges are (u, v, weight) tuples.

            g = Graph.from_edges(random_edges(50, 0.1, seed=1), nodes=range(50))
        """
        import random

        Edge = tuple[int, int, int]


        def _weight(rng: random.Random, weights: tuple[int, int] | None) -> int:
            return rng.randint(*weights) if weights else 1


        def random_edges(n: int, p: float = 0.3, *, directed: bool = False, weights: tuple[int, int] | None = None,
                         self_loops: bool = False, seed: int | None = None) -> list[Edge]:
            """Erdos-Renyi G(n, p): each possible edge exists with probability p.

            Undirected graphs emit each pair once (u < v). weights=(lo, hi) draws random ints (negatives allowed,
            which in a directed graph can create negative cycles).
            """
            rng = random.Random(seed)
            edges = []
            for u in range(n):
                for v in range(n):
                    if (u == v and not self_loops) or (not directed and v < u):
                        continue
                    if rng.random() < p:
                        edges.append((u, v, _weight(rng, weights)))
            return edges


        def random_dag(n: int, p: float = 0.3, *, weights: tuple[int, int] | None = None, seed: int | None = None) -> list[Edge]:
            """Directed acyclic: edges only go forward in a hidden random node order."""
            rng = random.Random(seed)
            order = list(range(n))
            rng.shuffle(order)
            return [(order[i], order[j], _weight(rng, weights))
                    for i in range(n) for j in range(i + 1, n) if rng.random() < p]


        def random_connected(n: int, extra: int = 0, *, weights: tuple[int, int] | None = None, seed: int | None = None) -> list[Edge]:
            """Undirected and connected: a random spanning tree plus `extra` additional distinct edges."""
            rng = random.Random(seed)
            nodes = list(range(n))
            rng.shuffle(nodes)
            edges = [(nodes[rng.randrange(i)], nodes[i], _weight(rng, weights)) for i in range(1, n)]
            present = {frozenset(e[:2]) for e in edges}
            room = n * (n - 1) // 2 - len(present)
            for _ in range(min(extra, room)):
                while True:
                    u, v = rng.sample(range(n), 2)
                    if frozenset((u, v)) not in present:
                        present.add(frozenset((u, v)))
                        edges.append((u, v, _weight(rng, weights)))
                        break
            return edges


        def random_grid(rows: int, cols: int, wall_p: float = 0.25, *, seed: int | None = None) -> list[list[int]]:
            """rows x cols grid of 0 (open) / 1 (wall). No solvability guarantee."""
            rng = random.Random(seed)
            return [[int(rng.random() < wall_p) for _ in range(cols)] for _ in range(rows)]


        if __name__ == "__main__":
            assert random_edges(5, 1.0) == [(u, v, 1) for u in range(5) for v in range(u + 1, 5)]
            assert len(random_edges(4, 1.0, directed=True, self_loops=True)) == 16
            from graphlib import TopologicalSorter
            ts = TopologicalSorter()
            for u, v, _ in random_dag(30, 0.5, seed=3):
                ts.add(v, u)
            list(ts.static_order())  # raises CycleError if the DAG isn't acyclic
            tree = random_connected(20, extra=5, weights=(-3, 9), seed=2)
            assert len(tree) == 24 and all(-3 <= w <= 9 for *_, w in tree)
            adj = {i: set() for i in range(20)}
            for u, v, _ in tree:
                adj[u].add(v); adj[v].add(u)
            reach, todo = {0}, [0]
            while todo:
                for v in adj[todo.pop()] - reach:
                    reach.add(v); todo.append(v)
            assert len(reach) == 20
            assert len(random_connected(4, extra=99)) == 6 and random_connected(1) == []
            g = random_grid(3, 4, seed=1)
            assert len(g) == 3 and all(len(r) == 4 and set(r) <= {0, 1} for r in g)
            print("random_graphs ok")
    ''',
}

PROJECTS = [
    P(31, "graph-traversal", {
        "graph.py": GRAPH,
        "bfs.py": r'''
            from collections.abc import Hashable

            from graph import Graph


            def bfs(graph: Graph, start: Hashable) -> list:
                """Nodes in breadth-first visit order from start."""
                raise NotImplementedError
        ''',
        "dfs.py": r'''
            from collections.abc import Hashable

            from graph import Graph


            def dfs(graph: Graph, start: Hashable) -> list:
                """Nodes in depth-first visit order from start."""
                raise NotImplementedError
        ''',
        "cycle_detection.py": r'''
            """Separate directed/undirected logic."""
            from graph import Graph


            def has_cycle_directed(graph: Graph) -> bool:
                raise NotImplementedError


            def has_cycle_undirected(graph: Graph) -> bool:
                raise NotImplementedError
        ''',
        "connected_components.py": r'''
            from graph import Graph


            def connected_components(graph: Graph) -> list[set]:
                """Every node appears in exactly one component, including isolated ones."""
                raise NotImplementedError
        ''',
    }, "tests/test_traversal.py", [
        "test_disconnected_graph_components_cover_all_nodes",
        "test_self_loops",
        "test_parallel_edges",
        "test_cycle_detection_directed_vs_undirected",
        "test_empty_graph_and_single_isolated_node",
    ], extra_imports=["from random_graphs import random_edges"]),

    P(32, "degrees-of-separation", {
        "graph_loader.py": r'''
            """Loads edges into an adjacency list."""
            from pathlib import Path


            def load_edges(path: str | Path) -> dict[str, set[str]]:
                """Undirected friend graph from a file of "a b" pairs, one per line."""
                raise NotImplementedError
        ''',
        "bfs_path.py": r'''
            """Shortest path plus degree count."""


            def shortest_path(adj: dict[str, set[str]], a: str, b: str) -> list[str] | None:
                """One shortest path a -> ... -> b (deterministic among ties), or None if not connected."""
                raise NotImplementedError


            def degrees(adj: dict[str, set[str]], a: str, b: str) -> int | None:
                """Edges on the shortest path (0 when a == b), or None if not connected."""
                raise NotImplementedError
        ''',
        "cli.py": r'''
            """Query interface."""
            import argparse

            from bfs_path import shortest_path
            from graph_loader import load_edges


            def format_result(a: str, b: str, path: list[str] | None) -> str:
                """Degree count and path, or an explicit "not connected"."""
                raise NotImplementedError


            def main(argv: list[str] | None = None) -> None:
                ap = argparse.ArgumentParser(description="Degrees of separation between two users.")
                ap.add_argument("edges", help="file of 'a b' friendship pairs")
                ap.add_argument("a")
                ap.add_argument("b")
                args = ap.parse_args(argv)
                print(format_result(args.a, args.b, shortest_path(load_edges(args.edges), args.a, args.b)))


            if __name__ == "__main__":
                main()
        ''',
    }, "tests/test_bfs_path.py", [
        "test_same_user_is_degree_zero",
        "test_disconnected_users_report_not_connected",
        "test_bfs_efficient_on_large_graph",
        "test_equal_length_paths_choice_is_deterministic",
    ], extra_imports=["from random_graphs import random_edges"]),

    P(33, "topo-sort", {
        "graph.py": GRAPH,
        "kahns_algorithm.py": r'''
            """BFS-based, in-degree tracking."""
            from graph import Graph


            def topo_sort_kahn(graph: Graph) -> list:
                """A valid order of every node, or a clear cycle report (raise or sentinel: be consistent with DFS)."""
                raise NotImplementedError
        ''',
        "dfs_based.py": r'''
            """DFS plus stack-based approach."""
            from graph import Graph


            def topo_sort_dfs(graph: Graph) -> list:
                """A valid order of every node, or a clear cycle report (same convention as Kahn's)."""
                raise NotImplementedError
        ''',
    }, "tests/test_topo_sort.py", [
        "test_cycle_detected_and_reported",
        "test_any_valid_order_has_every_edge_pointing_forward",
        "test_disconnected_components_all_nodes_appear",
        "test_isolated_node_appears",
    ], extra_imports=["from random_graphs import random_dag"]),

    P(34, "build-system-sim", {
        "parser.py": r'''
            """Reads the dependency spec file."""
            from pathlib import Path


            def parse_spec(text: str) -> dict[str, list[str]]:
                """task -> tasks it depends on. Pick a spec format (e.g. "build: compile test")."""
                raise NotImplementedError


            def load_spec(path: str | Path) -> dict[str, list[str]]:
                return parse_spec(Path(path).read_text())
        ''',
        "topo_sort.py": r'''
            """Copy in or adapt your Project 33 topological sort."""


            def build_order(deps: dict[str, list[str]]) -> list[str]:
                """Execution order where every task comes after its dependencies."""
                raise NotImplementedError
        ''',
        "cycle_reporter.py": r'''
            """Extracts and displays the actual cycle path."""


            def find_cycle(deps: dict[str, list[str]]) -> list[str] | None:
                """The tasks forming a cycle, in order (e.g. [a, b, c, a]), or None."""
                raise NotImplementedError


            def format_cycle(cycle: list[str]) -> str:
                raise NotImplementedError
        ''',
    }, "tests/test_build_order.py", [
        "test_circular_dependency_reports_involved_tasks",
        "test_undefined_dependency_policy",
        "test_duplicate_dependency_declarations",
        "test_independent_task_still_in_output",
    ]),

    P(35, "union-find", {
        "union_find.py": r'''
            """Path compression plus union by rank."""
            from collections.abc import Hashable, Iterable


            class UnionFind:
                def __init__(self, elements: Iterable[Hashable] = (), *, path_compression: bool = True, union_by_rank: bool = True):
                    """The flags let tests and benchmarks compare with and without each optimization."""
                    raise NotImplementedError

                def find(self, x: Hashable) -> Hashable:
                    """Representative of x's set."""
                    raise NotImplementedError

                def union(self, a: Hashable, b: Hashable) -> bool:
                    """Merge the sets of a and b. Return True if they were separate."""
                    raise NotImplementedError

                def connected(self, a: Hashable, b: Hashable) -> bool:
                    raise NotImplementedError
        ''',
    }, "tests/test_union_find.py", [
        "test_union_with_itself",
        "test_find_on_unknown_element_policy",
        "test_repeated_union_is_idempotent_rank_unchanged",
        "test_path_compression_preserves_rank",
        "test_long_chain_depth_reduced_by_compression",
    ], extra_imports=["from random_graphs import random_edges"]),

    DIRS(36, "friend-circles-or-regions",
        D("A_friend-circles", {
            "union_find.py": UNION_FIND_REUSE,
            "graph_builder.py": r'''
                from collections.abc import Hashable


                def friendships(source: list[list[int]] | dict[Hashable, list[Hashable]]) -> tuple[list[Hashable], list[tuple[Hashable, Hashable]]]:
                    """Normalize an adjacency matrix or adjacency list into (people, friendship_pairs)."""
                    raise NotImplementedError
            ''',
            "region_counter.py": r'''
                from collections.abc import Hashable


                def friend_groups(people: list[Hashable], pairs: list[tuple[Hashable, Hashable]]) -> list[set]:
                    """Distinct friend groups and their members."""
                    raise NotImplementedError
            ''',
        }, "tests/test_regions.py", [
            "test_fully_disconnected_each_person_own_group",
            "test_fully_connected_one_group",
            "test_empty_input",
        ], pick=[0, 1, 3]),
        D("B_image-regions", {
            "union_find.py": UNION_FIND_REUSE,
            "grid_scanner.py": r'''
                from collections.abc import Iterator

                Cell = tuple[int, int]


                def foreground_cells(grid: list[list[int]]) -> list[Cell]:
                    raise NotImplementedError


                def neighbors(grid: list[list[int]], cell: Cell) -> Iterator[Cell]:
                    """Adjacent foreground cells. 4- vs 8-connectivity is decided (and documented) here."""
                    raise NotImplementedError
            ''',
            "region_counter.py": r'''
                Cell = tuple[int, int]


                def regions(grid: list[list[int]]) -> list[set[Cell]]:
                    """Connected foreground regions and the pixels in each."""
                    raise NotImplementedError
            ''',
        }, "tests/test_regions.py", [
            "test_fully_disconnected_each_pixel_own_region",
            "test_fully_connected_one_region",
            "test_diagonal_adjacency_rule_documented",
            "test_empty_grid",
        ], extra_imports=["from random_graphs import random_grid"]),
    ),

    P(37, "shortest-path-comparison", {
        "graph.py": GRAPH,
        "dijkstra.py": r'''
            """Heap-based."""
            from collections.abc import Hashable

            from graph import Graph


            def dijkstra(graph: Graph, source: Hashable) -> dict[Hashable, float]:
                """Shortest distance to every node (unreachable = inf). Non-negative weights only."""
                raise NotImplementedError
        ''',
        "bellman_ford.py": r'''
            """Includes negative-cycle detection."""
            from collections.abc import Hashable

            from graph import Graph


            def bellman_ford(graph: Graph, source: Hashable) -> dict[Hashable, float]:
                """Shortest distance to every node (unreachable = inf). A negative cycle must be reported."""
                raise NotImplementedError
        ''',
        "floyd_warshall.py": r'''
            """All-pairs."""
            from collections.abc import Hashable

            from graph import Graph


            def floyd_warshall(graph: Graph) -> dict[Hashable, dict[Hashable, float]]:
                """dist[u][v] for every pair (unreachable = inf)."""
                raise NotImplementedError
        ''',
    }, "tests/test_shortest_path.py", [
        "test_dijkstra_negative_weights_rejected_or_documented",
        "test_bellman_ford_reports_negative_cycle",
        "test_unreachable_nodes_are_infinite",
        "test_single_node_and_weighted_self_loop",
    ], extra_imports=["from random_graphs import random_connected, random_edges"]),

    P(38, "pathfinding-game", {
        "grid.py": r'''
            """Grid representation plus obstacle placement. Storage only."""
            from collections.abc import Iterator

            Cell = tuple[int, int]


            class Grid:
                def __init__(self, rows: int, cols: int, walls: set[Cell] | None = None):
                    self.rows = rows
                    self.cols = cols
                    self.walls: set[Cell] = set(walls or ())

                @classmethod
                def from_matrix(cls, matrix: list[list[int]]) -> "Grid":
                    """1 = wall, 0 = open (the format random_grid() produces)."""
                    return cls(len(matrix), len(matrix[0]) if matrix else 0,
                               {(r, c) for r, row in enumerate(matrix) for c, v in enumerate(row) if v})

                def in_bounds(self, cell: Cell) -> bool:
                    r, c = cell
                    return 0 <= r < self.rows and 0 <= c < self.cols

                def is_open(self, cell: Cell) -> bool:
                    return self.in_bounds(cell) and cell not in self.walls

                def place_wall(self, cell: Cell) -> None:
                    self.walls.add(cell)

                def remove_wall(self, cell: Cell) -> None:
                    self.walls.discard(cell)

                def neighbors(self, cell: Cell) -> Iterator[Cell]:
                    """Walkable cells one step from `cell`. Movement rules (4 vs 8 directions) are yours."""
                    raise NotImplementedError
        ''',
        "pathfinder.py": r'''
            """A* or Dijkstra."""
            from grid import Cell, Grid


            def find_path(grid: Grid, start: Cell, goal: Cell) -> list[Cell] | None:
                """Cells from start to goal inclusive, or None when unreachable."""
                raise NotImplementedError
        ''',
        "game_loop.py": r'''
            """Rendering plus input handling. curses (stdlib) works for a terminal version."""
            from grid import Cell, Grid


            class Game:
                def __init__(self, grid: Grid, player: Cell, npc: Cell, goal: Cell):
                    raise NotImplementedError

                def handle_input(self, key: str) -> None:
                    """Move the player or place an obstacle."""
                    raise NotImplementedError

                def tick(self) -> None:
                    """Advance one step: the NPC follows its path, recomputing only if needed."""
                    raise NotImplementedError

                def render(self) -> str:
                    raise NotImplementedError


            def main() -> None:
                raise NotImplementedError


            if __name__ == "__main__":
                main()
        ''',
    }, "tests/test_pathfinder.py", [
        "test_unreachable_goal_detected",
        "test_start_equals_goal",
        "test_new_obstacle_triggers_recompute",
        "test_recompute_only_when_path_invalidated",
    ], extra_imports=["from random_graphs import random_grid"]),

    P(39, "mst", {
        "graph.py": GRAPH,
        "prims.py": r'''
            """Heap-based."""
            from graph import Graph

            Edge = tuple


            def prim_mst(graph: Graph) -> tuple[list[Edge], float]:
                """(MST edges, total cost). Disconnected input: a spanning forest or an explicit error."""
                raise NotImplementedError
        ''',
        "kruskals.py": r'''
            """Union-find based; sorts edges by weight."""
            from graph import Graph

            Edge = tuple


            def kruskal_mst(graph: Graph) -> tuple[list[Edge], float]:
                """(MST edges, total cost). Same disconnected-graph convention as prim_mst."""
                raise NotImplementedError
        ''',
    }, "tests/test_mst.py", [
        "test_disconnected_graph_forest_or_error",
        "test_duplicate_weights_total_cost_correct",
        "test_single_node_mst_empty_cost_zero",
        "test_prim_and_kruskal_agree_on_total_cost",
    ], extra_imports=["from random_graphs import random_connected"]),

    P(40, "network-design-tool", {
        "city_loader.py": r'''
            from dataclasses import dataclass
            from pathlib import Path


            @dataclass
            class City:
                name: str
                x: float | None = None
                y: float | None = None


            def load_cities(path: str | Path) -> list[City]:
                raise NotImplementedError
        ''',
        "cost_model.py": r'''
            """Computes or loads edge costs."""
            from pathlib import Path

            from city_loader import City

            Edge = tuple[str, str, float]


            def load_costs(path: str | Path) -> list[Edge]:
                """Candidate connections (city_a, city_b, cost) from a file."""
                raise NotImplementedError


            def candidate_edges(cities: list[City], k: int | None = None) -> list[Edge]:
                """Candidate connections computed from coordinates. k limits each city to its k nearest."""
                raise NotImplementedError
        ''',
        "mst.py": r'''
            """Copy in or adapt your Project 39 MST."""
            Edge = tuple[str, str, float]


            def minimum_spanning(nodes: list[str], edges: list[Edge]) -> tuple[list[Edge], float]:
                """(chosen edges, total cost) using only the given candidate edges."""
                raise NotImplementedError
        ''',
        "report.py": r'''
            """Outputs chosen connections plus total cost."""
            Edge = tuple[str, str, float]


            def format_report(chosen: list[Edge], total: float, unreachable: list[str]) -> str:
                """Chosen connections, total cost, and any cities that can't be connected."""
                raise NotImplementedError
        ''',
    }, "tests/test_network_design.py", [
        "test_missing_direct_connections_use_available_edges_only",
        "test_isolated_city_reported",
        "test_ties_between_equal_cost_designs",
        "test_large_city_count_uses_selective_candidates",
    ]),
]
