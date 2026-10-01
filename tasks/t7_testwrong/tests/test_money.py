from src.money import total
def test_total():
    assert total([0.1, 0.2]) == 0.3
