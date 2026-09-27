"""Generates the event feed for testing."""
import random


def generate_events(n: int, *, seed: int | None = None, start: float = 0.0, max_gap: float = 1.0,
                    value_range: tuple[int, int] = (0, 100)) -> list[tuple[float, int]]:
    """n (timestamp, value) events with increasing timestamps and random int values."""
    rng = random.Random(seed)
    t, events = start, []
    for _ in range(n):
        t += rng.uniform(0, max_gap)
        events.append((t, rng.randint(*value_range)))
    return events


if __name__ == "__main__":
    ev = generate_events(50, seed=1, value_range=(0, 3))
    assert len(ev) == 50 and all(a[0] <= b[0] for a, b in zip(ev, ev[1:]))
    assert generate_events(5, seed=7) == generate_events(5, seed=7)
    print("stream_simulator ok")
