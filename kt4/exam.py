"""KT4 (K14)."""


def two_digits_into_list(nr: int) -> list:
    """
    Return list of digits of 2-digit number.

    two_digits_into_list(11) => [1, 1]
    two_digits_into_list(71) => [7, 1]

    :param nr: 2-digit number
    :return: list of length 2
    """
    out = []

    out.append(nr // 10)
    out.append(nr % 10)

    return out


def only_one_pair(numbers: list) -> bool:
    """
    Whether the list only has one pair.

    Function returns True, if the list only has one pair (two elements have the same value).
    In other cases:
     there are no elements with the same value
     there are more than 2 elements with the same value
     there are several different pairs
    returns False.

    only_one_pair([1, 2, 3]) => False
    only_one_pair([1]) => False
    only_one_pair([1, 2, 3, 1]) => True
    only_one_pair([1, 2, 1, 3, 1]) => False
    """
    if len(numbers) < 2:
        return False

    count = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                count += 1
    return True if count == 1 else False


def min_diff(nums):
    """
    Find the smallest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1
    min_diff([1, 9, 17]) => 8
    min_diff([100, 90]) => 10
    min_diff([1, 100, 1000, 1]) => 0

    :param nums: list of ints, at least 2 elements.
    :return: min diff between 2 numbers.
    """
    diff = abs(nums[0] - nums[1])
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) < diff:
                diff = abs(nums[i] - nums[j])
    return diff


if __name__ == '__main__':
    print(two_digits_into_list(11))  # = > [1, 1]
    print(two_digits_into_list(71))  # = > [7, 1]
    print(only_one_pair([1, 2, 3]))  # => False
    print(only_one_pair([1]))  # => False
    print(only_one_pair([1, 2, 3, 1]))  # => True
    print(only_one_pair([1, 2, 1, 3, 1]))  # => False
    print(min_diff([1, 2, 3]))  # => 1
    print(min_diff([1, 9, 17]))  # => 8
    print(min_diff([100, 90]))  # => 10
    print(min_diff([1, 100, 1000, 1]))  # => 0
