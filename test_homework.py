from homework import add

def test_add():
    assert add(2, 3) == 5, "Test Case for positive integers failed"
    assert add(-1, -1) == -2, "Test Case for negative integers failed"
    assert add(0, 0) == 0, "Test Case for zeros failed"
    assert add(10.5, 5.5) == 16.0, "Test Case for floating point numbers failed"