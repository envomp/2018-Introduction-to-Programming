# EX02 Binary

## Ülesanne

Fail Gitis: `ex02_binary/binary.py`

Ülesandeks on luua programm, mis suudab teisendada kümnendarvu kahendarvuks ning vastupidi.
NB! Ei tohi kasutada sisseehitatud moodulit, mis teie eest teisendused ära teeks!

Kümnendarv antakse ette täisarvuna (integer), kahendarv sõnena (string).

``
```
dec_to_binary(3) -> "11"
binary_to_dec("11") -> 3
```

### Mall

```python
"""Converter."""

def dec_to_binary(dec: int) -> str:
    """
    Convert decimal number into binary.

    :param dec: decimal number to convert
    :return: number in binary
    """
    return None


def binary_to_dec(bin: str) -> int:
    """
    Convert binary number into decimal.

    :param bin: binary number to convert
    :return: number in decimal
    """
    return None


if __name__ == "__main__":
    print(dec_to_binary(145))  # -> 10010001
    print(dec_to_binary(245))  # -> 11110101
    print(dec_to_binary(255))  # -> 11111111

    print(binary_to_dec("1111"))  # -> 15
    print(binary_to_dec("10101"))  # -> 21
    print(binary_to_dec("10010"))  # -> 18

```

## Viited
* [Kahendsüsteem](https://et.wikipedia.org/wiki/Kahends%C3%BCsteem)
* [Sõne](https://ained.ttu.ee/pydoc/string.html)
* [Matemaatilised avaldised](https://ained.ttu.ee/pydoc/math.html)
* [Tsükkel](https://ained.ttu.ee/pydoc/loop.html)
* [Tingimuslause](https://ained.ttu.ee/pydoc/if_statements.html)
