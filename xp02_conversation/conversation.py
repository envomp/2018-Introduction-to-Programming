"""Conversation."""
from math import sqrt
import re

regex_a = '(((?<= )|(?<=^))(- )?[0-9]*)x2( |$)'
regex_b = '(((?<= )|(?<=^))(- )?[0-9]*)x1?( |$)'
regex_c = '(((?<= )|(?<=^))(- )?(?<!x)[0-9]+)(?!x)( |$)'


class Student:
    """Class Student."""

    def __init__(self, biggest_number: int) -> None:
        """
        Constructor.

        Save biggest number into a variable that is attainable later on.
        Create a collection of all possible results [possible_answers] <- dont rename that (can be a list or a set)
        :param biggest_number: biggest possible number(inclusive) to  guess
        NB: calculating using sets is much faster compared to lists
        """
        self.possible_answers = set([all_possible_answers for all_possible_answers in range(biggest_number + 1)])
        self.biggest_number = biggest_number

    def decision_ones(self, sentence: str) -> None:
        """
        Decision number of ones.

        :param sentence: sentence to solve
        :return:
        """
        regex = '([0-9]+) ones?'
        for match in re.finditer(regex, sentence):
            if int(match.group(1)) >= 0:
                self.deal_with_number_of_ones(int(match.group(1)))


    def decision_zeroes(self, sentence: str) -> None:
        """
        Decision number of zeroes.

        :param sentence: sentence to solve
        :return:
        """
        regex = '([0-9]+) zeroe?s?'
        for match in re.finditer(regex, sentence):
            if int(match.group(1)) >= 0:
                self.deal_with_number_of_zeroes(int(match.group(1)))

    def decision_hex(self, sentence: str) -> None:
        """
        Decision hex.

        :param sentence: sentence to solve
        :return:
        """
        regex = 'hex value: "(.+)"'
        for match in re.finditer(regex, sentence):
            if match.group(1):
                self.deal_with_hex_value(match.group(5))

    def decision_decimal(self, sentence: str) -> None:
        """
        Decision decimal.

        :param sentence: sentence to solve
        :return:
        """
        regex = 'decimal value: "(.+)"'
        for match in re.finditer(regex, sentence):
            if int(match.group(1)) >=1:
                self.deal_with_dec_value(match.group(1))

    def decision_catalan(self, sentence: str) -> None:
        """
        Decision catalan.

        :param sentence: sentence to solve
        :return:
        """
        regex = "(.*(n['o]t).+)?(catalan)"
        for match in re.finditer(regex, sentence):
            if match.group(3) == 'catalan':
                is_in = True if not match.group(3) else False
                self.deal_with_catalan_sequence(is_in)

    def decision_fibonacci(self, sentence: str) -> None:
        """
        Decision fibonacci.

        :param sentence: sentence to solve
        :return:
        """
        regex = "(.*(n['o]t).+)?(fibonacci)"
        for match in re.finditer(regex, sentence):
            if match.group(3) == 'fibonacci':
                is_in = True if not match.group(2) else False
                self.deal_with_fibonacci_sequence(is_in)


    def decision_composite(self, sentence: str) -> None:
        """
        Decision composite numbers.

        :param sentence: sentence to solve
        :return:
        """
        regex = "(.*.(n['o]t).+)?(composite)"
        for match in re.finditer(regex, sentence):
            if match.group(3) == 'composite':
                is_in = True if not match.group(2) else False
                self.deal_with_composites(is_in)

    def decision_prime(self, sentence: str) -> None:
        """
        Decision prime numbers.

        :param sentence: sentence to solve
        :return:
        """
        regex = "(.*(n['o]t).+)?(prime)"
        for match in re.finditer(regex, sentence):
            if match.group(3) == 'prime':
                is_in = True if not match.group(2) else False
                self.deal_with_primes(is_in)

    def decision_inc_dec(self, sentence: str) -> None:
        """
        Decision increasing or decreasing.

        :param sentence: sentence to solve
        :return:
        """
        regex = "(.*(n['o]t).+)?(increasing|decreasing).+(order)"
        for match in re.finditer(regex, sentence):
            if match.group(4) == 'order':
                to_be = True if not match.group(2) else False
                increasing = True if match.group(3) == 'increasing' else False
                self.deal_with_number_order(increasing, to_be)

    def decision_quadratic(self, sentence: str) -> None:
        """
        Decision quadratic equation.

        :param sentence: sentence to solve
        :return:
        """
        regex = '([+-]?[0-9]+.[0-9]+) (times).*(bigger|smaller).*equation:"(.+)"|' \
                '.*(bigger|smaller).*equation:"(.+)".* (divided) by ([+-]?[0-9]+.[0-9]+)'
        for match in re.finditer(regex, sentence):
            if match.group(2) == 'times':
                multiplicative = float(match.group(1))
                to_multiply = True
                is_bigger = True if match.group(3) == 'bigger' else False
                equation = match.group(24)
            else:
                multiplicative = float(match.group(8))
                to_multiply = False
                is_bigger = True if match.group(5) == 'bigger' else False
                equation = match.group(6)

            self.deal_with_quadratic_equation(equation, to_multiply, multiplicative, is_bigger)

    def decision_branch(self, sentence: str) -> str:
        """
        Regex can and should be used here.

        :param sentence: sentence to solve
        call one of the functions bellow (within this class) and return either one of the following strings:
        f"Possible answers are {sorted_list_of_possible_answers_in_growing_sequence)}."
        if there are multiple possibilities
        f"The number I needed to guess was {final_answer}." if the result is certain
        """
        regexes = [
            '([0-9]+) ones?',
            '([0-9]+) zeroe?s?',
            'hex value: "(.+)"',
            'decimal value: "(.+)"',
            '(.*(n[\'o]t).+)?(catalan)',
            '(.*(n[\'o]t).+)?(fibonacci)',
            '(.*(n[\'o]t).+)?(composite)',
            '(.*(n[\'o]t).+)?(prime)',
            '(.*(n[\'o]t).+)?(increasing|decreasing).+(order)',
            '([+-]?[0-9]+.[0-9]+) (times).*(bigger|smaller).*equation:"(.+)"|'
            '.*(bigger|smaller).*equation:"(.+)".* (divided) by ([+-]?[0-9]+.[0-9]+)'
        ]

        for i in range(len(regexes)):
            for match in re.finditer(regexes[i], sentence):
                if match.group(0):
                    self.decision_ones(sentence) if i == 0 else self.decision_zeroes(sentence) if i == 1 \
                        else self.decision_hex(sentence) if i == 2 else self.decision_decimal(sentence) if i == 3 \
                        else self.decision_catalan(sentence) if i == 4 else self.decision_fibonacci(sentence) if i == 5\
                        else self.decision_composite(sentence) if i == 6 else self.decision_prime(sentence) if i == 7 \
                        else self.decision_inc_dec(sentence) if i == 8 else self.decision_quadratic(sentence)

        return f"Possible answers are {sorted(self.possible_answers)}." if len(sorted(self.possible_answers)) > 1 \
            else f"The number I needed to guess was {sorted(self.possible_answers)[0]}."

    def intersect_possible_answers(self, update: list) -> None:
        """
        Logical AND between two sets.

        :param update: new list to be put into conjunction with self.possible_answers
        conjunction between self.possible_answers and update
        https://en.wikipedia.org/wiki/Logical_conjunction
        """
        self.possible_answers.intersection_update(update)

    def exclude_possible_answers(self, update: list) -> None:
        """
        Logical SUBTRACTION between two sets.

        :param update: new list to be excluded from self.possible_answers
        update excluded from self.possible_answers
        """
        self.possible_answers.difference_update(update)

    def deal_with_number_of_zeroes(self, amount_of_zeroes: int) -> None:
        """
        Filter possible_answers to match the amount of zeroes in its binary form.

        :param amount_of_zeroes: number of zeroes in the correct number's binary form
        """
        if amount_of_zeroes >= 0:
            is_amount_of_zeroes = [1]

            for i in self.possible_answers:
                if bin(i)[2:].count("0") == amount_of_zeroes:
                    is_amount_of_zeroes.append(i)

            self.possible_answers.intersection_update(is_amount_of_zeroes)


    def deal_with_number_of_ones(self, amount_of_ones: int) -> None:
        """
        Filter possible answers to match the amount of ones in its binary form.

        :param amount_of_ones: number of ones in the correct number's binary form.
        """
        if amount_of_ones >= 0:
            is_amount_of_ones = []

            for i in self.possible_answers:
                if bin(i)[2:].count("1") == amount_of_ones:
                    is_amount_of_ones.append(i)

            self.possible_answers.intersection_update(is_amount_of_ones)

    def deal_with_primes(self, is_prime: bool) -> None:
        """
        Filter possible answers to either keep or remove all primes.

        Call find_primes_in_range to get all prime numbers in range.
        :param is_prime: boolean whether the number is prime or not
        """
        if is_prime:
            self.possible_answers.intersection_update(find_primes_in_range(self.biggest_number))
        else:
            self.possible_answers.difference_update(find_primes_in_range(self.biggest_number))

    def deal_with_composites(self, is_composite: bool) -> None:
        """
        Filter possible answers to either keep or remove all composites.

        Call find_composites_in_range to get all composite numbers in range.
        :param is_composite: boolean whether the number is composite or not
        """
        if is_composite:
            self.possible_answers.intersection_update(find_composites_in_range(self.biggest_number))
        else:
            self.possible_answers.difference_update(find_composites_in_range(self.biggest_number))

    def deal_with_dec_value(self, decimal_value: str) -> None:
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param decimal_value: decimal value within the number like 9 in 192
        """
        is_decimal_value = []

        for i in self.possible_answers:
            if decimal_value in str(i):
                is_decimal_value.append(i)

        self.possible_answers.intersection_update(is_decimal_value)


    def deal_with_hex_value(self, hex_value: str) -> None:
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param hex_value: hex value within the number like e in fe2.
        """
        regex = '([0-9a-fA-F]+)'
        for match in re.finditer(regex, hex_value):
            if match.group(1):
                hex_value = match.group(1)

        is_hex_value = []

        for i in self.possible_answers:
            if hex_value in hex(i)[2:]:
                is_hex_value.append(i)

        self.possible_answers.intersection_update(is_hex_value)

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
        norm_equation = normalize_quadratic_equation(equation)
        result = quadratic_equation_solver(norm_equation)

        if result is not None:
            if len(result) == 1:
                x = quadratic_equation_solver(norm_equation)
            else:
                x1, x2 = quadratic_equation_solver(norm_equation)
                x = max(x1, x2) if is_bigger else min(x1, x2)

            multiplicative = float(multiplicative)

            if to_multiply:
                x = round(x * multiplicative)
            elif multiplicative != 0:
                x = round(x / multiplicative)

            self.deal_with_dec_value(str(x))

    def deal_with_fibonacci_sequence(self, is_in: bool) -> None:
        """
        Filter possible answers to either keep or remove all fibonacci numbers.

        Call find_fibonacci_numbers to get all fibonacci numbers in range.
        :param is_in: boolean whether the number is in fibonacci sequence or not
        """
        if is_in:
            self.possible_answers.intersection_update(find_fibonacci_numbers(self.biggest_number))
        else:
            self.possible_answers.difference_update(find_fibonacci_numbers(self.biggest_number))

    def deal_with_catalan_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all catalan numbers.

        Call find_catalan_numbers to get all catalan numbers in range.
        :param is_in: boolean whether the number is in catalan sequence or not
        """
        if is_in:
            self.possible_answers.intersection_update(find_catalan_numbers(self.biggest_number))
        else:
            self.possible_answers.difference_update(find_catalan_numbers(self.biggest_number))

    def deal_with_number_order(self, increasing: bool, to_be: bool) -> None:
        """
        Filter possible answers to either keep or remove all numbers with wrong order.

        :param increasing: boolean whether to check is in increasing or decreasing order
        :param to_be: boolean whether the number is indeed in that order
        """
        inc_dec_value = []

        for i in self.possible_answers:
            num = str(i)
            inc = increasing if len(num) > 1 else True

            for j in range(0, len(num) - 1):
                if increasing:
                    inc = True if num[j] <= num[j + 1] else False
                else:
                    inc = True if num[j] >= num[j + 1] else False
                if not inc:
                    break
            if inc:
                inc_dec_value.append(i)

        if to_be:
            self.possible_answers.intersection_update(inc_dec_value)
        else:
            self.possible_answers.difference_update(inc_dec_value)


def calculate_sum(regex, equation) -> int:
    """
    Calculate sum of equation element multipliers find by given regex.

    :param regex: regex string
    :param equation: equation string
    :return: sum of equation element multipliers
    """
    sum = 0
    for match in re.finditer(regex, equation):
        match = match.group(1).replace(' ', '')
        if match != '-0' and match != '+0':
            if match == '' or match == '+':
                sum += 1
            elif match == '-':
                sum -= 1
            else:
                sum += int(match)
    return sum


def normalize_quadratic_equation(equation: str) -> str:
    """
    Normalize equation.

    :param equation: quadratic equation to be normalized
    :return: normalized equation
    """
    if equation.find("=") != -1:
        left_side = equation[:equation.find("=") - 1]
        right_side = equation[equation.find("=") + 2:]
    else:
        left_side = equation
        right_side = ""

    a = calculate_sum(regex_a, left_side) - calculate_sum(regex_a, right_side)
    b = calculate_sum(regex_b, left_side) - calculate_sum(regex_b, right_side)
    c = calculate_sum(regex_c, left_side) - calculate_sum(regex_c, right_side)

    if a < 0 or a == 0 and b < 0:
        a *= -1
        b *= -1
        c *= -1

    equation = ("x2" if a > 0 else "-x2") if abs(a) == 1 else (str(a) + "x2") if a != 0 else ""

    if len(equation) != 0:
        equation += (" + x" if b > 0 else " - x") if abs(b) == 1 else \
            (" - " + str(abs(b)) + "x" if b < 0 else " + " + str(b) + "x") if b != 0 else ""
    else:
        equation += ("x" if b > 0 else "-x") if abs(b) == 1 else (str(b) + "x") if b != 0 else ""

    if len(equation) != 0:
        if c != 0:
            equation += " - " + str(abs(c)) if c < 0 else " + " + str(c)
    else:
        equation = str(abs(c))

    equation += " = 0"

    return equation


def quadratic_equation_solver(equation: str):
    """
    Solve the normalized quadratic equation.

    :param equation: quadratic equation
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return:
    if there are no solutions, return None.
    if there is exactly 1 solution, return it.
    if there are 2 solutions, return them in a tuple, where smaller is first
    all numbers are returned as floats.
    """
    a = calculate_sum(regex_a, equation)
    b = calculate_sum(regex_b, equation)
    c = calculate_sum(regex_c, equation)

    if a == 0 and b != 0:
        return - c / b
    else:
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant > 0:
            x1 = (- b - sqrt(discriminant)) / (2 * a)
            x2 = (- b + sqrt(discriminant)) / (2 * a)
            return (x1, x2) if x1 < x2 else (x2, x1)
        elif discriminant == 0:
            return (- b - sqrt(discriminant)) / (2 * a)
        else:
            return None


def find_primes_in_range(biggest_number: int) -> list:
    """
    Find all primes in range(end inclusive).

    :param biggest_number: all primes in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    :return: list of primes
    """
    nums = [True] * (biggest_number + 1)
    primes = []

    for i in range(2, int(sqrt(biggest_number)) + 1):
        if nums[i] is True:
            for j in range(0, biggest_number):
                index = i * i + j * i
                if index > biggest_number:
                    break
                nums[index] = False

    for i in range(2, len(nums)):
        if nums[i]:
            primes.append(i)

    return primes


def find_composites_in_range(biggest_number: int) -> list:
    """
    Find all composites in range(end inclusive).

    Call find_primes_in_range from this method to get all composites
    :return: list of composites
    :param biggest_number: all composites in range of biggest_number(included)
    """
    composites = []

    primes = find_primes_in_range(biggest_number)

    for i in range(2, biggest_number + 1):
        if i not in primes:
            composites.append(i)

    return composites


def calc_fibonacci(n: int) -> int:
    """
    Calculate n-th Fibonacci number.

    :param n: n-th number
    :return: n-th Fibonacci number
    """
    return n if n < 2 else calc_fibonacci(n - 2) + calc_fibonacci(n - 1)


def find_fibonacci_numbers(biggest_number: int) -> list:
    """
    Find all Fibonacci numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all fibonacci numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Fibonacci_number
    :return: list of fibonacci numbers
    """
    fibonacci = []

    if biggest_number >= 0:
        for i in range(0, biggest_number + 2):
            if calc_fibonacci(i) > biggest_number:
                break
            fibonacci.append(calc_fibonacci(i))

    return fibonacci


def calc_catalan(n: int) -> int:
    """
    Calculate n-th Catalan number.

    :param n: n-th number
    :return: n-th Catalan number
    """
    if n <= 1:
        return 1

    res = 0
    for i in range(n):
        res += calc_catalan(i) * calc_catalan(n - i - 1)

    return res


def find_catalan_numbers(biggest_number: int) -> list:
    """
    Find all Catalan numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all catalan numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Catalan_number
    :return: list of catalan numbers
    """
    catalan = []

    for i in range(0, biggest_number + 1):
        if calc_catalan(i) > biggest_number:
            break
        catalan.append(calc_catalan(i))

    return catalan


if __name__ == '__main__':
    test = Student(45)
    print(test.possible_answers)
    text = 'This number, that you need to guess is composite.'
    print(f"server > student: {text}")
    text = test.decision_branch(text)
    print(f"student > server: {text}")
