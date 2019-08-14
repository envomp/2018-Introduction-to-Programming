def swap_items(dic: dict) -> dict:
    """
    Given a dictionary return a new dictionary where keys and values are swapped.
    If duplicate keys in the new dictionary exist, leave the first one.

    {"a": 1, "b": 2, "c": 3} => {1: "a", 2: "b", 3: "c"}
    {"Morning": "Good", "Evening": "Good"} => {"Good": "Morning"}

    :param dic: original dictionary
    :return: dictionary where keys and values are swapped
    """
    to_return = {}
    for key, value in dic.items():
        if value not in to_return.keys():
            to_return[value] = key
    return to_return


def find_divisors(number: int) -> list:
    """
    The task is to find all the divisors for given number in range to the given number's value.
    Divisor - a number that divides evenly into another number.
    Return list of given number divisors in ascending order.
    NB! Numbers 1 and number itself must be excluded if there are more divisors
    than 1 and number itself!

    :param number: int
    :return: list of number divisors
    """
    divisiors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisiors.append(i)
    if divisiors.__len__() > 2:
        divisiors.remove(1)
        divisiors.remove(number)
    return divisiors


def sum_of_multiplies(first_num, second_num, limit) -> int:
    """
    The task is to find all the multiplies of each given of two numbers within the limit.
    Then, find the sum of those multiplies.

    :param first_num: first number
    :param second_num: second number
    :param limit: limit
    :return: sum of multiplies
    """

    sum = 0
    for i in range(limit + 1):
        if i % first_num == 0 or i % second_num == 0:
            sum += i
    return sum


def count_odds_and_evens(numbers: list) -> str:
    """
    The task is to count how many odd and even numbers does the given list contain.
    Result should be displayed as string "ODDS: {number of odds}
                                          EVENS: {number of evens}"

    :param numbers: list
    :return: str
    """
    s = ['odds' if i % 2 != 0 else 'evens' for i in numbers if i != 0]
    return f"ODDS: {s.count('odds')}\nEVENS: {s.count('evens')}"


def sum_between_25(numbers: list) -> int:
    """
    Return the sum of the numbers in the array.
    Ignore sections of numbers starting with a 2 and extending to the next 5.

    :param numbers: list
    :return:
    """
    do_count = False
    total = 0
    for num in numbers:
        if num == 2 and not do_count:
            do_count = True
        elif num == 5:
            do_count = False
        elif do_count:
            total += num
    return total


def transcribe(dna_strand: str):
    """
    Write a function that returns a transcribed RNA strand from the given DNA strand,
    that is formed by replacing each nucleotide(character) with its complement: G => C, C => G, T => A, A => U
    Return None if it is not possible to transcribe a DNA strand

    "ACGTGGTCTTAA" => "UGCACCAGAAUU"
    "gcu" => None

    :param dna_strand: original DNA strand
    :return: transcribed RNA strand in the uppercase or None
    """
    rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    new_result = ''
    try:
        for char in dna_strand:
            new_result += rna[char.upper()]
        return new_result
    except Exception:
        return None


def union_of_dict(d1: dict, d2: dict):
    """
    Given two dictionaries return dictionary that has all the key-value pairs that are the same in given dictionaries.

    union_of_dict({"a": 1, "b": 2, "c":3}, {"a": 1, "b": 42}) ==> {"a": 1}
    union_of_dict({}, {"bar": "foo"}) => {}
    """
    return dict(set(d1.items()) & set(d2.items()))


def reserve_list(input_strings: list) -> list:
    """
    Given list of strings, return new reversed list where each list element is
    reversed too. Do not reverse strings followed after element "python". If element is "java" -
    reverse mode is on again.
    P.S - "python" and "java" are not being reversed

    ['apple', 'banana', 'onion'] -> ['noino', 'ananab', 'elppa']
    ['lollipop', 'python', 'candy'] -> ['candy', 'python', 'popillol']
    ['sky', 'python', 'candy', 'java', 'fly'] -> ['ylf', 'java', 'candy', 'python', 'yks']
    ['sky', 'python', 'java', 'candy'] -> ['ydnac', 'java', 'python', 'yks']

    :param input_strings: list of strings
    :return: reversed list
    """
    reversed_mode = True
    result_list = []
    for element in input_strings:
        if element == "python":
            reversed_mode = False
        elif element == "java":
            reversed_mode = True
        elif reversed_mode:
            element = element[::-1]

        result_list.append(element)

    return result_list[::-1]


def convert_binary_to_decimal(binary_list):
    """
    Extract binary codes of given length from list and convert to decimal numbers.

    [0, 0, 0, 0] => 0.
    [0, 1, 0, 0] => 4.

    :param binary_list: list of 1 and 0 (binary code)
    :return: number converted into decimal system
    """
    return int(''.join(list(map(str, binary_list))), 2)


def print_pages(pages: str) -> list:
    """
    Find pages to print in console.

    examples:
    print_pages("2,4,9") -> [2, 4, 9]
    print_pages("2,4-7") -> [2, 4, 5, 6, 7]
    print_pages("2-5,7,10-12,17") -> [2, 3, 4, 5, 7, 10, 11, 12, 17]
    print_pages("1,1") -> [1]
    print_pages("2,1") -> [1, 2]

    :param pages: string containing page numbers and page ranges to print.
    :return: list of pages to print with no duplicates, sorted in increasing order.
    """
    return_pages = []
    if pages == "":
        return return_pages
    for i in pages.split(","):
        if "-" in i:
            for j in range(int(i.split('-')[0]), int(i.split('-')[1]) + 1):
                return_pages.append(j)
        else:
            return_pages.append(int(i))
    return sorted(list(set(return_pages)))
