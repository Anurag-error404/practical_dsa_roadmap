"""Times naive vs memoized vs tabulated."""
import memoized
import naive_recursive
import tabulated

IMPLEMENTATIONS = {"naive": naive_recursive, "memoized": memoized, "tabulated": tabulated}


def run(n_values: list[int], trials: int = 3) -> list[dict]:
    """Rows of {"impl", "problem", "n", "time_ms"}. Cap or time out the naive version at large n."""
    raise NotImplementedError


if __name__ == "__main__":
    for row in run([10, 20, 30, 35]):
        print(row)
