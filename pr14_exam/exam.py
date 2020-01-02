"""Exam."""


def swap_items(dic: dict) -> dict:
    """
    Given a dictionary return a new dictionary where keys and values are swapped.

    If duplicate keys in the new dictionary exist, leave the first one.
    {"a": 1, "b": 2, "c": 3} => {1: "a", 2: "b", 3: "c"}
    {"Morning": "Good", "Evening": "Good"} => {"Good": "Morning"}
    :param dic: original dictionary
    
    :return: dictionary where keys and values are swapped
    """
    out = {}
    for key, value in dic.items():
        if not out.get(value):
            out[value] = key
    return out



def find_divisors(number) -> list:
    """
    The task is to find all the divisors for given number in range to the given number's value.

    Divisor - a number that divides evenly into another number.
    Return list of given number divisors in ascending order.
    NB! Numbers 1 and number itself must be excluded if there are more divisors
    than 1 and number itself!
    print(find_divisors(138))  # > [2, 3, 6, 23, 46, 69]
    (3) > [1, 3]
    :param number: int
    :return: list of number divisors
    """
    if number < 2:
        return [number]
    out = []
    for i in range(1, number + 1):
        if not number % i:
            out.append(i)
    return out if len(out) == 2 else out[1:-1]


def sum_of_multiplies(first_num, second_num, limit) -> int:
    """
    The task is to find all the multiplies of each given of two numbers within the limit.

    Then, find the sum of those multiplies.
    print(sum_of_multiplies((3, 5, 20))  # => 98
    :param first_num: first number
    :param second_num: second number
    :param limit: limit
    :return: sum of multiplies
    """
    sum = 0
    for i in range(1, limit + 1):
        if not i % first_num or not i % second_num:
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
    odds = 0
    evens = 0
    for number in numbers:
        if number:
            if number % 2:
                odds += 1
            else:
                evens += 1
    return f"ODDS: {odds}\nEVENS: {evens}"


def sum_between_25(numbers: list) -> int:
    """
    Return the sum of the numbers in the array.

    Ignore sections of numbers starting with a 2 and extending to the next 5.
    print(sum_between_25([2, 1, 7, 3, 5]))  # => 0
    print(sum_between_25([1, 2, 3, 4, 5, 6, 2, 8, 9, 5, 1]))  # => 8
    :param numbers: list
    :return:
    """
    sum = 0
    include = False
    for num in numbers:
        if include:
            if num == 5:
                include = False
            else:
                sum += num
        else:
            if num == 2:
                include = True
            elif num == 5:
                include = False

    return sum


def transcribe(dna_strand: str):
    """
    Write a function that returns a transcribed RNA strand from the given DNA strand.

    That is formed by replacing each nucleotide(character) with its complement: G => C, C => G, T => A, A => U
    Return None if it is not possible to transcribe a DNA strand
    print(transcribe("ACGTGGTCTTAA"))  # => "UGCACCAGAAUU"
    print(transcribe("gcu"))  # => None
    :param dna_strand: original DNA strand
    :return: transcribed RNA strand in the uppercase or None
    """
    out = ""
    dna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    for char in dna_strand:
        if not dna.get(char.upper()):
            return None
        else:
            out += dna[char.upper()]
    return out


def union_of_dict(d1: dict, d2: dict):
    """
    Given two dictionaries return dictionary that has all the key-value pairs that are the same in given dictionaries.

    union_of_dict({"a": 1, "b": 2, "c":3}, {"a": 1, "b": 42}) ==> {"a": 1}
    union_of_dict({}, {"bar": "foo"}) => {}
    """
    out = {}
    for key, value in d1.items():
        if key in d2 and d2[key] == value:
            out[key] = value
    return out


def reserve_list(input_strings: list) -> list:
    """
    Given list of strings, return new reversed list where each list element is reversed too.

    Do not reverse strings followed after element "python". If element is "java" -
    reverse mode is on again.
    P.S - "python" and "java" are not being reversed
    print(reserve_list(['apple', 'banana', 'onion']))  # -> ['noino', 'ananab', 'elppa']
    print(reserve_list(['lollipop', 'python', 'candy']))  #  -> ['candy', 'python', 'popillol']
    print(reserve_list(['sky', 'python', 'candy', 'java', 'fly']))  #  -> ['ylf', 'java', 'candy', 'python', 'yks']
    print(reserve_list(['sky', 'python', 'java', 'candy']))  #  -> ['ydnac', 'java', 'python', 'yks']
    :param input_strings: list of strings
    :return: reversed list
    """
    out = []
    reverse = True
    for string in input_strings:
        if reverse:
            if string != 'python' and string != 'java':
                out.insert(0, string[::-1])
            else:
                out.insert(0, string)
                if string == 'python':
                    reverse = False
                else:
                    reverse = True
        else:
            out.insert(0, string)
            if string == 'python':
                reverse = False
            elif string == 'java':
                reverse = True

    return out


