def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    
    Args:
        a (int/float): The first number to add.
        b (int/float): The second number to add.
        
    Returns:
        int/float: The sum of the two numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers (integers or floats).")
    
    return a + b