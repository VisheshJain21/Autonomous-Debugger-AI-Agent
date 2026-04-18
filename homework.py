def add(a, b):
    if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("Both inputs must be either integers or floats.")
    return a + b

# Testing Plan:
1. Test the function with two integer arguments to ensure it returns their sum correctly.