import operator

import math
import re
from functools import lru_cache, partial, partialmethod
from typing import Callable


class Student:
    BINARY_ONES_REGEX = re.compile(r'.(\d+) ones in its binary form.')
    BINARY_ZERO_REGEX = re.compile(r'.(\d+) zero(?:es)? in its binary form.')

    def __init__(self, biggest_number: int):
        """
        Constructor.

        save biggest number into a variable that is attainable later on.
        Create a collection of all possible results [possible_answers] <- dont rename that (can be a list or a set)
        :param biggest_number: biggest possible number(inclusive) to guess
        NB: calculating using sets is much faster compared to lists
        """
        self.possible_answers = set([num for num in range(biggest_number + 1)])

    def decision_branch(self, sentence: str):
        """
        Regex can and should be used here.

        :param sentence: sentence to solve
        call one of the functions bellow (within this class) and return either one of the following strings:
        f"Possible answers are {sorted_list_of_possible_answers_in_growing_sequence)}." if there are multiple possibilities
        f"The number I needed to guess was {final_answer}." if the result is certain
        """
        # binary ones
        binary_one_match = self.BINARY_ONES_REGEX.search(sentence)
        if binary_one_match:
            self.deal_with_number_of_ones(int(binary_one_match.group(1)))
            return

        binary_zero_match = self.BINARY_ZERO_REGEX.search(sentence)
        if binary_zero_match:
            self.deal_with_number_of_zeroes(int(binary_zero_match.group(1)))
            return

    def intersect_possible_answers(self, update: list):
        """
        Logical AND between two sets.

        :param update: new list to be put into conjunction with self.possible_answers
        conjunction between self.possible_answers and update
        https://en.wikipedia.org/wiki/Logical_conjunction
        """
        self.possible_answers &= set(update)

    def exclude_possible_answers(self, update: list):
        """
        Logical SUBTRACTION between two sets.

        :param update: new list to be excluded from self.possible_answers
        update excluded from self.possible_answers
        """
        self.possible_answers -= set(update)

    def deal_with_number_of_zeroes(self, amount_of_zeroes: int):
        """
        Filter possible_answers to match the amount of zeroes in its binary form.

        :param amount_of_zeroes: number of zeroes in the correct number's binary form
        """
        num_of_zeros_in_bin = lambda num: len(self._get_bin(num).replace('1', ''))
        self.possible_answers = {num for num in self.possible_answers if num_of_zeros_in_bin(num) == amount_of_zeroes}

    def deal_with_number_of_ones(self, amount_of_ones: int):
        """
        Filter possible answers to match the amount of ones in its binary form.

        :param amount_of_ones: number of zeroes in the correct number's binary form
        """
        num_of_ones_in_bin = lambda num: len(self._get_bin(num).replace('0', ''))
        self.possible_answers = {num for num in self.possible_answers if num_of_ones_in_bin(num) == amount_of_ones}

    def deal_with_primes(self, is_prime: bool):
        """
        Filter possible answers to either keep or remove all primes.

        Call find_primes_in_range to get all composite numbers in range.
        :param is_prime: boolean whether the number is prime or not
        """
        pass

    def deal_with_composites(self, is_composite: bool):
        """
        Filter possible answers to either keep or remove all composites.

        Call find_composites_in_range to get all composite numbers in range.
        :param is_composite: boolean whether the number is composite or not
        """
        pass

    def deal_with_dec_value(self, decimal_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param decimal_value: decimal value within the number like 9 in 192
        """
        pass

    def deal_with_hex_value(self, hex_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param decimal_value: hex value within the number like e in fe2
        """
        pass

    def deal_with_quadratic_equation(self, equation: str, to_multiply: bool, multiplicative: float, is_bigger: bool):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        Regex can be used here.
        Call quadratic_equation_solver with variables a, b, c.
        deal_with_dec_value should be called.
        :param equation: the quadratic equation
        :param to_multiply: whether it is necessary to multiply or divide with a given multiplicative
        :param multiplicative: the multiplicative to multiply or divide with
        :param is_bigger: to use the bigger or smaller result of the quadratic equation(min or max from [x1, x2])
        """
        pass

    def deal_with_fibonacci_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all fibonacci numbers.

        Call find_fibonacci_numbers to get all fibonacci numbers in range.
        :param is_in: boolean whether the number is in fibonacci sequence or not
        """
        pass

    def deal_with_catalan_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all catalan numbers.

        Call find_catalan_numbers to get all catalan numbers in range.
        :param is_in: boolean whether the number is in catalan sequence or not
        """
        pass

    def deal_with_number_order(self, increasing: bool, to_be: bool):
        """
        Filter possible answers to either keep or remove all numbers with wrong order.

        :param increasing: boolean whether to check is in increasing or decreasing order
        :param to_be: boolean whether the number is indeed in that order
        """
        if increasing:
            self._filter_posible_answers(self._is_in_increasing_order, to_be)
        else:
            self._filter_posible_answers(self._is_in_decreasing_order, to_be)

    def _filter_posible_answers(self, f, positive: bool = False):
        self.possible_answers = {num for num in self.possible_answers if (f(num) if positive else not f(num))}

    @staticmethod
    def _get_bin(num: int) -> str:
        return '{0:b}'.format(num)

    def _is_in_order(self, num: int, operator) -> bool:
        previous = None
        for current in str(num):
            if previous and not operator(current, previous):
                return False
            previous = current
        return True

    _is_in_increasing_order = partialmethod(_is_in_order, operator=operator.gt)
    _is_in_decreasing_order = partialmethod(_is_in_order, operator=operator.lt)


regex_a = r'((?:- )?\d*)x2(?:[^0-9]|$)'
regex_b = r'((?:- )?\d*)x(?:[^02-9]|$)'
regex_c = r'((?<!x)(?:- )?\d+(?![0-9]*x))'

REGEX_A = re.compile(regex_a)
REGEX_B = re.compile(regex_b)
REGEX_C = re.compile(regex_c)


def _convert_quantifiers_to_int(quantifier: str, change_mark=False) -> int:
    quantifier = quantifier.replace(' ', '')  # - 2  ->  -2
    if quantifier == '':
        return 1 if not change_mark else -1
    if quantifier == '-':
        return -1 if not change_mark else 1
    return int(quantifier) if not change_mark else - int(quantifier)


def _process_certain_quantizer(equation: str, regex, append_plus: bool, hide_one: bool = True) -> str:
    left_side, right_side = equation.split(' = ')
    left_values = regex.findall(left_side)
    right_values = regex.findall(right_side)
    int_values = [_convert_quantifiers_to_int(q) for q in left_values]
    int_values += [_convert_quantifiers_to_int(q, change_mark=True) for q in right_values]
    quantifier = sum(int_values)
    if quantifier == 1 and hide_one:
        return '+ '
    if quantifier == -1 and hide_one:
        return '- '
    str_quantifier = str(quantifier) + ' '
    if append_plus and quantifier > 0:
        str_quantifier = '+ ' + str_quantifier
    return str_quantifier.strip().replace('-', '- ')


def normalize_quadratic_equation(equation: str) -> str:
    """
    Normalize the quadratic equation.

    normalize_quadratic_equation("x2 + 2x = 3") => "x2 + 2x - 3 = 0"
    normalize_quadratic_equation("0 = 3 + 1x2") => "x2 + 3 = 0"
    normalize_quadratic_equation("2x + 2 = 2x2") => "2x2 - 2x - 2 = 0"
    normalize_quadratic_equation("0x2 - 2x = 1") => "2x + 1 = 0"
    normalize_quadratic_equation("0x2 - 2x = 1") => "2x + 1 = 0"
    normalize_quadratic_equation("2x2 + 3x - 4 + 0x2 - x1 + 0x1 + 12 - 12x2 = 4x2 + x1 - 2") => "14x2 - x - 10 = 0"

    :param equation: quadratic equation to be normalized
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return: normalized equation
    """
    x2_quantifier = _process_certain_quantizer(equation, REGEX_A, False)

    x_quantifier = _process_certain_quantizer(equation, REGEX_B, True)

    linear_quantifier = _process_certain_quantizer(equation, REGEX_C, True, hide_one=False)
    # TODO If member is moved to the other side of the equation, the mark must be changed.
    #  So spilt the equation into two parts and deal with them separately.
    x2 = f'{x2_quantifier}x2' if x2_quantifier != '0' else ''
    x = f' {x_quantifier}x' if x_quantifier != '0' else ''
    c = f' {linear_quantifier}' if linear_quantifier != '0' else ''
    equation = f'{x2}{x}{c} = 0'.strip()
    if equation.startswith('-'):
        equation = equation.replace('-', 'minus').replace('+', '-').replace('minus', '+')

    return equation.strip('+ ').strip()


def quadratic_equation_solver(equation: str):
    """
    Solve the normalized quadratic equation.

    :param str: quadratic equation
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return:
    if there are no solutions, return None.
    if there is exactly 1 solution, return it.
    if there are 2 solutions, return them in a tuple, where smaller is first
    all numbers are returned as floats.
    """
    find_quantifier = partial(_process_certain_quantizer, append_plus=False, hide_one=False)

    def quantifier_as_int(equation: str, regex) -> int:
        quantifier = find_quantifier(equation, regex).replace('- ', '-')
        return int(quantifier)

    a = quantifier_as_int(equation, REGEX_A)
    b = quantifier_as_int(equation, REGEX_B)
    c = quantifier_as_int(equation, REGEX_C)

    if not a:
        return -c / b
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None

    def find_answer(a: int, b: int, operation: Callable[[int, int], int]):
        return operation(-b, math.sqrt(discriminant)) / (2 * a)

    answer1, answer2 = find_answer(a, b, operator.add), find_answer(a, b, operator.sub)
    if answer1 == answer2:
        return answer1
    return tuple(sorted([answer1, answer2]))


def find_primes_in_range(biggest_number: int):
    """
    Find all primes in range(end inclusive).

    :param biggest_number: all primes in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    :return: list of primes
    """

    def is_prime(num: int) -> bool:
        if num == 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    return [num for num in range(1, biggest_number + 1) if is_prime(num)]


def find_composites_in_range(biggest_number: int):
    """
    Find all composites in range(end inclusive).

    Call find_primes_in_range from this method to get all composites
    :return: list of composites
    :param biggest_number: all composites in range of biggest_number(included)
    """
    primes = set(find_primes_in_range(biggest_number))
    return [num for num in range(1, biggest_number + 1) if num not in primes]


def find_fibonacci_numbers(biggest_number: int):
    """
    Find all Fibonacci numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all fibonacci numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Fibonacci_number
    :return: list of fibonacci numbers
    """
    if biggest_number == 1:
        return [0]
    if biggest_number == 2:
        return [0, 1]
    fibonacci_numbers = [0, 1]
    for i in range(2, biggest_number + 1):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return fibonacci_numbers[1:]


def find_catalan_numbers(biggest_number: int):
    """
    Find all Catalan numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all catalan numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Catalan_number
    :return: list of catalan numbers
    """

    @lru_cache
    def catalan(num: int) -> int:
        if num <= 1:
            return 1
        result = 0
        for i in range(num):
            result += catalan(i) * catalan(num - i - 1)

        return result

    catalan_numbers = []
    for n in range(1, biggest_number + 1):
        catalan_numbers.append(catalan(n))
    return catalan_numbers


if __name__ == '__main__':
    student = Student(100)
    print(student.possible_answers)
    student.deal_with_number_order(True, False)
    print(student.possible_answers)
    exit(0)
    print(quadratic_equation_solver("x1 = 1"))
    print(quadratic_equation_solver("x2 + 2x = 3"))  # => "x2 + 2x - 3 = 0" OK
    print(quadratic_equation_solver("0 = 3 + 1x2"))  # => "x2 + 3 = 0"
    print(quadratic_equation_solver("2x + 2 = 2x2"))  # => "2x2 - 2x - 2 = 0"
    print(quadratic_equation_solver("0x2 - 2x = 1"))  # => "2x + 1 = 0"
    print(quadratic_equation_solver("0x2 - 2x = 1"))  # => "2x + 1 = 0"
    print(quadratic_equation_solver(
        "2x2 + 3x - 4 + 0x2 - x1 + 0x1 + 12 - 12x2 = 4x2 + x1 - 2"))  # => "14x2 - x - 10 = 0"

