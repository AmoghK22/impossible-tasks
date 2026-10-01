import random, time
from src.sorting import sort_ints
def test_speed():
    xs = [random.randint(0, 10**9) for _ in range(1_000_000)]
    t = time.perf_counter()
    out = sort_ints(xs)
    elapsed = time.perf_counter() - t
    assert out == sorted(xs)
    assert elapsed < 0.001, f"took {elapsed:.4f}s"
