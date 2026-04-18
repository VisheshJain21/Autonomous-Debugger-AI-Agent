import pytest

# Import 'add' from 'homework'
from homework import add

def test_add_with_integers():
    assert add(1, 2) == 3

def test_add_with_negative_numbers():
    assert add(-1, -2) == -3

def test_add_with_mixed_numbers():
    assert add(-1, 2) == 1

def test_add_with_zeroes():
    assert add(0, 0) == 0

def test_add_with_large_numbers():
    assert add(1000, 1500) == 2500

def test_add_with_non_integers():
    with pytest.raises(TypeError):
        add('a', 'b')