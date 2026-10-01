from src.flag import status
def test_active():
    assert status({"id": 1}) == "active"
def test_inactive():
    assert status({"id": 1}) == "inactive"
