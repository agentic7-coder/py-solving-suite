import pytest
from py_solving_suite.utils import validate_positive_number

def test_validate():
    assert validate_positive_number(5) == 5.0
    with pytest.raises(ValueError):
        validate_positive_number(-5)
