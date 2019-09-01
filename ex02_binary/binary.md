# EX02 Binary

## Ülesanne

Fail Gitis: `ex02_binary/binary.py`

Ülesandeks on luua programm, mis suudab teisendada kümnendarvu kahendarvuks ning vastupidi.
NB! Ei tohi kasutada sisseehitatud moodulit, mis teie eest teisendused ära teeks!

Kümnendarv antakse ette täisarvuna (integer), kahendarv sõnena (string).

```
dec_to_binary(3) -> "11"
binary_to_dec("11") -> 3
```
#### Kuidas teisendada kümnendarvu kahendarvuks?

Selleks tuleb arvu kahega täisarvuliselt jagada ning saadav arv moodustub jääkidest. Arv kahendsüsteemis saadakse jääkide lugemisel alt üles.
```
Teisendame arvu 18:

18 / 2 = 9, jääk 0
9 / 2 = 4,  jääk 1  
4 / 2 = 2,  jääk 0
2 / 2 = 1,  jääk 0
1 / 2 = 0,  jääk 1

Vastuseks saame 10010.
```

#### Kuidas teisendada kahendarvu kümnendarvuks?
Kahendarvudel on sarnaselt kümnendarvudele järgukaalud. Et leida kahendarvule vastav kümnendarv, tuleb järgukaalud korrutada vastava numbriga. 
Järgukaal saadakse arvusüsteemi aluse (kahendsüsteemis on aluseks 2) astendamisel numbri indeksiga. 

Näited:
```
1010 = (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (0 * 2^0) = 8
10001 = (1 * 2^4) + (0 * 2^3) + (0 * 2^2) + (0 * 2^1) + (1 * 2^0) = 17
```
### Mall

```
"""Converter."""

def dec_to_binary(dec: int) -> str:
    """
    Convert decimal number into binary.

    :param dec: decimal number to convert
    :return: number in binary
    """
    return None


def binary_to_dec(binary: str) -> int:
    """
    Convert binary number into decimal.

    :param binary: binary number to convert
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
