"""Outputs chosen connections plus total cost."""
Edge = tuple[str, str, float]


def format_report(chosen: list[Edge], total: float, unreachable: list[str]) -> str:
    """Chosen connections, total cost, and any cities that can't be connected."""
    raise NotImplementedError
