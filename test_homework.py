import pytest
from homework import add

def test_add_positive_integers():
    assert add(2, 3) == 5

def test_add_negative_integers():
    assert add(-1, -2) == -3

def test_add_mixed_integers():
    assert add(4, -3) == 1

def test_add_floating_point_numbers():
    assert abs(add(0.5, 0.7) - 1.2) < 1e-9

def test_add_zero_values():
    assert add(0, 0) == 0

def test_add_large_numbers():
    large_number = 9999999999999999999999
    assert add(large_number, large_number) == 2 * large_number

def test_add_non_numeric_inputs():
    with pytest.raises(TypeError):
        add('a', 'b')