"""KT6 (R12)."""


def duplicate_last(nums: list) -> list:
    """
    Return a list where the last element is doubled.

    In the case of empty list, return empty list.

    duplicate_last([1, 2, 3]) => [1, 2, 3, 3]
    duplicate_last([7]) => [7, 7]
    duplicate_last([]) => []
    """
    if not len(nums):
        return []
    out = nums[:]
    out.append(nums[-1])
    return out


def odd_sums_of_consecutive_elements(nums: list) -> list:
    """
    Return list of odd sums of consecutive elements.

    Consider all consecutive elements in the input list. Return a list of all the odd sums of consecutive elements.

    odd_sums_of_consecutive_elements([1, 2, 3, 5]) => [3, 5]
    odd_sums_of_consecutive_elements([8, 10]) => []
    odd_sums_of_consecutive_elements([9]) => []
    odd_sums_of_consecutive_elements([11, 8]) => [19]

    :param nums:
    :return:
    """
    out = []
    for i in range(len(nums) - 1):
        if (nums[i] + nums[i + 1]) % 2:
            out.append(nums[i] + nums[i + 1])
    return out


def fizzbuzz_series_up(nr: int) -> list:
    """
    Create a list of fizzbuzz series.

    Create a list with the pattern

    [1,   1, 2,   1, 2, 3,   ... 1, 2, 3, 4, 5, 6, 7 .., 14, 15, 16 , .., n],

    where additionally all numbers divisible by 3 are replaced with string "fizz",
    and all numbers divisible by 5 are replaced with string "buzz"
    if number is divisible by 3 and 5, it should be replaced with "fizzbuzz:

    [1,   1, 2,   1, 2, "fizz",   ... 1, 2, "fizz", 4, "buzz", "fizz, 7 .., 14, "fizzbuzz, 16 , .., n]].

    (spaces added to show the grouping).

    If n is not positive, return empty list.

    series_up(3) → [1, 1, 2, 1, 2, "fizz"]

    series_up(2) → [1, 1, 2]

    series_up(4) → [1, 1, 2, 1, 2, "fizz", 1, 2, "fizz", 4]

    series_up(7) → [
                        1,
                        1, 2,
                        1, 2, "fizz",
                        1, 2, "fizz", 4,
                        1, 2, "fizz", 4, "buzz",
                        1, 2, "fizz", 4, "buzz", "fizz",
                        1, 2, "fizz", 4, "buzz", "fizz", 7
                    ]

    series_up(0) → []
    """
    if nr < 0:
        return []
    out = []
    for i in range(1, nr + 1):
        for j in range(1, i + 1):
            if not j % 3 and not j % 5:
                out.append('fizzbuzz')
            elif not j % 5:
                out.append('buzz')
            elif not j % 3:
                out.append('fizz')
            else:
                out.append(j)

    return out


if __name__ == '__main__':
    print(duplicate_last([1, 2, 3]))  # = > [1, 2, 3, 3]
    print(duplicate_last([7]))  # = > [7, 7]
    print(duplicate_last([]))  # = > []
    print(odd_sums_of_consecutive_elements([1, 2, 3, 5]))  # => [3, 5]
    print(odd_sums_of_consecutive_elements([8, 10]))  # => []
    print(odd_sums_of_consecutive_elements([9]))  # => []
    print(odd_sums_of_consecutive_elements([11, 8]))  # => [19]
    print(fizzbuzz_series_up(5))
