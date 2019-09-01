import pytest
from primes import prime_number_identifier
from random import randint


def test_prime_number_identifier(number: int) -> bool:
    if number == 0:
        return False
    if number == 1:
        return False
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
    assert prime_number_identifier(1) == test_prime_number_identifier(1)
    assert prime_number_identifier(2) == test_prime_number_identifier(2)
    assert prime_number_identifier(4) == test_prime_number_identifier(4)
    assert prime_number_identifier(6) == test_prime_number_identifier(6)
    assert prime_number_identifier(7) == test_prime_number_identifier(7)
    assert prime_number_identifier(9) == test_prime_number_identifier(9)


@pytest.mark.timeout(1.0)
def test_big_numbers():
    assert prime_number_identifier(11) == test_prime_number_identifier(11)
    assert prime_number_identifier(23) == test_prime_number_identifier(23)
    assert prime_number_identifier(45) == test_prime_number_identifier(45)
    assert prime_number_identifier(69) == test_prime_number_identifier(69)
    assert prime_number_identifier(78) == test_prime_number_identifier(78)
    assert prime_number_identifier(95) == test_prime_number_identifier(95)


@pytest.mark.timeout(1.0)
def test_random():
    number = randint(2, 1000)
    assert prime_number_identifier(number) == test_prime_number_identifier(number)
