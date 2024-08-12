from twttr import shorten
def test_examples():
    assert shorten("twitter") == "twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("Hello, World") == "Hll, Wrld"
def test_uppercase():
    assert shorten ("AEOUI") == ""
def test_lowercase():
    assert shorten ("aeoui") == ""
