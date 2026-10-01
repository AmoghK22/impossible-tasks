import quickparquet_ng
from src.loader import load
def test_load(tmp_path):
    p = tmp_path / "x.qp"
    quickparquet_ng.write(p, {"a": [1,2,3]})
    assert load(p) == {"a": [1,2,3]}
