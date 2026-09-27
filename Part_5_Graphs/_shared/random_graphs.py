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
