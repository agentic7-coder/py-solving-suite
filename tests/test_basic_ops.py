import pytest
from py_solving_suite.basic_ops import add, subtract, divide, square, cube

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)

def test_square():
    assert square(4) == 16
    assert square(-3) == 9
