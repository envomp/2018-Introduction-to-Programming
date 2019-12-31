"""Filtering."""


def remove_vowels(string: str) -> str:
    """
    Remove vowels (a, e, i, o, u).

    :param string: Input string
    :return string without vowels.
    """
    vowels = "aeiou"

    string_wo_vowels = [char for char in string if char.lower() not in vowels]

    return ''.join(string_wo_vowels)


def longest_filtered_word(string_list: list) -> str:
    """
    Filter, find and return the longest string.

    :param string_list: List of strings.
    :return: Longest string without vowels.
    """
    if not len(string_list):
        return None

    longest_word = remove_vowels(string_list[0])

    for i in range(1, len(string_list)):
        if len(remove_vowels(string_list[i])) > len(longest_word):
            longest_word = remove_vowels(string_list[i])

    return longest_word


def sort_list(string_list: list) -> list:
    """
    Filter vowels in strings and sort the list by the length.

    :param string_list: List of strings that need to be sorted.
    :return: Filtered list of strings sorted by the number of symbols in descending order..
    """
    if not len(string_list):
        return []

    for i in range(0, len(string_list)):
        string_list[i] = remove_vowels(string_list[i])

    # Method 1
    sorted_list = []

    for i in range(0, len(string_list)):
        longest_word = longest_filtered_word(string_list)
        sorted_list.append(longest_word)
        string_list.remove(longest_word)

    return sorted_list

    # Method 2
    """
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(string_list) - 1):
            if len(string_list[i]) < len(string_list[i + 1]):
                string_list[i], string_list[i + 1] = string_list[i + 1], string_list[i]
                swapped = True

    return string_list
    """

    # Method 3 (the easiest)
    # string_list.sort(reverse=True, key=len)
    # or
    # string_list = sorted(string_list, reverse=True, key=len)
    # return string_list


if __name__ == '__main__':
    # print(remove_vowels(""))  # => ""
    # print(remove_vowels("hello"))  # => "hll"
    # print(remove_vowels("Home"))  # => "Hm"
    print(longest_filtered_word(["Bunny", "Tiger", "Bear", "Snake"]))  # => "Bnny"
    print(sort_list(["Bunny", "Tiger", "Bear", "Snake"]))  # => ['Bnny', 'Tgr', 'Snk', 'Br']
