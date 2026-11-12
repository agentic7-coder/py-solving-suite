"""Geometry functions: areas, volumes, and Pythagorean theorem"""

import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

def pythagorean_theorem(a, b):
    return math.sqrt(a**2 + b**2)
