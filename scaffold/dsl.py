from dataclasses import dataclass, field


@dataclass
class Sub:
    files: dict
    test_file: str
    tests: list
    dir: str = ""
    edge: int = 0
    pick: list | None = None
    extra_imports: list = field(default_factory=list)


@dataclass
class Project:
    n: int
    dir: str
    subs: list
    requirements: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    js: bool = False


SUB_KEYS = {"edge", "pick", "extra_imports"}


def P(n, dir, files, test_file, tests, **kw):
    sub_kw = {k: kw.pop(k) for k in list(kw) if k in SUB_KEYS}
    return Project(n, dir, [Sub(files, test_file, tests, **sub_kw)], **kw)


def D(dir, files, test_file, tests, **kw):
    return Sub(files, test_file, tests, dir=dir, **kw)


def DIRS(n, dir, *subs, **kw):
    return Project(n, dir, list(subs), **kw)


GRAPH = r'''
"""Adjacency-list graph container. Storage only: traversal and algorithms live in the other modules."""
from collections.abc import Hashable, Iterable


class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj: dict[Hashable, list[tuple[Hashable, float]]] = {}
        self.edge_list: list[tuple[Hashable, Hashable, float]] = []

    def add_node(self, u: Hashable) -> None:
        self.adj.setdefault(u, [])

    def add_edge(self, u: Hashable, v: Hashable, weight: float = 1) -> None:
        """Store u->v (plus v->u if undirected). Parallel edges are kept; an undirected self-loop is stored once."""
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, weight))
        if not self.directed and u != v:
            self.adj[v].append((u, weight))
        self.edge_list.append((u, v, weight))

    def nodes(self) -> list[Hashable]:
        return list(self.adj)

    def neighbors(self, u: Hashable) -> list[tuple[Hashable, float]]:
        """(neighbor, weight) pairs. KeyError for a node that was never added."""
        return self.adj[u]

    def edges(self) -> list[tuple[Hashable, Hashable, float]]:
        """Every edge exactly as added (an undirected edge appears once)."""
        return list(self.edge_list)

    @classmethod
    def from_edges(cls, edges: Iterable[tuple], directed: bool = False, nodes: Iterable[Hashable] = ()) -> "Graph":
        """Build from (u, v) or (u, v, weight) tuples; `nodes` adds isolated nodes too."""
        g = cls(directed)
        for u in nodes:
            g.add_node(u)
        for e in edges:
            g.add_edge(*e)
        return g
'''

TRIE_NODE = r'''
class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False
'''

UNION_FIND_REUSE = r'''
"""Union-Find. Copy in your Project 35 implementation (or rewrite it)."""
from collections.abc import Hashable


class UnionFind:
    def __init__(self, elements=()):
        raise NotImplementedError

    def find(self, x: Hashable) -> Hashable:
        """Representative of x's set."""
        raise NotImplementedError

    def union(self, a: Hashable, b: Hashable) -> bool:
        """Merge the sets of a and b. Return True if they were separate."""
        raise NotImplementedError

    def connected(self, a: Hashable, b: Hashable) -> bool:
        raise NotImplementedError
'''

FENWICK_REUSE = r'''
"""Fenwick tree (binary indexed tree). Copy in or adapt your Project 52 implementation."""


class FenwickTree:
    def __init__(self, size: int):
        """All-zero tree over indices 0..size-1."""
        raise NotImplementedError

    def add(self, index: int, delta: float) -> None:
        """Point update: values[index] += delta."""
        raise NotImplementedError

    def prefix_sum(self, index: int) -> float:
        """Sum of values[0..index] inclusive."""
        raise NotImplementedError

    def range_sum(self, left: int, right: int) -> float:
        """Sum of values[left..right] inclusive."""
        raise NotImplementedError
'''
