import pytest
from py_solving_suite.roots import square_root, cubic_root, power_root

def test_square_root():
    assert square_root(9) == 3.0
    with pytest.raises(ValueError):
        square_root(-4)

def test_cubic_root():
    assert cubic_root(27) == 3.0
    assert cubic_root(-8) == -2.0
