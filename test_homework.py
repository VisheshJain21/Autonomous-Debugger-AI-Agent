import pytest
from homework import add

def test_add_positive_numbers():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0

def test_add_mixed_numbers():
    assert add(-1, 5) == 4
    assert add(5, -1) == 4

def test_add_float_numbers():
    assert add(1.5, 2.5) == 4.0
    assert add(-1.5, 2.0) == 0.5

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_add_strings():
    with pytest.raises(TypeError):
        add("hello", "world")

def test_add_list_and_int():
    with pytest.raises(TypeError):
        add([1, 2], 3)

def test_add_none_and_int():
    with pytest.raises(TypeError):
        add(None, 5)

def test_add_int_and_none():
    with pytest.raises(TypeError):
        add(5, None)