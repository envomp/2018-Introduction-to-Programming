"""KTJ1."""


def remove_middle_character(string: str) -> str:
    """
    Return a string where middle character is removed if the string lentgh is equal to odd number, otherwise return input string.

    In the case of empty string, return empty string.

    remove_middle_char("kalev") => "kaev"
    remove_middle_char("linda") => "linda"
    remove_middle_char("olevipoeg") => "olevpoeg"
    remove_middle_char("") => ""
    """
    if len(string) % 2:
        middle = len(string) // 2
        return string[:middle] + string[middle + 1:]
    else:
        return string


def has_seven(nums):
    """
    Given a list if ints, return True if the value 7 appears in the list exactly 3 times and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    if nums.count(7) == 3:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return False
        else:
            return True
    else:
        return False


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
    list_move([], 3, 4) => [[], [], [], []]
    """
    out = []

    if factor > len(initial_list) and len(initial_list) > 0:
        factor = factor % len(initial_list)

    for i in range(amount):
        out.append(initial_list)
        initial_list = initial_list[-factor:] + initial_list[:-factor]

    return out


def list_move2(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.
    """
    out = []

    if factor > len(initial_list) and len(initial_list) > 0:
        factor = factor % len(initial_list)

    for i in range(amount):
        out.append(initial_list[-factor * i % len(initial_list) if len(initial_list) > 0 else 1:] +
                   initial_list[:-factor * i % len(initial_list) if len(initial_list) > 0 else 1])

    return out


if __name__ == '__main__':
    print(remove_middle_character("kalev"))  # => "kaev"
    print(remove_middle_character("linda"))  # => "lida"
    print(remove_middle_character("olevipoeg"))  # => "olevpoeg"
    print(remove_middle_character(""))  # => ""
    print(has_seven([1, 2, 3]))  # => False
    print(has_seven([7, 1, 7, 7]))  # => False
    print(has_seven([7, 1, 7, 1, 7]))  # => True
    print(has_seven([7, 1, 7, 1, 1, 7]))  # => False
