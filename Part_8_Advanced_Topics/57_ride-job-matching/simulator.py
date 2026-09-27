"""Runs matching over simulated requests."""
import random

from models import MatchResult, Request, Resource


def random_requests(n: int, *, bounds: float = 10.0, skills: tuple[str, ...] = (), seed: int | None = None) -> list[Request]:
    rng = random.Random(seed)
    return [Request(f"r{i}", (rng.uniform(0, bounds), rng.uniform(0, bounds)),
                    rng.choice(skills) if skills else None, float(i)) for i in range(n)]


def random_resources(n: int, *, bounds: float = 10.0, skills: tuple[str, ...] = (), seed: int | None = None) -> list[Resource]:
    rng = random.Random(seed)
    return [Resource(f"d{i}", (rng.uniform(0, bounds), rng.uniform(0, bounds)), True,
                     frozenset(rng.sample(skills, rng.randint(1, len(skills)))) if skills else frozenset())
            for i in range(n)]


class Simulator:
    def __init__(self, resources: list[Resource]):
        self.resources = {r.id: r for r in resources}

    def step(self, new_requests: list[Request]) -> MatchResult:
        """Match a batch of new requests against currently available resources."""
        raise NotImplementedError

    def set_unavailable(self, resource_id: str) -> None:
        """Take a resource out mid-simulation (re-matching policy is yours)."""
        raise NotImplementedError


if __name__ == "__main__":
    rs = random_requests(5, skills=("a", "b"), seed=1)
    ds = random_resources(3, skills=("a", "b"), seed=1)
    assert len(rs) == 5 and all(r.required_skill in ("a", "b") for r in rs)
    assert all(d.skills and d.skills <= {"a", "b"} for d in ds)
    assert random_requests(3, seed=9) == random_requests(3, seed=9)
    print("simulator plumbing ok")
