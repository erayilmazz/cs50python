from fuel import convert, gauge
import pytest

def test_int():
    with pytest.raises(ValueError):
        convert("four/five")
    with pytest.raises(ValueError):
        convert("23/fifty")
    with pytest.raises(ValueError):
        convert("four/43")
    with pytest.raises(ValueError):
        convert("full")
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_convert():
    assert convert("45/100") == 45
    assert convert("0/5") == 0
    assert convert("5/5") == 100


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"




