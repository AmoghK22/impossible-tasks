from src.chunk import chunks
def test_even():
    assert chunks([1,2,3,4], 2) == [[1,2],[3,4]]
def test_remainder():
    assert chunks([1,2,3,4,5], 2) == [[1,2],[3,4],[5]]
