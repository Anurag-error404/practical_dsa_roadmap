"""Builds a composite comparator from a key order."""
from collections.abc import Callable
from functools import cmp_to_key

from models import Item


def build_comparator(order: list[str]) -> Callable[[Item, Item], int]:
    """cmp(a, b) -> negative/0/positive, comparing by order[0], then order[1], ..."""
    raise NotImplementedError


def sort_items(items: list[Item], order: list[str]) -> list[Item]:
    return sorted(items, key=cmp_to_key(build_comparator(order)))
