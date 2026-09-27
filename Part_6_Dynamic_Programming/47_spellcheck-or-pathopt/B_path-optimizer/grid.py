"""Per-cell movement costs; None marks an obstacle. Storage only."""
Cell = tuple[int, int]


class CostGrid:
    def __init__(self, costs: list[list[float | None]]):
        self.costs = costs
        self.rows = len(costs)
        self.cols = len(costs[0]) if costs else 0

    def in_bounds(self, cell: Cell) -> bool:
        r, c = cell
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_obstacle(self, cell: Cell) -> bool:
        r, c = cell
        return self.costs[r][c] is None

    def cost(self, cell: Cell) -> float | None:
        r, c = cell
        return self.costs[r][c]
