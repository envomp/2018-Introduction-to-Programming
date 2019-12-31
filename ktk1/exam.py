"""KTK1 (L)."""


def remove_middle_character(string: str) -> str:
    """
    Return a string where middle character is removed if the string lentgh is equal to odd number, otherwise return input string.

    In the case of empty string, return empty string.
    remove_middle_char("kalev") => "kaev"
    remove_middle_char("aadu") => "aadu"
    remove_middle_char("olevipoeg") => "olevpoeg"
    remove_middle_char("") => ""
    """
    if not len(string) % 2:
        return string

    return string[:len(string) // 2] + string[len(string) // 2 + 1:]


def multiplication(number: int) -> list:
    """
    Return list, where input number is multiplicated with numbers from 1 to 10.

    Input number can be any integer (negative as well).
    multiplication(5) => [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    multiplication(0) => [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    return [i * number for i in range(1, 11)]


def chars_combinations(string: str) -> list:
    """
    Return all combinations of string characters by 2 string length is bigger than 1.

    otherwise return empty list.
    Characters in results should follow their natural order in input string.
    chars_combinations("habe") => ["ha", "hb", "he", "ab", "ae", "be"]
    chars_combinations("az") => ["az"]
    chars_combinations("s") => []
    chars_combinations("") => []
    """
    if len(string) < 2:
        return []

    return [string[i] + string[j] for i in range(len(string) - 1) for j in range(i + 1, len(string))]


if __name__ == '__main__':
    print(remove_middle_character("kalev"))  # => "kaev"
    print(remove_middle_character("aadu"))  # => "aadu"
    print(remove_middle_character("olevipoeg"))  # => "olevpoeg"
    print(remove_middle_character(""))  # => ""
    print(multiplication(5))  # => [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    print(multiplication(0))  # => [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(chars_combinations("habe"))   # => ["ha", "hb", "he", "ab", "ae", "be"])
