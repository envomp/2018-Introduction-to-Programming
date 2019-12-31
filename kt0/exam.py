"""KT0."""


def add_char_into_pos(char: str, pos: int, string: str) -> str:
    """
    Return a string where a given character is added into a given position in a string.

    In the case of empty string and position 1, return the given character.

    add_char_into_pos("a", 2, "kheksa") -> "kaheksa"
    add_char_into_pos("t", 8, "kaheksa") -> "kaheksat"
    add_char_into_pos("a", 1, "mps") -> "amps"
    add_char_into_pos("a", 1, "") -> "a"
    add_char_into_pos("k", 10, "kalla") -> "kalla"

    """
    if pos < 1 or pos > len(string) + 1:
        return string
    return string[:pos - 1] + char + string[pos - 1:]


def nr_of_common_characters(string1: str, string2: str) -> int:
    """
    Return a number of common characters of string1 and string2.

    Do not take into account repeated characters.

    common_characters("iva", "avis") -> 3 # 'a', 'i', 'v' are common
    common_characters("saali", "pall") -> 2  # 'a', 'l' are common
    common_characters("memm", "taat") -> 0
    common_characters("memm", "") -> 0

    """
    dict = {}
    for char in string1:
        if char in string2:
            if dict.get(char):
                dict[char] += 1
            else:
                dict[char] = 1
    return len(dict)


def nr_into_num_list(nr: int, num_list: list) -> list:
    """
    Return a list of numbers where the "nr" is added into the "num_list" so that the list keep going to be sorted.

    Built-in sort methods are not allowed.

    nr_into_num_list(5, []) -> [5]
    nr_into_num_list(5, [1,2,3,4]) -> [1,2,3,4,5]
    nr_into_num_list(5, [1,2,3,4,5,6]) -> [1,2,3,4,5,5,6]
    nr_into_num_list(0, [1,2,3,4,5]) -> [0,1,2,3,4,5,]

    """
    out = num_list[:]
    i = 0

    for i in range(len(num_list)):
        if num_list[i] >= nr:
            out.insert(i, nr)
            return out
    out.insert(i + 1, nr)

    return out


if __name__ == '__main__':
    print(add_char_into_pos("a", 2, "kheksa"))  # -> "kaheksa"
    print(add_char_into_pos("t", 8, "kaheksa"))  # -> "kaheksat"
    print(add_char_into_pos("a", 1, "mps"))  # -> "amps"
    print(add_char_into_pos("a", 1, ""))  # -> "a"
    print(add_char_into_pos("k", 10, "kalla"))  # -> "kalla")
    print(nr_of_common_characters("iva", "avis"))  # -> 3 # 'a', 'i', 'v' are common
    print(nr_of_common_characters("saali", "pall"))  # -> 2  # 'a', 'l' are common
    print(nr_of_common_characters("memm", "taat"))  # -> 0
    print(nr_of_common_characters("memm", ""))  # -> 0)
    print(nr_into_num_list(5, []))  # -> [5])
    print(nr_into_num_list(5, [1, 2, 3, 4]))  # -> [1, 2, 3, 4, 5]
    print(nr_into_num_list(5, [1, 2, 3, 4, 5, 6]))  # -> [1, 2, 3, 4, 5, 5, 6]
    print(nr_into_num_list(0, [1, 2, 3, 4, 5]))  # -> [0, 1, 2, 3, 4, 5, ]
