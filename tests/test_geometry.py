import math
from py_solving_suite.geometry import circle_area, pythagorean_theorem

def test_circle_area():
    assert circle_area(1) == pytest.approx(math.pi)

def test_pythagorean():
    assert pythagorean_theorem(3, 4) == 5.0
