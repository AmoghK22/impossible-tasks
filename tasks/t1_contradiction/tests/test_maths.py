from src.maths import add
def test_add_small():
    assert add(1, 1) == 2
def test_add_pair():
    assert add(2, 2) == 5
