"""Derives the min cut from the final residual graph."""
from collections.abc import Hashable

from graph import FlowGraph


def min_cut(graph: FlowGraph, residual: dict, source: Hashable) -> list[tuple[Hashable, Hashable]]:
    """Edges crossing from the source-reachable side to the rest."""
    raise NotImplementedError