def convert_binary_to_decimal(binary_list: list):
    """
    Extract binary codes of given length from list and convert to decimal numbers.

    [0, 0, 0, 0] => 0.
    [0, 1, 0, 0] => 4.
    :param binary_list: list of 1 and 0 (binary code)
    :return: number converted into decimal system
    """
    decimal = 0
    for i, num in enumerate(binary_list[::-1]):
        decimal += num * 2 ** i
    return decimal


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
    values = pages.split(",")
    out = []

    for value in values:
        if "-" in str(value):
            interval = value.split("-")
            numbers = [int(x) for x in interval]
            numbers.sort()
            for i in range(numbers[0], numbers[1] + 1):
                out.append(i)
        elif len(value):
            out.append(int(value))
    out = list(set(out))
    out.sort()
    return out


def sum_digits(num: int) -> int:
    """
    Return sum of digits recursively.

    #09

    Given a positive number as an integer find and return the sum of digits of the number recursively.
    This function CANNOT contain any while/for loops.

    sum_digits(123) => 6
    sum_digits(19) => 10

    :param num: number (int)
    :return: sum of number's digits
    """
    if not num:
        return 0

    return num % 10 + sum_digits(num // 10)


def multiple_elements(items: list) -> dict:
    """
    Given a list of items (strings), return a dict where key is item (string) and value is count.

    #05

    But you are interested only in items which are present more than once.
    So, items with count 1 should not be in the result.

    multiple_items(['a', 'b', 'a']) => {'a': 2}
    multiple_items(['a', 'b', 'c']) => {}
    multiple_items(['a', 'a', 'c', 'c']) => {'a': 2, 'c': 2}

    :param items:
    :return:
    """
    out = {}
    for item in items:
        if item not in out:
            out[item] = 1
        else:
            out[item] += 1

    out = {k: v for k, v in out.items() if v > 1}
    return out


def double_char(original_string: str) -> str:
    """
    Given a string, return a string where for every char in the original is doubled.

    #02

    double_char("a") => "aa"
    double_char("ab") => "aabb"
    double_char("") => ""

    :param str: string
    :return: string where chars are doubled
    """
    out = ""
    for char in original_string:
        out += char * 2
    return out


def reverse_list(input_strings: list) -> list:
    """
    Reverse the list and elements except for "python" and "java" and everything between.

    #04

    Given list of strings, return new reversed list where each list element is
    reversed too. Do not reverse strings followed after element "python". If element is "java" -
    reverse mode is on again.
    P.S - "python" and "java" are not being reversed

    reverse_list(['apple', 'banana', 'onion']) -> ['noino', 'ananab', 'elppa']
    reverse_list(['lollipop', 'python', 'candy']) -> ['candy', 'python', 'popillol']
    reverse_list(['sky', 'python', 'candy', 'java', 'fly']) -> ['ylf', 'java', 'candy', 'python', 'yks']
    reverse_list(['sky', 'python', 'java', 'candy']) -> ['ydnac', 'java', 'python', 'yks']

    :param input_strings: list of strings
    :return: reversed list
    """
    out = []
    reverse = True
    for string in input_strings:
        if reverse:
            if string != 'python' and string != 'java':
                out.insert(0, string[::-1])
            else:
                out.insert(0, string)
                if string == 'python':
                    reverse = False
                else:
                    reverse = True
        else:
            out.insert(0, string)
            if string == 'python':
                reverse = False
            elif string == 'java':
                reverse = True

    return out


def common_elements(list_a: list, list_b: list) -> list:
    """
    Given two lists, return a list of elements that can be found in both input lists.

    #03

    The elements can be in any order. The result should have no duplicates.

    common_elements([1, 2], [2, 1]) => [1, 2]
    common_elements([1, 2], [2, 2, 2]) => [2]
    common_elements([1, 2], []) => []
    common_elements([1, 2, 3], [3, 4, 5, 3]) => [3]
    :param list_a: list
    :param list_b: list
    :return: list of elements found in list_a and list_b
    """
    return list(set([value for value in list_a if value in list_b]))


def sum_time(time1: tuple, time2: tuple) -> tuple:
    """
    Add two times represented as tuples.

    #01

    Both arguments represent time in format (hours, minutes).
    A tuple with two integers. The input is always correct (you don't have to check that).
    0 <= hours <= 23
    0 <= minutes <= 59

    sum_time((0, 10), (0, 20)) => (0, 30)
    sum_time((12, 30), (0, 40)) => (13, 10)
    sum_time((23, 20), (2, 40)) => (2, 0)

    :param time1: tuple with two integers: hours, minutes
    :param time2: tuple with two integers: hours, minutes
    :return: sum of time1, time2; tuple with two integers: hours, minutes
    """
    minutes = (time1[1] + time2[1]) % 60
    hours = ((time1[0] + time2[0]) + (time1[1] + time2[1]) // 60) % 24
    return (hours, minutes)


# 07. University imitation
class Book:
    """
    Represent book model.

    When printing the book object, it should show the name.
    """

    def __init__(self, name: str):
        """
        Class constructor. Each book has name.

        :param name: book name
        """
        self.name = name

    def __repr__(self):
        """Print book."""
        return self.name


class Student:
    """
    Represent student model.

    When printing the student object, it should be as: "name(gpa):[book1, book2]"
    ( f"{name}({gpa}):{books}" ).
    """

    def __init__(self, name: str, gpa: float):
        """
        Class constructor.

        Each student has name and gpa (Grade Point Average)
        Student also should have a list of books.

        :param name: student's name
        :param gpa: student's gpa
        """
        self.name = name
        self.gpa = gpa
        self.books = []

    def add_book(self, book: Book):
        """
        Add book to student's bag.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self.books.append(book)

    def can_add_book(self, book: Book):
        """
        Check if given book can be added to student's bag.

        The book can be added if it is not already in student's bag.
        :param book: Book
        :return: bool
        """
        return True if book not in self.books else False

    def get_books(self):
        """
        Return a list of all the books.

        :return: list of Book objects
        """
        return self.books

    def __repr__(self):
        """Print Student."""
        return f"{self.name}({self.gpa}):{self.books}"


class University:
    """
    Represent university model.

    When printing the object, it should be shown as: "name:[student1, student2]"
    ( f"{name}:{students}" ) .
    """

    def __init__(self, name: str, gpa_required: float, books_required: int):
        """
        Class constructor.

        Each university has name, gpa_required and books_required. Last two
        are used to define if student can be added to university.

        University should also have a database to keep track of all students.

        :param name: university name
        :param gpa_required: university required gpa
        :param books_required: university required books amount
        """
        self.name = name
        self.gpa_required = gpa_required
        self.books_required = books_required
        self.students = []

    def enrol_student(self, student: Student):
        """
        Enrol new student to university.

        :param student: Student
        Function does not return anything
        """
        if self.can_enrol_student(student):
            self.students.append(student)

    def can_enrol_student(self, student: Student):
        """
        Check if student can be enrolled to university.

        Student can be successfully enrolled if:
            * he/she has required gpa
            * he/she has enough amount of books required
            * he/she is not already enrolled to this university

        :return: bool
        """
        return True if student.gpa >= self.gpa_required and len(student.get_books()) >= self.books_required \
                       and student not in self.get_students() else False

    def unenrol_student(self, student: Student):
        """
        Unenrol student from University.

        Student can be unenrolled if he/she actually studies in this university.
        Function does not return anything
        """
        if student in self.students:
            self.students.remove(student)

    def get_students(self):
        """
        Return a list of all students in current university.

        :return: list of Student objects
        """
        return self.students

    def get_student_highest_gpa(self):
        """
        Return a list of students (student) with the highest gpa.

        :return: list of Student objects
        """
        return [i for i in self.get_students() if i.gpa == max([i.gpa for i in self.get_students()])]

    def get_student_max_books(self):
        """
        Return a list of students (student) with the greatest books amount.

        :return: list of Student objects
        """
        return [i for i in self.get_students() if len(i.get_books()) == max([len(i.get_books()) for i in self.get_students()])]

    def __repr__(self):
        """Print University."""
        return f"{self.name}:{self.get_students()}"


# 08. Troll Hunt
class Troll:
    """Troll."""

    def __init__(self, name, weight, height, health_points, stamina_points):
        """
        Constructor.

        :param name: troll name.
        :param weight: troll weight (t).
        :param height: troll height (m).
        :param health_points: troll health points (hp).
        :param stamina_points: troll stamina points (sp).
        """
        self.name = name
        self.weight = weight
        self.height = height
        self.health_points = health_points
        self.stamina_points = stamina_points

    def __repr__(self):
        """Print Troll."""
        return f"Name: {self.name}, lvl: {self.get_troll_level()}"

    def get_troll_attack_speed(self):
        """
        Get the troll attack speed (1-100), integer.

        The heavier and higher the troll is, the slower it moves.
        The troll speed is calculated using the following formula: 100 / (weight + height).
        Round down.
        Assume that sum of weight and height is always non-negative and smaller or equal to 100.

        EXAMPLE
        --------------------------------------------
        troll weight = 3
        troll height = 20
        then troll speed = 100 / (3 + 20) = 4.347 ~ 4. So the answer is 4.
        --------------------------------------------

        :return: troll attack speed, integer.
        """
        return 100 // (self.weight + self.height)

    def get_troll_attack_power(self):
        """
        Get the troll attack power, integer.

        The heavier and higher the troll is, the stronger it is.
        The troll attack power is just the sum of its weight and height.

        EXAMPLE
        --------------------------------------------
        troll weight = 5
        troll height = 20
        then troll attack power = 5 + 20 = 25
        --------------------------------------------

        :return: troll attack power, integer.
        """
        return self.weight + self.height

    def get_troll_level(self):
        """
        Get the level of the troll (1-5), integer.

        Each troll has a level, which indicates how dangerous it is in combat.
        The troll level mostly depends on its hp, sp, speed and attack power.
        The level of the troll is calculated using the following formula:

        delta = (5 - 1) / (3000 - 500) = 0.0016
        troll_power = (troll health points + troll stamina points + troll attack speed + troll attack power)

        formula: 0.0016 * (troll_power - 3000) + 5, round down

        EXAMPLE
        --------------------------------------------
        troll hp = 500
        troll stamina = 300
        troll atk speed = 4
        troll atk power = 25

        delta = 0.0016
        troll power = (500 + 300 + 4 + 25) = 829

        troll lvl = 0.0016 * (829 - 3000) + 5) = 1.53 ~= 1
        --------------------------------------------

        :return: troll lvl.
        """
        delta = 0.0016
        troll_power = self.health_points + self.stamina_points + \
            self.get_troll_attack_speed() + self.get_troll_attack_power()
        return int(delta * (troll_power - 3000) + 5)

    def get_name(self):
        """
        Getter.

        :return: troll name.
        """
        return self.name

    def get_weight(self):
        """
        Getter.

        :return: troll weight.
        """
        return self.weight

    def get_height(self):
        """
        Getter.

        :return: troll height.
        """
        return self.height

    def get_hp(self):
        """
        Get health points.

        :return: troll hp.
        """
        return self.health_points

    def get_sp(self):
        """
        Get stamina.

        :return: troll sp.
        """
        return self.stamina_points

    # add required method(s) to get string representation: f"Name: {troll name}, lvl: {troll lvl}"


class Hunter:
    """Troll hunter."""

    def __init__(self, attack_power, intelligent: bool = False):
        """
        Constructor.

        :param attack_power: Attack power of the hunter.
        :param intelligent: Says for itself.
        """
        self.attack_power = attack_power
        self.intelligent = intelligent

    def call_for_help(self):
        """
        If the hunter is intelligent, he can call for help.

        Calling for help increases attack power by 10.
        :return:
        """
        if self.is_intelligent():
            self.attack_power += 10

    def get_attack_power(self):
        """
        Getter.

        :return: hunter's atk power.
        """
        return self.attack_power

    def is_intelligent(self):
        """
        Getter.

        :return: is hunter intelligent? Boolean.
        """
        return True if self.intelligent else False


class Mission:
    """Mission."""

    def __init__(self, hunters, troll):
        """
        Constructor.

        :param hunters: list of hunters obj
        :param troll: troll obj
        """
        self.hunters = hunters
        self.troll = troll

    def hunt(self):
        """
        The hunters try to slay down the given troll.

        The hunters succeed if their total attack power is bigger than troll lvl * 300. The troll will become None.
        If their total attack power is smaller than troll lvl * 300, troll kills the most powerful hunter and
        all intelligent hunters call for help.
        If after calling for help total attack power of hunters is still too low, hunters die and the mission is failed.

        If hunters succeed to kill the troll, return true. In other case return false.

        :return: boolean
        """
        if self.get_hunters_power() > self.troll.get_troll_level() * 300:
            self.troll = None
            return True
        else:
            self.hunters.remove(self.get_most_powerful_hunter())
            for hunter in self.hunters:
                if hunter.is_intelligent():
                    hunter.call_for_help()
            if self.get_hunters_power() > self.troll.get_troll_level() * 300:
                self.troll = None
                return True
            else:
                self.hunters = []
                return False

    def get_hunters_power(self):
        """Get all hunters power."""
        hunters_power = 0
        for hunter in self.hunters:
            hunters_power += hunter.get_attack_power()
        return hunters_power

    def get_most_powerful_hunter(self):
        """Get most powerful hunter."""
        return [i for i in self.hunters if i.get_attack_power() == max([i.get_attack_power() for i in self.hunters])][0]

    def set_hunters(self, hunters):
        """
        Setter.

        :param hunters: list of hunters obj
        """
        self.hunters = hunters

    def set_troll(self, troll):
        """
        Setter.

        Check if troll is Troll class obj and set. In other case do not do anything.

        :param troll: Troll class obj
        """
        if isinstance(troll, Troll):
            self.troll = troll

    def get_troll(self):
        """
        Getter.

        :return: troll
        """
        return self.troll


def robot_movement(orders):
    """
    Given a string with robot orders, return the end position and the number of orders executed.

    #06

    The robot knows the following orders:
    - L - turn 90 degrees left
    - R - turn 90 degrees right
    - D - drive 1 step

    There are other orders in the string, but you should ignore those for this exercise.
    In front of an order, there can be a multiplier which indicates how many times the following order is executed.
    For example:
    3D - drives 3 steps
    3L - turns 3 times 90 degree left (when starting heading north, it will then be heading east)
    123D - drives 123 steps
    A - ignore this order
    5A - still ignore (both 5 and A)
    5AD - is the same as just "D"

    The robot starts at (0, 0) heading north. The result should be a tuple in format: (x, y, number of orders executed).
    x grows from west to east, y grows from south to north.

    Examples:

    robot_movement("DDDRDD") => (2, 3, 6)
    robot_movement("RRRLLLL") => (0, 0, 7)
    robot_movement("RRR7L") => (0, 0, 10)
    robot_movement("7A7BD") => (0, 1, 1)

    :param orders:
    :return:
    """
    directions = {
        "S": (0, -1),
        "N": (0, 1),
        "E": (1, 0),
        "W": (-1, 0)
    }
    cur_pos_x = 0
    cur_pos_y = 0
    cur_dir = "N"
    number = ""
    steps = 0

    for order in orders:
        if order.isnumeric():
            number += order
        else:
            if len(number):
                if order in ("L", "R"):
                    for i in range(0, int(number) % 4):
                        cur_dir = new_dir(cur_dir, order)
                    steps += int(number)
                elif order == "D":
                    cur_pos_x += directions[cur_dir][0] * int(number)
                    cur_pos_y += directions[cur_dir][1] * int(number)
                    steps += int(number)
                number = ""
            else:
                if order in ("L", "R"):
                    cur_dir = new_dir(cur_dir, order)
                    steps += 1
                elif order == "D":
                    cur_pos_x += directions[cur_dir][0]
                    cur_pos_y += directions[cur_dir][1]
                    steps += 1

    return (cur_pos_x, cur_pos_y, steps)


def new_dir(cur_dir: str, turn: str) -> str:
    """Calculate new direction."""
    dirs = ["N", "E", "S", "W"]
    cur_pos = dirs.index(cur_dir)
    if turn == 'L':
        new_pos = 3 if cur_pos == 0 else cur_pos - 1
    elif turn == 'R':
        new_pos = 0 if cur_pos == 3 else cur_pos + 1
    else:
        return cur_dir
    return dirs[new_pos]


if __name__ == '__main__':
    """
    if d2.get(key) on  False ka juhul, kui d2[key] == 0 või "" või [] jne
    key in d2 ütleb seda, kas seal on selline võti (väärtusel pole vahet)
    my_dict[key] = my_dict.get(key, 0) + 1
    Kui key puudub, tekitab key ja paneb väärtuseks 0, kui on key olemas lisab +1 väärtusele
    """
    print(robot_movement("DDDRDD"))  # => (2, 3, 6)
    print(robot_movement("RRRLLLL"))  # => (0, 0, 7)
    print(robot_movement("RRR7L"))  # => (0, 0, 10)
    print(robot_movement("7A7BD"))  # => (0, 1, 1)
