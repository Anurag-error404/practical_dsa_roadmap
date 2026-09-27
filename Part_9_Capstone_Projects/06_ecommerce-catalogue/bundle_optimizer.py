"""Knapsack-based bundle suggestion."""
from models import Bundle, Product


def suggest_bundle(products: list[Product], budget: float) -> Bundle:
    """Value-maximizing bundle within budget. Nothing fits: empty bundle plus a message."""
    raise NotImplementedError
