from numb3rs import validate

def test_validate():
    assert validate("cat") == False
    assert validate("1.2.3.4") == True
    assert validate("275.3.6.28") == False
    assert validate("27.cat.6.28") == False
    assert validate("27.277.6.28") == False
