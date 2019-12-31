"""Program that creates beautiful pyramids."""


def make_pyramid(base: int, char: str) -> list:
    """
    Construct a pyramid with given base.

    Pyramid should consist of given chars, all empty spaces in the pyramid list are ' '.
    Pyramid height depends on base length. Lowest floor consists of base-number chars.
    Every floor has 2 chars less than the floor lower to it.
    make_pyramid(3, "A") ->
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    make_pyramid(6, 'a') ->
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    :param base: int
    :param char: str
    :return: list
    """
    if base < 0:
        return []

    if base % 2:
        return [[char if int((base - 1) / 2) - i <= j <= int((base - 1) / 2) + i else ' '
                 for j in range(base)] for i in range(int((base - 1) / 2) + 1)]
    else:
        return [[char if int(base / 2) - 1 - i <= j <= int(base / 2) + i else ' '
                 for j in range(base)] for i in range(int(base / 2))]


def join_pyramids(pyramid_a: list, pyramid_b: list) -> list:
    """
    Join together two pyramid lists.

    Get 2 pyramid lists as inputs. Join them together horizontally.
    If the the pyramid heights are not equal, add empty lines on the top until they are equal.
    join_pyramids(make_pyramid(3, "A"), make_pyramid(6, 'a')) ->
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]

    :param pyramid_a: list
    :param pyramid_b: list
    :return: list
    """
    if not len(pyramid_a) and not len(pyramid_b):
        return []
    elif not len(pyramid_a):
        return pyramid_b
    elif not len(pyramid_b):
        return pyramid_a

    if len(pyramid_a) < len(pyramid_b):
        [pyramid_a.insert(0, [' ' for i in range(len(pyramid_a[0]))]) for j in range(len(pyramid_b) - len(pyramid_a))]
    elif len(pyramid_a) > len(pyramid_b):
        [pyramid_b.insert(0, [' ' for i in range(len(pyramid_b[0]))]) for j in range(len(pyramid_a) - len(pyramid_b))]

    return [pyramid_a[i] + pyramid_b[i] for i in range(len(pyramid_a))]


def to_string(pyramid: list) -> str:
    """
    Return pyramid list as a single string.

    Join pyramid list together into a string and return it.
    to_string(make_pyramid(3, 'A')) ->
    '''
     A
    AAA
    '''

    :param pyramid: list
    :return: str
    """
    if not len(pyramid):
        return ""

    pyramid_str = [pyramid[i][j] + '\n' if i < len(pyramid) - 1 and j == len(pyramid[i]) - 1 else pyramid[i][j]
                   for i in range(len(pyramid)) for j in range(len(pyramid[i]))]

    return ''.join(pyramid_str)


if __name__ == '__main__':
    pyramid_a = make_pyramid(3, "A")
    print(pyramid_a)  # ->
    """
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    """

    pyramid_b = make_pyramid(6, 'a')
    print(pyramid_b)  # ->
    """
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    """

    joined = join_pyramids(pyramid_a, pyramid_b)
    print(joined)  # ->
    """
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]
    """

    pyramid_string = to_string(joined)
    print(pyramid_string)  # ->
