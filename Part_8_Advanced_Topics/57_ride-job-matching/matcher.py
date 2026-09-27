"""Bipartite matching (greedy or Hopcroft-Karp)."""
from models import MatchResult, Request, Resource


def cost(request: Request, resource: Resource) -> float | None:
    """Match cost (distance, wait, ...), or None if incompatible."""
    raise NotImplementedError


def match(requests: list[Request], resources: list[Resource]) -> MatchResult:
    """Deterministic assignment. Unmatched requests and idle resources are reported, not dropped."""
    raise NotImplementedError
