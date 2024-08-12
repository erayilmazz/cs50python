from um import count

def test_count():
    assert count("um") == 1
    assert count("yumurta severim") == 0
    assert count("hıı um aaaa!") == 1
    assert count("um, i dont Um") == 2
