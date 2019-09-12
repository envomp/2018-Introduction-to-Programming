"""Primes identifier."""
from math import sqrt
from itertools import count, islice


def is_prime_number(n: int) -> bool:
    """
    Check if number (given in function parameter) is prime.

    If number is prime -> return True
    If number is not prime -> return False

    :param number: number for check.
    :return: boolean True if number is prime or False if number is not prime.
    """

    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True


if __name__ == '__main__':
    for x in range(5, 1, -1):
        print(x)
