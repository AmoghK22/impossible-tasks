from src.legacy.parser import parse_record
def test_parse():
    assert parse_record("id=7;name=ana") == {"id": 7, "name": "ana"}
