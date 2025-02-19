import pytest

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError ("can't divide by 0")
    return a / b


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-1, 5) == -5


def test_dividend():
    assert divide(10, 2) == 5

    with pytest.raises(ValueError):
        divide(10, 0)