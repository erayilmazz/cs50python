from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity > 0


def test_str():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪"



def test_deposit():
    jar = Jar()
    capacity = jar.capacity
    jar.deposit(capacity)
    assert str(jar) == "🍪" * capacity
    with pytest.raises(ValueError):
        assert jar.deposit(1)




def test_withdraw():
    jar = Jar()
    capacity = jar.capacity
    jar.deposit(capacity)
    assert jar.size == capacity
    jar.withdraw(capacity)
    assert jar.size == 0
    assert str(jar) == ""
    with pytest.raises(ValueError):
        assert jar.withdraw(1)

