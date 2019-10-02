import re


def read_file(path: str) -> list:
    return [line.rstrip('\n') for line in open(path, encoding="utf8")]


def match_specific_string(input_data: list, keyword: str) -> int:
    return sum([len(re.findall("(?i)" + keyword, element)) for element in input_data])


def detect_email_addresses(input_data: list) -> list:
    return list(sorted(set([x.group() for y in input_data for x in re.finditer(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", y)])))


if __name__ == '__main__':
    list_of_lines_emails = read_file("input_detect_email_addresses_example_1.txt")  # reading from file
    print(list_of_lines_emails)
    print(detect_email_addresses(list_of_lines_emails))

    list_of_lines_keywords = read_file("input_match_specific_string_example_1.txt")
    print(match_specific_string(list_of_lines_keywords, "job"))  # 10

    list_of_lines_emails = read_file("input_detect_email_addresses_example_2.txt")  # reading from file
    print(detect_email_addresses(list_of_lines_emails))
