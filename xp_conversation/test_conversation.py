import conversation
import random
import math
import re
import string
import pytest

sentence_indices = [["The given number ", "This number ", "Number ", "The aforementioned number "],
                    [["consists of ", "has ", "is made up of "],
                     ["involves ", "includes ", "contains ", "is comprised of "]],
                    [["is ", "occurs to be ", "happens to be "],
                     ["is not ", "isn't ", "doesn't occur to be ", "doesn't happen to be "]]]


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_decision_branch_content():
    student, right, server = conversation.Student(1023), CorrectStudent(1023), Server(1023)
    server_out = server.get_quadratic_equation()
    assert student.decision_branch(server_out) == right.decision_branch(server_out)
    server_out = server.get_amount_of_zeroes_in_binary()
    assert student.decision_branch(server_out) == right.decision_branch(server_out)
    server_out = server.get_amount_of_ones_in_binary()
    assert student.decision_branch(server_out) == right.decision_branch(server_out)
    server_out = server.get_random_dec_number()
    assert student.decision_branch(server_out) == right.decision_branch(server_out)
    server_out = server.get_random_hex_number()
    assert student.decision_branch(server_out) == right.decision_branch(server_out)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_decision_branch_sequence():
    student, right, server = conversation.Student(1023), CorrectStudent(1023), Server(1023)
    server_out = server.is_composite()
    assert student.decision_branch(server_out) == right.decision_branch(server_out)
    server_out = server.is_prime()
    assert student.decision_branch(server_out) == right.decision_branch(server_out)
    server_out = server.is_in_fibonacci_sequence()
    assert student.decision_branch(server_out) == right.decision_branch(server_out)
    server_out = server.is_in_catalan_sequence()
    assert student.decision_branch(server_out) == right.decision_branch(server_out)
    server_out = server.get_order()
    assert student.decision_branch(server_out) == right.decision_branch(server_out)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_number_of_zeroes_to_possible_solutions():
    student, right = conversation.Student(1023), CorrectStudent(1023)
    for i in range(9):
        student.number_of_zeroes_to_possible_solutions(i)
        right.number_of_zeroes_to_possible_solutions(i)
        assert student.possible_answers == right.possible_answers


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_number_of_ones_to_possible_solutions():
    student, right = conversation.Student(1023), CorrectStudent(1023)
    for i in range(10):
        student.number_of_ones_to_possible_solutions(i)
        right.number_of_ones_to_possible_solutions(i)
        assert student.possible_answers == right.possible_answers


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_deal_with_primes():
    student, right = conversation.Student(1023), CorrectStudent(1023)
    for i in range(2):
        student.deal_with_primes(bool(i))
        right.deal_with_primes(bool(i))
        assert student.possible_answers == right.possible_answers


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_deal_with_composites():
    student, right = conversation.Student(1023), CorrectStudent(1023)
    for i in range(2):
        student.deal_with_composites(bool(i))
        right.deal_with_composites(bool(i))
        assert student.possible_answers == right.possible_answers


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_deal_with_random_dec_value():
    student, right = conversation.Student(1023), CorrectStudent(1023)
    for i in range(10):
        student.deal_with_random_dec_value(str(i))
        right.deal_with_random_dec_value(str(i))
        assert student.possible_answers == right.possible_answers


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_deal_with_random_hex_value():
    student, right = conversation.Student(1023), CorrectStudent(1023)
    for i in range(16):
        student.deal_with_random_hex_value(hex(i)[2:])
        right.deal_with_random_hex_value(hex(i)[2:])
        assert student.possible_answers == right.possible_answers


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_deal_with_quadratic_equation():
    student, right, server = conversation.Student(1023), CorrectStudent(1023), Server(1023)
    for i in range(10):
        sentence = server.get_quadratic_equation()
        for start in sentence_indices[0]:
            if sentence.startswith(start):
                sentence = sentence.replace(start, '')
                break
        student.deal_with_quadratic_equation(
            re.findall(r'"(.+)"', sentence)[0], 'times' in sentence,
            re.findall(r'(-?\d+\.\d{4})', sentence)[0], 'bigger' in sentence)
        right.deal_with_quadratic_equation(
            re.findall(r'"(.+)"', sentence)[0], 'times' in sentence,
            re.findall(r'(-?\d+\.\d{4})', sentence)[0], 'bigger' in sentence)
        assert student.possible_answers == right.possible_answers


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_deal_with_fibonacci_sequence():
    student, right = conversation.Student(1023), CorrectStudent(1023)
    for i in range(2):
        student.deal_with_fibonacci_sequence(bool(i))
        right.deal_with_fibonacci_sequence(bool(i))
        assert student.possible_answers == right.possible_answers


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_deal_with_catalan_sequence():
    student, right = conversation.Student(1023), CorrectStudent(1023)
    for i in range(2):
        student.deal_with_catalan_sequence(bool(i))
        right.deal_with_catalan_sequence(bool(i))
        assert student.possible_answers == right.possible_answers


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_and_possible_answers():
    student = conversation.Student(1023)
    random_set1 = set([random.randint(0, 100) for _ in range(100)])
    random_set2 = [random.randint(0, 100) for _ in range(100)]
    student.possible_answers = random_set1
    student.and_possible_answers(random_set2)
    assert student.possible_answers == student.possible_answers & set(random_set2)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_exclusion_possible_answers():
    student = conversation.Student(1023)
    random_set1 = set([random.randint(0, 100) for _ in range(100)])
    random_set2 = [random.randint(0, 100) for _ in range(100)]
    student.possible_answers = random_set1
    student.exclusion_possible_answers(random_set2)
    assert student.possible_answers == student.possible_answers - set(random_set2)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_quadratic_equation_solver():
    for a in range(-10, 10):
        for b in range(-10, 10):
            for c in range(-10, 10):
                try:
                    assert conversation.quadratic_equation_solver(a, b, c) == quadratic_equation_solver(a, b, c)
                except ValueError:
                    pass

                except ZeroDivisionError:
                    pass


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_find_primes_in_range():
    random_int = random.randint(5000, 10000)
    assert conversation.find_primes_in_range(random_int) == find_primes_in_range(random_int)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_find_composites_in_range():
    random_int = random.randint(5000, 10000)
    assert conversation.find_composites_in_range(random_int) == find_composites_in_range(random_int)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_find_fibonacci_numbers():
    random_int = random.randint(5000, 10000)
    assert conversation.find_fibonacci_numbers(random_int) == find_fibonacci_numbers(random_int)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_find_catalan_numbers():
    random_int = random.randint(5000, 10000)
    assert conversation.find_catalan_numbers(random_int) == find_catalan_numbers(random_int)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_deal_with_number_order():
    student, right = conversation.Student(1023), CorrectStudent(1023)
    for i in range(2):
        for j in range(2):
            student.deal_with_number_order(bool(i), bool(j))
            right.deal_with_number_order(bool(i), bool(j))
            assert student.possible_answers == right.possible_answers


