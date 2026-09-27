from dataclasses import dataclass


@dataclass
class Item:
    weight: float
    value: float


def fractional_knapsack(items: list[Item], capacity: float) -> float:
    """Max value when items may be taken fractionally."""
    raise NotImplementedError
