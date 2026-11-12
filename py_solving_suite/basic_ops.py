"""Basic mathematical operations: add, subtract, divide, square, cube"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def square(x):
    """Return the square of x"""
    return x ** 2

def cube(x):
    """Return the cube of x"""
    return x ** 3
