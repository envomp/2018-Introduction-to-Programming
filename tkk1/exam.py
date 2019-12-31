"""TKK 1 (L14)."""


def sum_odds_or_evens(a, b):
    """
    Given two numbers, return the sum of these numbers if they both are even or odd numbers, otherwise return None.

    Consider that zero is also even number.

    sum_odds_or_evens(2, 19) → None
    sum_odds_or_evens(17, 31) → 48
    sum_odds_or_evens(99, 100) → None

    :param a: an integer.
    :param b: an integer.
    :return: The sum of a and b if they are both even or odd numbers, otherwise None.
    """
    return a + b if a % 2 == b % 2 else None


def first_and_last_item(num_list):
    """
    Given an list of numbers (ints), return a new list with length 2 containing the first and last elements from the initial list.

    The initial list will be length 2 or more.

    first_and_last_item([9, 1, 5, 2, 7]) → [9, 7]
    first_and_last_item([1, 2, 3, 4]) → [1, 4]
    first_and_last_item([91, 4, 6, 52]) → [91, 52]

    :param nums: List of integers.
    :return: List with the first and the last element from the input list.
    """
    out = []
    out.append(num_list[0])
    out.append(num_list[-1])
    return out


def exchange_first_and_last(word):
    """
    Given a word as a string, return a string where first and last character are exchanged if last character is smaller than first one, otherwise return initial word.

    Also, if the length of input word is smaller than two return the initial word.

    exchange_first_and_last('kala') → 'aalk'
    exchange_first_and_last('kalalaev') → 'kalalaev'
    exchange_first_and_last('r') → 'r'
    exchange_first_and_last('') → ''

    :param word: input string.
    :return: a string
    """
    if len(word) < 2:
        return word
    return word[-1] + word[1:-1] + word[0] if ord(word[-1]) < ord(word[0]) else word


def remove_nth_symbol(s, n):
    """
    Return a new string where n-th symbol is removed.

    If the n is outside of the string's length, return original string.
    If n is 1, the first symbol is removed etc.

    remove_nth_symbol("tere", 1) => "ere"
    remove_nth_symbol("tere", 3) => "tee"
    remove_nth_symbol("tere", 5) => "tere"

    :param s: Input string.
    :param n: Which element to remove.
    :return: String where n-th symbol is removed.
    """
    if n <= 0 or n > len(s):
        return s
    return s[:n - 1] + s[n:]


def repeated_word_numeration(words):
    """
    For a given list of words, add numeration for every repeated word.

    The input list consists of words. For every repeated element in the input list,
    the output list adds a numeration after the words.
    The format is as follows: #N, where N starts from 1.
    Word comparison should be case-insensitive.
    The case of symbols in a word itself in output list should remain the same as in input list.

    The output list has the same amount of elements as the input list.
    For every repeated element in the output list, "#N" is added, where N = 1, 2, 3, ...

    word_numeration(["tere", "tere", "tulemast"]) => ["tere#1", "tere#2", "tulemast"]
    word_numeration(["Tere", "tere", "tulemast"]) => ["Tere#1", "tere#2", "tulemast"]
    word_numeration(["Tere", "tere", "tulemast", "no", "tere", "TERE"]) => ["Tere#1", "tere#2", "tulemast", "no", "tere#3", "TERE#4"]

    :param words: A list of strings.
    :return: List of words where repeated words have numeration.
    """
    temp = []
    out = []

    lowered = [word.lower() for word in words]

    for i in words:
        temp.append(i.lower())
        order = temp.count(i.lower())
        is_multiple = lowered.count(i.lower())

        if is_multiple == 1:
            out.append(i)
        else:
            out.append(i + "#" + str(order))

    return out


if __name__ == '__main__':
    print(sum_odds_or_evens(3, 1))
    print(first_and_last_item([5, 2, 7]))
    print(exchange_first_and_last('vaal'))
    print(remove_nth_symbol('sadam', 3))
    print(repeated_word_numeration(["tere", "tere", "tulemast"]))  # = > ["tere#1", "tere#2", "tulemast"]
    print(repeated_word_numeration(["Tere", "tere", "tulemast"]))  # = > ["Tere#1", "tere#2", "tulemast"]
