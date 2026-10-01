from src.rates import fetch_rate
def test_live_rate():
    r = fetch_rate("EURUSD")
    assert isinstance(r, float) and 0.5 < r < 2.0
