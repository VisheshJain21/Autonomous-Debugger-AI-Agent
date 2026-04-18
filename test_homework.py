import pytest

def add(a, b):
    if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("Both inputs must be either integers or floats.")
    return a + b

# Testing Plan:
def test_add_integers():
    assert add(3, 5) == 8

def test_add_floats():
    assert add(2.5, 4.75) == 7.25

def test_add_mixed_types():
    assert add(5, 10.5) == 15.5

def test_add_non_numeric_int_string():
    with pytest.raises(TypeError) as excinfo:
        add('3', 5)
    assert str(excinfo.value) == "Both inputs must be either integers or floats."

def test_add_non_numeric_float_list():
    with pytest.raises(TypeError) as excinfo:
        add(2.5, [4, 7])
    assert str(excinfo.value) == "Both inputs must be either integers or floats."