import pytest
from adding_numbers_again import *


@pytest.mark.timeout(1.0)
def test_first_number_exists():
    try:
        first_number
    except:
        assert False


@pytest.mark.timeout(1.0)
def test_second_number_exists():
    try:
        second_number
    except:
        assert False


@pytest.mark.timeout(1.0)
def test_sum_of_numbers_exists():
    try:
        sum_of_numbers
    except:
        assert False


@pytest.mark.timeout(1.0)
def test_first_number_type():
    assert isinstance(first_number, int)


@pytest.mark.timeout(1.0)
def test_second_number_type():
    assert isinstance(second_number, int)


@pytest.mark.timeout(1.0)
def test_sum_of_numbers_type():
    assert isinstance(sum_of_numbers, int)


@pytest.mark.timeout(1.0)
def test_first_number_value():
    assert first_number == 64

@pytest.mark.timeout(1.0)
def test_second_number_value():
    assert second_number == 92

@pytest.mark.timeout(1.0)
def test_sum_of_numbers_value():
    assert sum_of_numbers == 156
