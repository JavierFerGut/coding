import pytest

from returns import calculate_return


def test_return_of_a_ten_percent_rise():
    assert calculate_return(110, 100) == 0.10


def test_return_of_a_fall():
    assert calculate_return(90, 100) == pytest.approx(-0.10)


def test_return_is_zero_without_previous_value():
    assert calculate_return(100, 0) == 0.0