"""Regex."""
import re


def read_file(path: str) -> list:
    """
    Read file and return list of lines read.

    :param path: str
    :return: list
    """
    collected_data = []

    with open(path, encoding='utf-8') as file:
        for line in file:  # Loops over the file object and reads each line.
            collected_data.append(line.rstrip())

    return collected_data


def match_specific_string(input_data: list, keyword: str) -> int:
    """
    Check if given list of strings contains keyword.

    Return all keyword occurrences (case insensitive). If an element cointains the keyword several times, count all the occurrences.
    ["Python", "python", "PYTHON", "java"], "python" -> 3

    :param input_data: list
    :param keyword: str
    :return: int
    """
    count = 0
    regex = '(' + keyword + ')'

    for row in input_data:
        for match in re.finditer(regex, row, re.IGNORECASE):
            if match.group(1):
                count += 1

    return count


def detect_email_addresses(input_data: list) -> list:
    """
    Check if given list of strings contains valid email addresses.

    Return all unique valid email addresses in alphabetical order presented in the list.
    ["Test", "Add me test@test.ee", "ago.luberg@taltech.ee", "What?", "aaaaaa@.com", ";_:Ö<//test@test.au??>>>;;d,"] ->
    ["ago.luberg@taltech.ee", "test@test.au", "test@test.ee"]

    :param input_data: list
    :return: list
    """
    valid_addresses = []

    # regex = r"(?=[a-z0-9][a-z0-9@.!#$%&'*+\-=?^_`{|]{5,253})([a-z0-9][a-z0-9.!#$%&'*+\-=?^_`{|]{0,63}" \
    # r"(?<![.!#$%&'*+\-=?^_`{|])@(?:(?=[a-z0-9-]{1,63}\.)[a-z0-9]+(?:-[a-z0-9]+)*\.){1,8}[a-z]{2,63})"

    # regex = r"([a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+)"

    regex = r"([a-z0-9][a-z0-9.%+_-]*@(?:(?=[a-z0-9-]+\.)[a-z0-9]+(?:-[a-z0-9]+)*\.)+[a-z]{2,})"

    for row in input_data:
        for match in re.finditer(regex, row, re.IGNORECASE):
            if match.group(1):
                valid_addresses.append(match.group(1))

    valid_addresses = list(set(valid_addresses))
    valid_addresses.sort()

    return valid_addresses


if __name__ == '__main__':
    list_of_lines_emails = read_file("input_detect_email_addresses_example_2.txt")  # reading from file
    print(detect_email_addresses(list_of_lines_emails))
    # ['allowed@example.com', 'firstname-lastname@example.com',
    # 'right@example.com', 'spoon@lol.co.jp', 'testtest@dome.museum', 'testtest@example.name']
    list_of_lines_keywords = read_file("input_match_specific_string_example_1.txt")
    print(match_specific_string(list_of_lines_keywords, "job"))  # 9
