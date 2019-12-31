"""Test filter.py functions."""
# import pytest
import filter
import string
import random

vowels = "aeiouAEIOU"
allowed_chars = "bcdfghjklmnpqrstvxyzBCDFGHJKLMNPQRSTVXYZ"
all_chars = string.ascii_letters
all_punct = string.punctuation


def test_remove_vowels_when_no_vowels():
    """
    String without any vowels.

    :return:
    """
    test_string = ''.join(random.choice(allowed_chars) for _ in range(random.randrange(10, 40)))
    assert filter.remove_vowels(test_string) == test_string


def test_remove_vowels_one_vowel():
    """
    String with one wovel.

    :return:
    """
    for vowel in vowels:
        assert filter.remove_vowels(vowel) == ''


def test_remove_vowels_simple():
    """
    Simple test.

    :return:
    """
    string = ''.join(random.choice(allowed_chars) for _ in range(random.randrange(10, 40)))
    test_string = add_random_vowels(string, random.randrange(10, 40))
    assert filter.remove_vowels(test_string) == string


def test_remove_vowels_only_vowels_return_empty():
    """
    String contains only vowels.

    :return:
    """
    test_string = ''.join(random.choice(vowels) for x in range(random.randrange(10, 40)))
    assert filter.remove_vowels(test_string) == ""


def test_remove_vowels_empty_string():
    """
    String is empty.

    :return:
    """
    assert filter.remove_vowels("") == ""


def test_remove_vowels_removes_wrong_ascii_letters():
    """
    Wrong ascii letters.

    :return:
    """
    assert filter.remove_vowels(string.ascii_lowercase) == "bcdfghjklmnpqrstvwxyz"


def test_remove_vowels_uppercase():
    """
    Uppercase string.

    :return:
    """
    string = ''.join(random.choice(allowed_chars) for _ in range(random.randrange(10, 40))).upper()
    test_string = add_random_vowels(string, random.randrange(10, 40)).upper()
    assert filter.remove_vowels(test_string) == string


def test_remove_vowels_mixed_letters():
    """
    Mixed letter with puncts.

    :return:
    """
    pass


def test_longest_filtered_word():
    """
    Longest filtered word.

    :return:
    """
    list = []
    test_list = []
    for i in range(random.randrange(1, 10)):
        string = ''.join(random.choice(allowed_chars) for _ in range(random.randrange(10, 40)))
        list.append(string)
        test_list.append(add_random_vowels(string, random.randrange(10, 40)))

    assert filter.longest_filtered_word(test_list) == max(list, key=len)


def test_longest_filtered_word_first_in_order():
    """
    Longest word is first.

    :return:
    """
    list = []
    test_list = []
    for i in range(random.randrange(1, 10)):
        string = ''.join(random.choice(allowed_chars) for x in range(random.randrange(10, 40)))
        list.append(string)

    list.sort(key=len, reverse=True)
    for string in list:
        test_list.append(add_random_vowels(string, random.randrange(10, 40)))

    assert filter.longest_filtered_word(test_list) == max(list, key=len)


def test_longest_filtered_word_one_empty_string():
    """
    Given list contains only empty string.

    :return:
    """
    assert filter.longest_filtered_word([""]) == ""


def test_longest_filtered_word_empty_list():
    """
    Given list is empty.

    :return:
    """
    assert filter.longest_filtered_word([]) is None


def test_longest_filtered_word_important_order():
    """
    Order is important.

    :return:
    """
    list = []
    test_list = []
    for i in range(random.randrange(5, 10)):
        string = ''.join(random.choice(allowed_chars) for x in range(10 - i // 2))
        list.append(string)

    list.sort(key=len)

    for string in list:
        test_list.append(add_random_vowels(string, random.randrange(10, 40)))

    assert filter.longest_filtered_word(test_list) == list[-2]


def test_longest_filtered_word_same_length_leftmost():
    """
    Same length leftmost.

    :return:
    """
    list = []
    test_list = []
    for i in range(random.randrange(5, 10)):
        string = ''.join(random.choice(allowed_chars) for x in range(10 - i // 2))
        list.append(string)

    for string in list:
        test_list.append(add_random_vowels(string, random.randrange(10, 40)))

    assert filter.longest_filtered_word(test_list) == list[0]


def test_sort_list_empty_list():
    """
    List is empty.

    :return:
    """
    assert filter.sort_list([]) == []


def test_sort_list_list_len_1():
    """
    List len 1.

    :return:
    """
    list = []
    test_list = []

    string = ''.join(random.choice(allowed_chars) for x in range(10, 40))
    list.append(string)

    for string in list:
        test_list.append(add_random_vowels(string, random.randrange(10, 40)))

    assert filter.sort_list(test_list) == list


def test_sort_list_should_not_change_input_list():
    """
    Not change imput.

    :return:
    """
    list = []

    for i in range(random.randrange(1, 10)):
        string = ''.join(random.choice(allowed_chars) for _ in range(random.randrange(10, 40)))
        list.append(string)

    assert filter.sort_list(list) != list


def test_sort_list_correct_order_with_same_length():
    """
    List elements with same length should keep order.

    :return:
    """
    list = []
    test_list = []

    for i in range(random.randrange(5, 10)):
        string = ''.join(random.choice(allowed_chars) for _ in range(10))
        list.append(string)

    for string in list:
        test_list.append(add_random_vowels(string, random.randrange(10, 40)))

    assert filter.sort_list(test_list) == list


def add_random_vowels(input_str: str, count: int) -> str:
    """
    Add vowels to string in random positions.

    :param input_str: string
    :param count: vowels count
    :return: string with added vowels
    """
    str = input_str[:]
    for i in range(count):
        pos = random.randrange(0, len(str))
        char = random.choice(vowels)
        str = str[:pos] + char + str[pos:]
    return str
