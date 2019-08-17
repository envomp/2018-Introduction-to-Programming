# PR02 Primes

## Ülesanne

Fail Gitis: `pr2_primes/primes.py`

Ülesandeks on kirjutada programm, mis suudab tuvastada, kas antud arv on algarv.
Tuvastamisele minev arv on antud funktsiooni parameetrina.

Kui tegemist on algarvuga, tagastab funktsioon True.

`prime_number_identifier(7) -> True`

Kui tegemist pole algarvuga, tagastab funktsioon False.

`prime_number_identifier(6) -> False`


### Mall

```
"""Primes identifier."""

def prime_number_identifier(number: int) -> bool:
    """
    Check if number (given in function parameter) is prime.
    If number is prime -> return True
    If number is not prime -> return False
    
    :param number: number for check.
    :return: boolean True if number is prime or False if number is not prime.
    """
    
    return None
    
if __name__ == '__main__':
    print(prime_number_identifier(2))  # -> True
    print(prime_number_identifier(89))  # -> True
    print(prime_number_identifier(23))  # -> True
    print(prime_number_identifier(4))  # -> False
    print(prime_number_identifier(7))  # -> True
    print(prime_number_identifier(88))  # -> False

```

## Viited

* [Matemaatilised avaldised](https://ained.ttu.ee/pydoc/math.html)
* [Tsükkel](https://ained.ttu.ee/pydoc/loop.html)
* [Algarv](https://en.wikipedia.org/wiki/Prime_number)
* [Tingimuslause](https://ained.ttu.ee/pydoc/if_statements.html)

