def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return a + b

# Test with positive integers
assert add(2, 3) == 5

# Test with negative integers
assert add(-1, -2) == -3

# Test with a mix of positive and negative integers
assert add(4, -3) == 1

# Test with floating-point numbers
assert abs(add(0.5, 0.7) - 1.2) < 1e-9

# Test with zero values
assert add(0, 0) == 0

# Test with large numbers (Python arbitrary precision)
large_number = 9999999999999999999999
assert add(large_number, large_number) == 2 * large_number

# Test with non-numeric inputs
try:
    assert(add('a', 'b')) is not False  # This should raise an error
except TypeError as e:
    print("Caught expected error:", e)

print("All tests passed!")