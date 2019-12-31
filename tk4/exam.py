"""Test 4 (K14)."""


def string_edges(first: str, second: str) -> str:
    """
    Given two strings return a string which consists of the last elements of input strings.

    The strings will have length 1 or more.

    string_edges("abc", "def") => "cf"
    string_edges("a", "b") => "ab"
    """
    return first[-1] + second[-1]


def near_ten(nr):
    """
    Given a non-negative number "num", return True if num is within 2 of a multiple of 10.

    near_ten(0) →  True
    near_ten(3) →  False
    near_ten(10) →  True
    near_ten(23) →  False
    near_ten(198) →  True

    :param nr: non-negative integer.
    :return: True if num is within 2 of a multiple of 10.
    """
    return True if not nr % 10 else True if nr % 10 <= 2 or nr % 10 >= 8 else False


def non_start(first_string, second_string):
    """
    Given 2 strings, return their concatenation, except omit the first char of each.

    The strings will be at least length 1.

    non_start('Hello', 'There') → 'ellohere'
    non_start('java', 'code') → 'avaode'
    non_start('shotl', 'java') → 'hotlava'

    :param second_string: First string.
    :param first_string: Second string.
    :return: Concatenation of two string without first chars.
    """
    return first_string[1:] + second_string[1:]


def min_diff(nums):
    """
    Calculate min difference.

    Diff is a distance (non-negative number) between a value of an element and a value
    of the element at position of original element value.
    Take diffs for both first and the last element, return the smaller diff.
    If one index is out of range, then return the diff of other element.
    If both indices are out of range, return -1.

    min_diff([1, 2, 3, 4, 5, 3]) => 1
    min_diff([1, 3, 3, 4, 1, 4]) => 2
    min_diff([0, 1, 2, 0]) => 0
    min_diff([1, 100, 102, 2]) => 99

    min_diff([1, 2, 3]) => 1
    min_diff([79, 2, 0]) => 79
    min_diff([123, 0, 122]) => -1

    :param nums: List of integers.
    :return: Min diff
    """
    if nums[0] < len(nums) and nums[-1] < len(nums):
        return min(abs(nums[0] - nums[nums[0]]), abs(nums[-1] - nums[nums[-1]]))
    elif nums[0] >= len(nums) and nums[-1] < len(nums):
        return abs(nums[-1] - nums[nums[-1]])
    elif nums[0] < len(nums) and nums[-1] >= len(nums):
        return abs(nums[0] - nums[nums[0]])
    else:
        return -1


def mirror_ends(s):
    """
    Given a string, look for a mirror image (backwards) string at both the beginning and end of the given string.

    In other words, zero or more characters at the very beginning of the given string,
    and at the very end of the string in reverse order (possibly overlapping).

    For example, the string "abXYZba" has the mirror end "ab".

    mirrorEnds("abXYZba") → "ab"
    mirrorEnds("abca") → "a"
    mirrorEnds("aba") → "aba"

    :param s: String
    :return: Mirror image string
    """
    out = ""
    for i in range(len(s)):
        if s[i] == s[len(s) - 1 - i]:
            out += s[i]
        else:
            return out
    return out


if __name__ == '__main__':
    print(string_edges("abc", "def"))