class CorrectStudent:
    def __init__(self, biggest_number: int):
        self.biggest_number = biggest_number
        self.possible_answers = set([x for x in range(biggest_number + 1)])

    def decision_branch(self, sentence: str):
        for start in sentence_indices[0]:
            if sentence.startswith(start):
                sentence = sentence.replace(start, '')
                break
        if any(sentence.startswith(x) for x in sentence_indices[1][0]):
            if 'binary' in sentence:
                if any(x in sentence for x in ['zero', 'zeroes']):
                    self.number_of_zeroes_to_possible_solutions(int(re.findall(r'(\d)', sentence)[0]))
                if any(x in sentence for x in ['one', 'ones']):
                    self.number_of_ones_to_possible_solutions(int(re.findall(r'(\d)', sentence)[0]))
        elif any(sentence.startswith(x) for x in sentence_indices[1][1]):
            if 'decimal' in sentence:
                self.deal_with_random_dec_value(re.findall(r'"(\d)"', sentence)[0])
            if 'hex' in sentence:
                self.deal_with_random_hex_value(re.findall(r'"(.)"', sentence)[0])
            if 'quadratic' in sentence:
                self.deal_with_quadratic_equation(re.findall(r'"(.+)"', sentence)[0], 'times' in sentence,
                                                  re.findall(r'(-?\d+\.\d{4})', sentence)[0],
                                                  'bigger' in sentence)
        elif any(sentence.startswith(x) for x in sentence_indices[2][1]):
            if "prime" in sentence:
                self.deal_with_primes(False)
            if "composite" in sentence:
                self.deal_with_composites(False)
            if "fibonacci" in sentence:
                self.deal_with_fibonacci_sequence(False)
            if "catalan" in sentence:
                self.deal_with_catalan_sequence(False)
            if 'order' in sentence:
                self.deal_with_number_order('increasing' in sentence, False)
        elif any(sentence.startswith(x) for x in sentence_indices[2][0]):
            if "prime" in sentence:
                self.deal_with_primes(True)
            if "composite" in sentence:
                self.deal_with_composites(True)
            if "fibonacci" in sentence:
                self.deal_with_fibonacci_sequence(True)
            if "catalan" in sentence:
                self.deal_with_catalan_sequence(True)
            if 'order' in sentence:
                self.deal_with_number_order('increasing' in sentence, True)

        new_round = list(sorted(self.possible_answers))
        return f'Possible answers are {new_round}.' if new_round.__len__() > 1 else f'The number I needed to guess was {list(new_round)[0]}.'

    def number_of_zeroes_to_possible_solutions(self, amount_of_zeroes: int):
        self.helper_number_of_ones_and_zeroes('0', amount_of_zeroes)

    def number_of_ones_to_possible_solutions(self, amount_of_ones: int):
        self.helper_number_of_ones_and_zeroes('1', amount_of_ones)

    def helper_number_of_ones_and_zeroes(self, what_to_check: str, count: int):
        self.and_possible_answers(
            [x for x in range(self.biggest_number + 1) if bin(x).replace('0b', '').count(what_to_check) == count])

    def deal_with_primes(self, is_prime: bool):
        self.and_possible_answers(
            find_primes_in_range(self.biggest_number)) if is_prime else self.exclusion_possible_answers(
            find_primes_in_range(self.biggest_number))

    def deal_with_composites(self, is_composite: bool):
        self.and_possible_answers(
            find_composites_in_range(self.biggest_number)) if is_composite else self.exclusion_possible_answers(
            find_composites_in_range(self.biggest_number))

    def deal_with_random_dec_value(self, decimal_value: str):
        self.and_possible_answers(
            [x for x in range(self.biggest_number + 1) if decimal_value in str(x)])

    def deal_with_random_hex_value(self, hex_value: str):
        self.and_possible_answers(
            [x for x in range(self.biggest_number + 1) if hex_value in hex(x).replace('0x', '')])

    def deal_with_quadratic_equation(self, equation: str, to_multiply: bool, multiplicative: float, is_bigger: bool):
        a = b = c = 0
        last = '+'
        side = False
        for x in equation.split():
            if re.match(r'(\d+\w\^2)', x):
                a += (int(x[:-3]) if last in ['+', '='] else -int(x[:-3])) * (-1 if side else 1)
            elif re.match(r'(\d+\D$)', x):
                b += (int(x[:-1]) if last in ['+', '='] else -int(x[:-1])) * (-1 if side else 1)
            elif re.match(r'(\d+$)', x):
                c += (int(x) if last in ['+', '='] else -int(x)) * (-1 if side else 1)

            side = side or x == '='
            last = x
        g = float(max(quadratic_equation_solver(a, b, c)) if is_bigger else min(quadratic_equation_solver(a, b, c)))
        if to_multiply:
            g *= float(multiplicative)
        else:
            g /= float(multiplicative)
        self.deal_with_random_dec_value(str(round(g)))

    def deal_with_fibonacci_sequence(self, is_in: bool):
        self.and_possible_answers(
            find_fibonacci_numbers(self.biggest_number)) if is_in else self.exclusion_possible_answers(
            find_fibonacci_numbers(self.biggest_number))

    def deal_with_catalan_sequence(self, is_in: bool):
        self.and_possible_answers(
            find_catalan_numbers(self.biggest_number)) if is_in else self.exclusion_possible_answers(
            find_catalan_numbers(self.biggest_number))

    def deal_with_number_order(self, increasing: bool, to_be: bool):
        self.possible_answers = set(x for x in self.possible_answers if (
            ''.join(sorted(str(x), reverse=increasing is not True)) == str(x) if to_be else ''.join(
                sorted(str(x), reverse=increasing is not True)) != str(x)))

    def and_possible_answers(self, update: list):
        self.possible_answers = set(self.possible_answers) & set(update)

    def exclusion_possible_answers(self, update: list):
        self.possible_answers = set(self.possible_answers) - set(update)


