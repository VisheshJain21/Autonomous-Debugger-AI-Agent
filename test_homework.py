import pytest
from homework import add_numbers

def test_add_numbers_positive_ints():
    assert add_numbers(2, 3) == 5

def test_add_numbers_negative_ints():
    assert add_numbers(-1, -3) == -4

def test_add_numbers_mixed_int_float():
    assert add_numbers(2.5, 3) == 5.5

def test_add_numbers_negative_int_float():
    assert add_numbers(-1.5, -3) == -4.5

def test_add_numbers_zero():
    assert add_numbers(0, 0) == 0

def test_add_numbers_non_numeric_value():
    with pytest.raises(ValueError):
        add_numbers("a", "b")

def test_add_numbers_one_string_one_int():
    with pytest.raises(ValueError):
        add_numbers("a", 2)

def test_add_numbers_one_string_one_float():
    with pytest.raises(ValueError):
        add_numbers("3.5", 2)