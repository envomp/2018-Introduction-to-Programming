"""Test 6 (R12)."""


def rotate_left3(nums):
    """
    Given an array of ints length 3, return an array with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].

    rotate_left3([1, 2, 3]) → [2, 3, 1]
    rotate_left3([5, 11, 9]) → [11, 9, 5]
    rotate_left3([7, 0, 0]) → [0, 0, 7]

    :param nums: List of integers of length 3.
    :return: Rotated list.
    """
    return nums[1:] + nums[0:1]


def love6(a: int, b: int) -> bool:
    """
    Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6.

    love6(6, 1) → True
    love6(3, 3) → True
    love6(2, 3) → False
    """
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6


def middle_chars(s: str) -> str:
    """Return two chars in the middle of string.

    The length of the string is an even number.

    middle_chars("abcd") => "bc"
    middle_chars("bc") => "bc"
    middle_chars("aabbcc") => "bb"
    middle_chars("") => ""
    """
    return "" if not len(s) else s[(len(s) // 2) - 1] + s[len(s) // 2]


def remove_nth_symbol(s, n):
    """
    Return a new string where n-th symbol is removed.

    If the n is outside of the string, return original string.
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


def remove_in_middle(text, to_remove):
    """
    Remove substring from the text, except for the first and the last occurrence.

    remove_in_middle("abc", "def") => "abc"
    remove_in_middle("abcabcabc", "abc") => "abcabc"
    remove_in_middle("abcdabceabcabc", "abc") => "abcdeabc"
    remove_in_middle("abcd", "abc") => "abcd"
    remove_in_middle("abcdabc", "abc") => "abcdabc"
    remove_in_middle("ABCAaaaAA", "a") => "ABCAaaAA

    :param text: string from where the remove takes place.
    :param to_remove: substring to be removed.
    :return: string with middle substrings removed.
    """
    if text.find(to_remove) == -1 or text.find(to_remove) == text.rfind(to_remove):
        return text
    if text.find(to_remove) + len(to_remove) > text.rfind(to_remove):
        return text

    begin = text.find(to_remove) + len(to_remove)
    end = text.rfind(to_remove)

    middle = text[begin:end].replace(to_remove, '')
    return text[:begin] + middle + text[end:]


if __name__ == '__main__':
    # print(rotate_left3([1, 2, 3]))
    # print(love6(6, 1))
    # print(middle_chars(""))
    # print(remove_nth_symbol("tere", 4))
    print(remove_in_middle("aaaaaaaaa", "aaa"))
