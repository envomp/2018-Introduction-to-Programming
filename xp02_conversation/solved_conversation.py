import random
import re
import math

sentence_indices = [["The given number ", "This number ", "Number ", "The aforementioned number ",
                     "This number, that you need to guess ", "This number that we are speaking of right now "],
                    [["consists of ", "has ", "is made up of "],
                     ["involves ", "includes ", "contains ", "is comprised of "]],
                    [["is ", "occurs to be ", "happens to be ", "is without a doubt ", "is with no hesitation "],
                     ["is not ", "isn't ", "doesn't occur to be ", "doesn't happen to be ", "does not occur to be ",
                      "does not happen to be "]]]


class Student:
    def __init__(self, biggest_number: int):
        self.biggest_number = biggest_number
        self.possible_answers = set([x for x in range(biggest_number + 1)])

    def decision_branch(self, sentence: str):
        new_sentences = []
        for start in sentence_indices[0]:
            if sentence.startswith(start):
                new_sentences.append(sentence.replace(start, ''))
        sentence = min(new_sentences, key=len)
        if any(sentence.startswith(x) for x in sentence_indices[1][0]):
            if 'binary' in sentence:
                if any(x in sentence for x in ['zero', 'zeroes']):
                    self.deal_with_number_of_zeroes(int(re.findall(r'(\d)', sentence)[0]))
                if any(x in sentence for x in ['one', 'ones']):
                    self.deal_with_number_of_ones(int(re.findall(r'(\d)', sentence)[0]))
        elif any(sentence.startswith(x) for x in sentence_indices[1][1]):
            if 'decimal' in sentence:
                self.deal_with_dec_value(re.findall(r'"(\d)"', sentence)[0])
            if 'hex' in sentence:
                self.deal_with_hex_value(re.findall(r'"(.)"', sentence)[0])
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

    def deal_with_number_of_zeroes(self, amount_of_zeroes: int):
        self.helper_number_of_ones_and_zeroes('0', amount_of_zeroes)

    def deal_with_number_of_ones(self, amount_of_ones: int):
        self.helper_number_of_ones_and_zeroes('1', amount_of_ones)

    def helper_number_of_ones_and_zeroes(self, what_to_check: str, count: int):
        self.intersect_possible_answers(
            [x for x in range(self.biggest_number + 1) if bin(x).replace('0b', '').count(what_to_check) == count])

    def deal_with_primes(self, is_prime: bool):
        self.intersect_possible_answers(
            find_primes_in_range(self.biggest_number)) if is_prime else self.exclude_possible_answers(
            find_primes_in_range(self.biggest_number))

    def deal_with_composites(self, is_composite: bool):
        self.intersect_possible_answers(
            find_composites_in_range(self.biggest_number)) if is_composite else self.exclude_possible_answers(
            find_composites_in_range(self.biggest_number))

    def deal_with_dec_value(self, decimal_value: str):
        self.intersect_possible_answers(
            [x for x in range(self.biggest_number + 1) if decimal_value in str(x)])

    def deal_with_hex_value(self, hex_value: str):
        self.intersect_possible_answers(
            [x for x in range(self.biggest_number + 1) if hex_value in hex(x).replace('0x', '')])

    def deal_with_quadratic_equation(self, equation: str, to_multiply: bool, multiplicative: float, is_bigger: bool):
        f = quadratic_equation_solver(normalize_quadratic_equation(equation))
        if type(f) == float:
            g = f
        else:
            g = float(max(f) if is_bigger else min(f))
        if to_multiply:
            g *= float(multiplicative)
        else:
            g /= float(multiplicative)
        self.deal_with_dec_value(str(round(g)))

    def deal_with_fibonacci_sequence(self, is_in: bool):
        self.intersect_possible_answers(
            find_fibonacci_numbers(self.biggest_number)) if is_in else self.exclude_possible_answers(
            find_fibonacci_numbers(self.biggest_number))

    def deal_with_catalan_sequence(self, is_in: bool):
        self.intersect_possible_answers(
            find_catalan_numbers(self.biggest_number)) if is_in else self.exclude_possible_answers(
            find_catalan_numbers(self.biggest_number))

    def deal_with_number_order(self, increasing: bool, to_be: bool):
        self.possible_answers = set(x for x in self.possible_answers if (
            ''.join(sorted(str(x), reverse=increasing is not True)) == str(x) if to_be else ''.join(
                sorted(str(x), reverse=increasing is not True)) != str(x)))

    def intersect_possible_answers(self, update: list):
        self.possible_answers = set(self.possible_answers) & set(update)

    def exclude_possible_answers(self, update: list):
        self.possible_answers = set(self.possible_answers) - set(update)

    def deal_with_fractal_calculation(self, json):
        pass


