"""KT3 (R12)."""


def last_to_first(s):
    """
    Move last symbol to the beginning of the string.

    last_to_first("ab") => "ba"
    last_to_first("") => ""
    last_to_first("hello") => "ohell"
    """
    if not len(s):
        return ""

    return s[-1] + s[:-1]


def take_partial(text: str, leave_count: int, take_count: int) -> str:
    """
    Take only part of the string.

    Ignore first leave_count symbols, then use next take_count symbols.
    Repeat the process until the end of the string.

    The following conditions are met (you don't have to check those):
    leave_count >= 0
    take_count >= 0
    leave_count + take_count > 0

    take_partial("abcdef", 2, 3) => "cde"
    take_partial("abcdef", 0, 1) => "abcdef"
    take_partial("abcdef", 1, 0) => ""
    """
    result = ""
    for i in range(0, len(text), leave_count + take_count):
        result += text[i + leave_count:i + leave_count + take_count]
    """
    while len(text) > 0:
        result += text[leave_count:leave_count + take_count]
        text = text[leave_count + take_count:]
    """
    return result


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.

    This function creates a list with amount of lists inside it.
    In each sublist, elements are shifted right by factor elements.
    factor >= 0

    list_move(["a", "b", "c"], 3, 0) => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    list_move(["a", "b", "c"], 3, 1) => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    list_move([1, 2, 3], 3, 2) => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    list_move([1, 2, 3], 4, 1) => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    list_move([], 3, 4) => [[], [], []]
    """
    result = []
    if factor > len(initial_list) and len(initial_list) > 0:
        factor = factor % len(initial_list)
    for i in range(amount):
        result.append(initial_list)
        initial_list = initial_list[-factor:] + initial_list[:-factor]
    return result


if __name__ == '__main__':
    print(last_to_first("ab"))  # => "ba"
    print(last_to_first(""))  # => ""
    print(last_to_first("hello"))  # => "ohell"
    print(take_partial("abcdef", 2, 3))  # = > "cde"
    print(take_partial("abcdef", 0, 1))  # = > "abcdef"
    print(take_partial("abcdef", 1, 0))  # = > ""
    print(list_move(["a", "b", "c"], 3, 0))  # = > [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    print(list_move(["a", "b", "c"], 3, 4))  # = > [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    print(list_move([1, 2, 3], 3, 2))  # = > [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    print(list_move([1, 2, 3], 4, 1))  # = > [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    print(list_move([], 3, 4))  # = > [[], [], []]