def quadratic_equation_solver(a: int, b: int, c: int):
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    # find two solutions
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    return x1, x2


def find_primes_in_range(biggest_number: int):
    return [num for num in range(2, biggest_number + 1) if not any((num % i) == 0 for i in range(2, num))]


def find_composites_in_range(biggest_number: int):
    primes = find_primes_in_range(biggest_number)
    return [num for num in range(2, biggest_number + 1) if num not in primes]


def find_fibonacci_numbers(biggest_number: int):
    if biggest_number == 0:
        return [0]
    fibonacci_numbers = [0, 1]
    while True:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
        if fibonacci_numbers[-1] > biggest_number:
            return fibonacci_numbers[:-1]


def find_catalan_numbers(biggest_number: int):
    if biggest_number == 0:
        return []
    if biggest_number == 1:
        return [1]
    catalan = [1, 1]
    i = 2
    # Fill entries in catalan[] using recursive formula
    while True:
        catalan.append(0)
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i - j - 1]
        if catalan[-1] > biggest_number:
            return catalan[:-1]
        i += 1


class Server:
    def __init__(self, biggest_number: int):
        self.biggest_number = biggest_number
        self.number = random.randint(0, biggest_number + 1)  # generating a number for student to guess

    def get_amount_of_zeroes_in_binary(self):
        total = bin(self.number).replace('0b', '').count("0")
        return random.choice(sentence_indices[0]) + random.choice(
            sentence_indices[1][0]) + f'''{total} {'zero' if total == 1 else 'zeroes'} in it's binary form.'''

    def get_amount_of_ones_in_binary(self):
        total = bin(self.number).replace('0b', '').count("1")
        return random.choice(sentence_indices[0]) + random.choice(
            sentence_indices[1][0]) + f'''{total} {'one' if total == 1 else 'ones'} in it's binary form.'''

    def get_random_hex_number(self):
        return random.choice(sentence_indices[0]) + random.choice(
            sentence_indices[1][1]) + f'''hex value: "{random.choice(hex(self.number).replace('0x', ''))}".'''

    def get_random_dec_number(self):
        return random.choice(sentence_indices[0]) + random.choice(
            sentence_indices[1][1]) + f'''decimal value: "{random.choice(str(self.number))}".'''

    def is_prime(self):
        return random.choice(sentence_indices[0]) + random.choice(
            sentence_indices[2][0 if self.number in find_primes_in_range(self.biggest_number) else 1]) + "prime."

    def is_composite(self):
        return random.choice(sentence_indices[0]) + random.choice(
            sentence_indices[2][
                0 if self.number in find_composites_in_range(self.biggest_number) else 1]) + "composite."

    def is_in_fibonacci_sequence(self):
        return random.choice(sentence_indices[0]) + random.choice(
            sentence_indices[2][
                0 if self.number in find_fibonacci_numbers(self.biggest_number) else 1]) + "in fibonacci sequence."

    def is_in_catalan_sequence(self):
        return random.choice(sentence_indices[0]) + random.choice(
            sentence_indices[2][
                0 if self.number in find_catalan_numbers(self.biggest_number) else 1]) + "in catalan sequence."

    def get_order(self):
        increasing = bool(random.getrandbits(1))
        return random.choice(sentence_indices[0]) + random.choice(
            sentence_indices[2][0 if ''.join(sorted(str(self.number), reverse=increasing is not True)) == str(
                self.number) else 1]) + f"in {'increasing' if increasing else 'decreasing'} order."

    @staticmethod
    def create_random_list_with_sum_n(n: int):
        stack = [random.randint(-100, 100) for i in range(random.randint(0, 5))]
        stack.append(n - sum(stack))
        return stack

    def get_quadratic_equation(self):
        x_value = int(random.choice(str(self.number)))
        while True:  # b**2 > 4*a*c
            b, a, c = random.randint(1, 100) * -1 if bool(random.getrandbits(1)) else 1, random.randint(1, 100), \
                      random.randint(1, 100)

            if bool(random.getrandbits(1)):
                a *= -1
            else:
                c *= -1

            if (b ** 2) - (4 * a * c) >= 0 and (b ** 2 - 4 * a * c) ** 0.5 == int((b ** 2 - 4 * a * c) ** 0.5):
                x1, x2 = quadratic_equation_solver(a, b, c)
                variable = random.choice(string.ascii_uppercase)
                bigger = bool(random.getrandbits(1))
                x_result = max(x1, x2) if bigger else min(x1, x2)
                equation = [f'{"-" if x < 0 else "+"} {abs(x)}{l} ' for j, l in
                            [(a, f"{variable}^2"), (b, variable), (c, '')] for x in
                            self.create_random_list_with_sum_n(j)]
                random.shuffle(equation)
                position = random.randint(0, equation.__len__())
                equation = ''.join([
                    f"{x}= " if j == position else f"{x.replace('- ', '').replace('+', '-')}" if j == position + 1 else
                    f"{x.replace('-', '/').replace('+', '-').replace('/', '+')}" if j > position else f"{x}"
                    for j, x in enumerate(equation)])
                if equation.endswith('= '):
                    equation += '0'
                if equation.startswith('+ '):
                    equation = equation[2:]
                if '=' not in equation:
                    equation += '= 0'
                equation = equation.strip()
                return random.choice(sentence_indices[0]) + random.choice(sentence_indices[1][1]) \
                       + ((f'''a digit where {"{0:.4f}".format(x_value / x_result)} times the {'bigger' if bigger
                else 'smaller'} result for the following quadratic equation:"{equation}" and is rounded to closest integer.''')
                          if bool(random.getrandbits(1)) or x_value == 0 else f'''a digit, where the {'bigger' if bigger
                else 'smaller'} result for the following quadratic equation:"{equation}" what is divided by {"{0:.4f}".format(1 / (x_value / x_result))} and rounded to closest integer.''')