regex_a = r'(([-]\s*)?(\d+)?)?x2(?![0-9])'
regex_b = r'(([-]\s*)?(\d+)?)?x1?(?![0-9])'
regex_c = r'(?<!x)(([-]\s*)?(\d+))(?![x0-9])'


def get_abc(eq):
    parts = eq.split("=")
    vals = [0, 0, 0]
    for parti, part in enumerate(parts):
        regexs = (regex_a, regex_b, regex_c)
        for i, reg in enumerate(regexs):
            for match in re.finditer(reg, part):
                val = match.group(1)
                val = val.replace(" ", "")
                try:
                    valint = int(val)
                    if parti == 1: valint *= -1
                    vals[i] += valint
                except:
                    if val == "":
                        vals[i] = 1
                    if val == "-":
                        vals[i] = -1

    # print(vals)
    if (vals[0] < 0) or (vals[0] == 0 and vals[1] < 0) or ((vals[0], vals[1]) == (0, 0) and vals[2] < 0):
        vals = [-v for v in vals]
    return vals


def normalize_quadratic_equation(eq):
    xs = ("x2", "x", "")
    vals = get_abc(eq)

    if vals[0] == 0 and vals[1] == 0 and vals[2] == 0:
        return "0 = 0"

    result = ""
    for i in range(len(vals)):
        if vals[i] == 0:
            continue
        if vals[i] > 0:
            if len(result) > 0:
                result += " + "
                # result += f"{vals[i] if vals[i] != 1 else ''}{xs[i]}"
        elif vals[i] < 0:
            if len(result) > 0:
                result += " - "
            else:
                result += "-"
        if xs[i] == "" and abs(vals[i]) == 1:
            result += "1"
        else:
            result += f"{abs(vals[i]) if abs(vals[i]) != 1 else ''}{xs[i]}"
    result += " = 0"
    return result


def quadratic_equation_solver_1(a: int, b: int, c: int):
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    # find two solutions
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    return x1, x2


def quadratic_equation_solver(eq):
    a, b, c = get_abc(eq)
    if a == 0:
        if c == 0:
            return 0
            # return "x = 0"
        else:
            if b == 0:
                return None
            x = -c / b
            return x
            # return "x = {:.3}".format(x)
    else:
        if (b * b - 4 * a * c) < 0:
            return None
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 / a
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 / a
    # print(x1, x2)
    if abs(x1 - x2) < 0.0001:
        return x1
        # return "x = {:.2}".format(x1)
    else:
        return [min(x1, x2), max(x1, x2)]
        # return "x1 = {:.2}, x2 = {:.2}".format(min(x1, x2), max(x1, x2))


def find_primes_in_range(biggest_number: int):
    return [num for num in range(2, biggest_number + 1) if
            not any((num % i) == 0 for i in range(2, int(math.sqrt(num)) + 1))]


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
            sentence_indices[1][0]) + f'''{total} {'zero' if total == 1 else 'zeroes'} in its binary form.'''

    def get_amount_of_ones_in_binary(self):
        total = bin(self.number).replace('0b', '').count("1")
        return random.choice(sentence_indices[0]) + random.choice(
            sentence_indices[1][0]) + f'''{total} {'one' if total == 1 else 'ones'} in its binary form.'''

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
                x1, x2 = quadratic_equation_solver_1(a, b, c)
                variable = "x"
                bigger = bool(random.getrandbits(1))
                x_result = max(x1, x2) if bigger else min(x1, x2)
                equation = [f'{"-" if x < 0 else "+"} {abs(x)}{l} ' for j, l in
                            [(a, f"{variable}2"), (b, variable), (c, '')] for x in
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
                else 'smaller'} result for the following quadratic equation:"{equation}" is rounded to closest integer.''')
                          if bool(random.getrandbits(1)) or x_value == 0 else f'''a digit, where the {'bigger' if bigger
                else 'smaller'} result for the following quadratic equation:"{equation}" is divided by {"{0:.4f}".format(1 / (x_value / x_result))} and is rounded to closest integer.''')


def conversation_init():
    student = Student(100)
    server = Server(100)
    server_functions = [server.get_quadratic_equation, server.get_amount_of_zeroes_in_binary,
                        server.get_amount_of_ones_in_binary, server.get_random_dec_number, server.get_random_hex_number,
                        server.is_composite, server.is_prime, server.is_in_fibonacci_sequence,
                        server.is_in_catalan_sequence, server.get_order]
    while True:
        server_call = random.choice(server_functions)()
        print('server > student:', server_call)
        student_result = student.decision_branch(server_call)
        print('student > server:', student_result)
        if server.number not in student.possible_answers:
            print('server > student: You made a mistake... It is a humane thing to do.')
            break
        if re.compile(r'(\d+)\.').search(student_result):
            if int(re.compile(r'(\d+)\.').search(student_result).group()[:-1]) == server.number:
                print('server > student: You are correct.')
                break


if __name__ == '__main__':
    for i in range(10):
        conversation_init()
        print()
