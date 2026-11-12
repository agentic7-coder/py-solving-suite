"""Root and power operations"""

def square_root(x):
    """Return the square root of x"""
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return x ** 0.5

def cubic_root(x):
    """Return the cube root of x"""
    if x >= 0:
        return x ** (1/3)
    else:
        return -(-x) ** (1/3)

def power_root(x, n):
    """Return the nth root of x"""
    if n == 0:
        raise ValueError("Root degree cannot be zero")
    if x < 0 and n % 2 == 0:
        raise ValueError("Cannot compute even root of negative number")
    if x >= 0:
        return x ** (1/n)
    else:
        return -(-x) ** (1/n)
