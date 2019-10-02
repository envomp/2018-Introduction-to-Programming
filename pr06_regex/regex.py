import re


def read_file(path: str) -> list:
    """
    Read file and return list of lines read.

    :param path: str
    :return: list
    """
    return [x for x in open(path, "r").readlines()]


def match_specific_string(input_data: list, keyword: str) -> int:
    """
    Check if given list of strings contains keyword.
    Return all keyword occurrences (case insensitive).

    ["Python", "python", "PYTHON", "java"], "python" -> 3

    :param input_data: list
    :param keyword: str
    :return: int
    """
    return sum([len(re.findall(keyword, x.lower())) for x in input_data])


def detect_email_addresses(input_data: list) -> list:
    """
    Check if given list of strings contains valid email addresses.
    Return all unique valid email addresses in alphabetical order presented in the list.

    ["Test", "Add me test@test.ee", "ago.luberg@taltech.ee", "What?", "aaaaaa@.com", ";_:Ö<//test@test.au??>>>;;d,"] ->
    ["ago.luberg@taltech.ee", "test@test.au", "test@test.ee"]

    :param input_data: list
    :return: list
    """
    return list(sorted(set(
        [y.group() for x in input_data for y in re.finditer(r"\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w+)+", x)])))


if __name__ == '__main__':
    list_of_lines_emails = read_file("input_detect_email_addresses_example_1.txt")  # reading from file
    print(list_of_lines_emails)
    print(detect_email_addresses(list_of_lines_emails))

    list_of_lines_keywords = read_file("input_match_specific_string_example_1.txt")
    print(match_specific_string(list_of_lines_keywords, "job"))  # 10

    list_of_lines_emails = read_file("input_detect_email_addresses_example_2.txt")  # reading from file
    print(detect_email_addresses(list_of_lines_emails))
