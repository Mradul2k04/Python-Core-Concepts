import pytest 

from check_exception import devide


def test_divide_by_zero():
    with pytest.raises(ValueError):
        devide(10,0)