"""KT2 (R10)."""


def switch_lasts_and_firsts(s: str) -> str:
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    if len(s) < 4:
        return s[::-1]

    return s[-2:] + s[2:-2] + s[:2]


def has_seven(nums):
    """
    Given a list if ints, return True if the value 7 appears in the list exactly 3 times
    and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    if nums.count(7) != 3:
        return False
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return False
    return True


def g_happy(s):
    """
    We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right.

    Return True if all the g's in the given string are happy.

    g_happy("xxggxx") => True
    g_happy("xxgxx") => False
    g_happy("xxggyygxx") => False
    """
    for i in range(len(s)):
        if s[i] == 'g':
            if i > 0 and s[i - 1] == 'g':
                continue
            if i < len(s) - 1 and s[i + 1] == 'g':
                continue
            return False
    return True


if __name__ == '__main__':
    print(switch_lasts_and_firsts("ambulance"))  # 3 => "cebulanam"
    print(switch_lasts_and_firsts("firetruck"))  # => "ckretrufi"
    print(switch_lasts_and_firsts("car"))  # => "rac"
    print(has_seven([1, 2, 3]))  # => False
    print(has_seven([7, 1, 7, 7]))  # => False
    print(has_seven([7, 1, 7, 1, 7]))  # => True
    print(has_seven([7, 1, 7, 1, 1, 7]))  # => False
    print(g_happy("ggxgxgg"))  # => True
    print(g_happy("ggxxggxxgg"))  # => False
    print(g_happy("xxggyygxx"))  # => False
