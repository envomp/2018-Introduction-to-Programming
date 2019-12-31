"""Test 5 (R10)."""
import math


def reverse3(nums):
    """
    Given an int list(length 3), return a new list with the order of the elements reversed.

    reverse3([1, 2, 3]) → [3, 2, 1]
    reverse3([7, 7, 7]) → [7, 7, 7]
    reverse3([5, 2, 9]) → [9, 2, 5]
    """
    return nums[::-1]


def is_sum_of_two(a: int, b: int, c: int) -> bool:
    """
    Whether one parameter is a sum of other two.

    is_sum_of_two(3, 2, 1) => True
    is_sum_of_two(3, 1, 1) => False
    is_sum_of_two(3, 2, 5) => True
    """
    return a == b + c or b == a + c or c == a + b


def left2(s):
    """
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.

    The string length will be at least 2.

    left2('Hello') → 'lloHe'
    left2('java') → 'vaja'
    left2('Hi') → 'Hi'
    :param s: input string.
    :return: "rotated" string.
    """
    if len(s) <= 2:
        return s
    return s[2:] + s[:2]


def index_index_value(nums):
    """
    Return value at index.

    Take the last element.
    Use the last element value as the index to get another value.
    Use this another value as the index of yet another value.
    Return this yet another value.

    If the the last element points to out of list, return -1.
    If the element at the index of last element points out of the list, return -2.

    All elements in the list are non-negative.

    index_index_value([0]) => 0
    index_index_value([0, 2, 4, 1]) => 4
    index_index_value([0, 2, 6, 2]) => -2  (6 is too high)
    index_index_value([0, 2, 4, 5]) => -1  (5 is too high)

    :param nums: List of integer
    :return: Value at index of value at index of last element's value
    """
    if nums[-1] >= len(nums):
        return -1
    return -2 if nums[nums[-1]] >= len(nums) else nums[nums[nums[-1]]]


def make_bricks(small, big, goal):
    """
    Return whether we can make a row of bricks.

    We want to make a row of bricks that is goal inches long.
    We have a number of small bricks (1 inch each) and big bricks (5 inches each).
    Return True if it is possible to make the goal by choosing from the given bricks.
    This is a little harder than it looks and can be done without any loops.

    make_bricks(3, 1, 8) → True
    make_bricks(3, 1, 9) → False
    make_bricks(3, 2, 10) → True
    :param small: Number of small bricks.
    :param big: Number of big bricks.
    :param goal: Length of row we want to build.
    :return: Can we build the row?
    """
    big_needed = int(math.ceil((goal - small) / 5))
    small_needed = goal % 5
    return True if big_needed <= big and small_needed <= small else False


if __name__ == '__main__':
    # print(reverse3([1, 2, 3]))
    print(is_sum_of_two(3, 2, 1))  # => True
    print(is_sum_of_two(3, 1, 1))  # => False
    print(is_sum_of_two(3, 2, 5))  # => True
    print(left2('Hello'))  #
    print(index_index_value([0, 2, 4, 1]))
    print(make_bricks(3, 1, 4))
