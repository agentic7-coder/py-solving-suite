"""Utility functions"""

def validate_positive_number(value, name="value"):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value < 0:
        raise ValueError(f"{name} must be non-negative")
    return float(value)
