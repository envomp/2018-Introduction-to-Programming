"""KT1 (K14)."""


def capitalize_string(s: str) -> str:
    """
    Return capitalized string. The first char is capitalized, the rest remain as they are.

    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    return s[:1].upper() + s[1:]


def sum_half_evens(nums: list) -> int:
    """
    Return the sum of first half of even ints in the given array.

    If there are odd number of even numbers, then include the middle number.

    sum_half_evens([2, 1, 2, 3, 4]) => 4
    sum_half_evens([2, 2, 0, 4]) => 4
    sum_half_evens([1, 3, 5, 8]) => 8
    sum_half_evens([2, 3, 5, 7, 8, 9, 10, 11]) => 10
    """
    evens = [n for n in nums if n % 2 == 0]

    return sum(evens[:(len(evens) + 1) // 2])


def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("") => 0
    """
    if not len(s):
        return 0

    str = s[0]
    count = 1
    max = 1
    for i in range(1, len(s)):
        if str == s[i]:
            count += 1
            if count > max:
                max = count
        else:
            str = s[i]
            count = 1

    return max


if __name__ == '__main__':
    print(capitalize_string("abc"))  # = > "Abc"
    print(capitalize_string("ABc"))  # = > "ABc"
    print(capitalize_string(""))  # = > ""
    print(sum_half_evens([2, 1, 2, 3, 4]))  # => 4
    print(sum_half_evens([2, 2, 6, 4]))  # => 4
    print(sum_half_evens([1, 3, 5, 8]))  # => 8
    print(sum_half_evens([2, 3, 5, 7, 8, 9, 10, 11]))  # => 10)

    print(max_block("hooplaaa"))  # => 2
    print(max_block("aabbCCCddBBBxx"))  # => 3
    print(max_block(""))  # => 0)
