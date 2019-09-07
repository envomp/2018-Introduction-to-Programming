import pytest
from primes import prime_number_identifier
from random import randint


def identifier(number: int) -> bool:
    if number == 0:
        return False
    if number == 1:
        return False  # 1 is not prime number
    if number == 2:
        return True

    for divider in range(2, number):
        if number % divider == 0:
            return False

    return True


@pytest.mark.timeout(1.0)
def test_zero():
    assert not prime_number_identifier(0)


@pytest.mark.timeout(1.0)
def test_one():
    assert not prime_number_identifier(1)


@pytest.mark.timeout(1.0)
def test_small_numbers():
    assert prime_number_identifier(3)
    assert prime_number_identifier(2)
    assert not prime_number_identifier(4)
    assert not prime_number_identifier(6)
    assert prime_number_identifier(7)
    assert not prime_number_identifier(9)


@pytest.mark.timeout(1.0)
def test_big_numbers():
    assert prime_number_identifier(6073)
    assert prime_number_identifier(5393)
    assert prime_number_identifier(5557)
    assert prime_number_identifier(5693)
    assert prime_number_identifier(7877)
    assert not prime_number_identifier(7878)


@pytest.mark.timeout(1.0)
def test_random():
    number = randint(2, 1000)
    assert prime_number_identifier(number) == identifier(number)
