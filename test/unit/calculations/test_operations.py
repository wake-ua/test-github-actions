import pytest
import calculations.operations


def test_fibonacci():
    result = calculations.operations.fibonacci(7)
    assert result == 13


def test_fibonacci_zero():
    result = calculations.operations.fibonacci(0)
    assert result == 0


def test_fibonacci_negative_input():
    with pytest.raises(ValueError) as error:
        calculations.operations.fibonacci(-1)
    assert str(error.value) == "Input number should be " \
                               "equal or greater than 0."
