PR04 - Filter
===
Fail Gitis: pr04_filter/filter.py

Ülesande eesmärgiks on luua programm, mis filtreerib sõnedest täishäälikud ja sorteerib saadud uue järjendi sõne pikkuse järgi.

Abimaterjalid ülesande lahendamiseks
------------------------------------

- `sõne <https://ained.ttu.ee/pydoc/string.html>`
- `järjend <https://ained.ttu.ee/pydoc/list.html>`
- `tsükkel (loop) <https://ained.ttu.ee/pydoc/loop.html>`
- `tingimuslause <https://ained.ttu.ee/pydoc/if_statements.html>`

Funktsioonid
---

Funktsioonid:

- ``filter_vowels(string)`` - Sisendiks on string ehk sõne. Funktsioon peab tagastama sõne ilma täishäälikuteta. Ülesande lihtsustamiseks jätame täpitähed välja. 
Funktsioon peab arvestama nii suur- kui väiketähtedega. Tagastada tuleb väikesed tähed väikestena ja suured suurtena. ```(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])```

- ``longest_filtered_word(string_list)`` - Saab sisendiks sõnedest koosneva järjendi. Funktsioon peab tagastama sõne, mis on kõige pikem peale täishäälikute välja filtreerimist. 
Kui kahes tekkinud sõnes on sama palju tähti, siis tagastada sõne, mis paikneb järjendis eespool. Selles funktsioonis tuleks ära kasutada funktsiooni ``filter_vowels()``.

- ``sort_list(string_list)`` - Sisendiks on sõnedest koosnev järjend. Funktsioon peab tagastama sama järjendi filtreerides välja täishäälikud ning sorteerides järjendi sõne pikuse järgi. 
Sorteerimiseks on soovitav kasutada ``filter_vowels()``, ``longest_filtered_word()`` või mõlemat funktsiooni. Tühja sisendjärjendi saamisel tagastada tühi järjend.

```
Mall:

"""Filtering."""


def filter_vowels(string: str):
    """
    Filter vowels(a, e, i, o, u).

    :param string:
    :return string without vowels:
    """

    pass


def longest_filtered_word(string_list: list):
    """
    Filter, find and return the longest string.

    :param string_list:
    :return: Longest string without vowels.
    """
    pass



def sort_list(string_list: list):
    """
    Filter vowels in strings and sort the list by the length.

    :param string_list: List of strings that need to be sorted.
    :return: Filtered list of strings sorted by the number of vowels.
    """
    pass
    

if __name__ == '__main__':
    print(filter_vowels(""))  # => ""
    print(filter_vowels("hello"))  # => "hll"
    print(filter_vowels("Home"))  # => "Hm"
    print(longest_filtered_word(["Bunny", "Tiger", "Bear", "Snake"]))  # => "Bnny"
    print(sort_list(["Bunny", "Tiger", "Bear", "Snake"]))  # => ['Bnny', 'Tgr', 'Snk', 'Br']
```
