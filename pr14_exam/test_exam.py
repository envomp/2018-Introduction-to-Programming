import exam
import pytest
import string
import random


def test_swap_items():
    data_1 = [
        [{1: "a", 2: "b", 3: "c"}, {"a": 1, "b": 2, "c": 3}],
        [{1: "a", 3: "c", "2": "b"}, {"a": 1, "b": "2", "c": 3}],
        [{"-33": 33, -21: 12}, {12: -21, 33: "-33"}],
        [{"Ross The Painter": "Bob"}, {"Bob": "Ross The Painter"}],
        [{1: "a", 2: "first"}, {"a": 1, "first": 2}],
        [{1: "a", "1": "b", 3: "c"}, {"a": 1, "b": "1", "c": 3}],
        [{"Good": "Morning"}, {"Morning": "Good"}],
        [{None: "a", 2: None}, {"a": None, None: 2}],
        [{False: True, True: False}, {True: False, False: True}],
        [{}, {}]
    ]

    for i in range(data_1.__len__()):
        assert exam.swap_items(data_1[i][0]) == data_1[i][1]


def test_find_divisors():
    """Normal case, where 1 and input number should not be present."""
    assert exam.find_divisors(138) == [2, 3, 6, 23, 46, 69]
    assert exam.find_divisors(254) == [2, 127]
    assert exam.find_divisors(1) == [1]
    assert exam.find_divisors(3) == [1, 3]
    assert exam.find_divisors(1028) == [2, 4, 257, 514]


def test_sum_of_multiplies():
    """Normal case when all three numbers are positive. Wider range."""
    assert exam.sum_of_multiplies(3, 5, 20) == 98
    assert exam.sum_of_multiplies(10, 15, 20) == 45
    assert exam.sum_of_multiplies(4, 8, 245) == 7564
    assert exam.sum_of_multiplies(2, 3, 1) == 0
    assert exam.sum_of_multiplies(30, 32, 10258) == 3281970


def test_count_odds_and_evens():
    """Has both odd and even numbers."""
    numbers = [25, 1, 6, 20, 47, 18, 66, 74]
    assert exam.count_odds_and_evens(numbers) == __solver_count_odds_and_evens(numbers)
    numbers = [2, 4, 6]
    assert exam.count_odds_and_evens(numbers) == __solver_count_odds_and_evens(numbers)
    numbers = [3, 5, 7]
    assert exam.count_odds_and_evens(numbers) == __solver_count_odds_and_evens(numbers)
    numbers = [0, 0, 0]
    assert exam.count_odds_and_evens(numbers) == __solver_count_odds_and_evens(numbers)
    numbers = []
    assert exam.count_odds_and_evens(numbers) == __solver_count_odds_and_evens(numbers)


def __solver_count_odds_and_evens(numbers):
    s = ['odds' if i % 2 != 0 else 'evens' for i in numbers if i != 0]
    return f"ODDS: {s.count('odds')}\nEVENS: {s.count('evens')}"


def test_sum_between_25():
    """Easy case when 2 is the first and 5 is the last numbers from the list."""
    nums = [2, 1, 7, 3, 5]
    assert exam.sum_between_25(nums) == __solver_sum_between_25(nums)
    nums = [1, 2, 3, 4, 5, 6, 2, 8, 9, 5, 1]
    assert exam.sum_between_25(nums) == __solver_sum_between_25(nums)
    nums = [3, 2, 1, 5, 6, 2, 7, 5, 8, 2, 4, 5, 10]
    assert exam.sum_between_25(nums) == __solver_sum_between_25(nums)
    nums = [1, 2, 3, 2, 5, 4, 2, 1, 8, 2, 5]
    assert exam.sum_between_25(nums) == __solver_sum_between_25(nums)
    nums = [2, 5, 2, 5, 2, 5]
    assert exam.sum_between_25(nums) == __solver_sum_between_25(nums)


def __solver_sum_between_25(numbers):
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


@pytest.mark.timeout(1.0)
def test_transcribe():
    assert "G" == exam.transcribe("C")
    assert "C" == exam.transcribe("G")
    assert "A" == exam.transcribe("T")
    assert "U" == exam.transcribe("A")
    # G,C,T,A are only valid
    assert None == exam.transcribe("U")
    assert None == exam.transcribe("GO")
    assert None == exam.transcribe("123")
    assert None == exam.transcribe("AG$(")
    assert "UGCACCAGAAUU" == exam.transcribe("ACGTGGTCTTAA")
    assert "UUACGUUCCGAUCAU" == exam.transcribe("AATGCAAGGCTAGTA")
    assert "UUUUCUUU" == exam.transcribe("AAAAGAAA")
    assert "" == exam.transcribe("")
    assert "UGCACCAGAAUU" == exam.transcribe("acgtggtcttaa")
    assert "U" == exam.transcribe("a")
    assert "" == exam.transcribe("")
    assert None == exam.transcribe("ACGTGGOCTTAA")
    assert None == exam.transcribe("AuGC")
    assert None == exam.transcribe("gcu")
    for _ in range(100):
        alphabet = string.ascii_letters
        valid_nucleotides = {"G": "C", "C": "G", "T": "A", "A": "U"}
        strand_length = random.randint(0, 10)

        _dna_strand = ""  # DNA strand that is sent into transcribe() as an argument
        _rna_strand = ""  # Expected RNA strand

        if random.randint(0, 1):
            # Make a DNA only out of valid nucleotides
            alphabet = list(valid_nucleotides.keys())

        for _ in range(strand_length):
            random_char = random.choice(alphabet)

            # If chosen random char is not in valid nucleotides,
            # DNA cannot be transcribed => RNA is None
            if random_char.upper() in valid_nucleotides and _rna_strand is not None:
                _rna_strand += valid_nucleotides[random_char.upper()]
            else:
                _rna_strand = None

            _dna_strand += random_char

        # print(f"[{_dna_strand}] > [{_rna_strand}]")
        assert _rna_strand == exam.transcribe(_dna_strand), f"[{_dna_strand}] > [{_rna_strand}]"


@pytest.mark.timeout(1.0)
def test_union_of_dict():
    assert exam.union_of_dict({"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 42}) == {"a": 1}
    assert exam.union_of_dict({}, {"bar": "foo"}) == {}
    d = {}
    for i in range(50):
        d[i] = chr(i)
        assert exam.union_of_dict(d, d) == d

    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"A": 1, "b": 1, "c": "d", "g": 223}
    assert exam.union_of_dict(d1, d2) == {}
    assert exam.union_of_dict(d2, d1) == {}
    d1 = {"a": 1, "b": 2, "c": 3, "d": 3, "g": 52}
    d2 = {"a": 1, "b": 2, "c": "d"}
    assert exam.union_of_dict(d1, d2) == {"a": 1, "b": 2}
    assert exam.union_of_dict(d2, d1) == {"a": 1, "b": 2}
    # empty tests
    assert exam.union_of_dict({1: "something"}, {}) == {}
    assert exam.union_of_dict({}, {1: "something"}) == {}
    # none tests
    d1 = {"a": None, "b": None}
    d2 = {"a": 2345, "b": None}
    assert exam.union_of_dict(d1, d2) == {"b": None}
    assert exam.union_of_dict(d2, d1) == {"b": None}

    d1 = {None: "a", "b": None}
    d2 = {None: "a", "b": None}
    assert exam.union_of_dict(d1, d2) == {None: "a", "b": None}
    assert exam.union_of_dict(d2, d1) == {None: "a", "b": None}

    d1 = {"c": None, None: "d"}
    d2 = {None: "c", "d": None}
    assert exam.union_of_dict(d1, d2) == {}
    assert exam.union_of_dict(d2, d1) == {}


@pytest.mark.timeout(1.0)
def test_reserve_list():
    assert exam.reserve_list(["python"]) == ["python"]
    assert exam.reserve_list(["java"]) == ["java"]
    assert exam.reserve_list([]) == []
    assert exam.reserve_list(["book", "school", "gpa"]) == ['apg', 'loohcs', 'koob']
    assert exam.reserve_list(["python", "book"]) == ['book', 'python']
    assert exam.reserve_list(["python", "book", "python", "book"]) == ['book', 'python', 'book', 'python']
    assert exam.reserve_list(["python", "book", "book", "flower", "chair"]) == ['chair', 'flower', 'book', 'book',
                                                                                'python']
    assert exam.reserve_list(["java", "book"]) == ['koob', 'java']
    assert exam.reserve_list(["java", "book", "java"]) == ['java', 'koob', 'java']
    assert exam.reserve_list(["java", "book", "java", "flower"]) == ['rewolf', 'java', 'koob', 'java']
    assert exam.reserve_list(["java", "python"]) == ['python', 'java']
    assert exam.reserve_list(["java", "book", "python", "chair"]) == ['chair', 'python', 'koob', 'java']
    assert exam.reserve_list(["book", "java", "chair", "python"]) == ['python', 'riahc', 'java', 'koob']
    ran_strings = ['java', 'python', 'cake', 'book', 'garden', 'java', 'tree', 'board']
    for i in range(50):
        r_list = random.sample(ran_strings, len(ran_strings))
        assert exam.reserve_list(r_list) == reverse_func(r_list);


def reverse_func(input_strings):
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


def _overall(ex_input):
    assert exam.convert_binary_to_decimal(ex_input[0]) == ex_input[1]


def test_convert_binary_to_decimal():
    _overall(([0, 0, 0], 0))
    _overall(([1, 1, 1, 1], 15))
    _overall(([1, 1, 0, 0, 1], 25))
    _overall(([0, 1, 0, 0, 1, 0, 1], 37))
    _overall(([0, 1, 0, 0, 1, 0, 1], 37))


def test_print_pages():
    # test samples
    assert exam.print_pages("2,4,9") == [2, 4, 9]
    assert exam.print_pages("2,4-7") == [2, 4, 5, 6, 7]
    assert exam.print_pages("2-5,7,10-12,17") == [2, 3, 4, 5, 7, 10, 11, 12, 17]
    assert exam.print_pages("") == []
    assert exam.print_pages("1,1") == [1]
    assert exam.print_pages("2,1") == [1, 2]
    # test simple stuff
    assert exam.print_pages("1-3,4-5,6,7,8,9-10") == list(range(1, 11))
    assert exam.print_pages("1,3,5,7,9,11") == list(range(1, 12, 2))
    assert exam.print_pages("1,4,5,10-200") == [1, 4, 5] + list(range(10, 201))
    # test a bit more complicated stuff
    # test_overlap
    assert exam.print_pages("1,2,3,4,5,1-10,6,7,8,9,10") == list(range(1, 11))
    # test wrong order
    MAX_NUM = 50
    assert exam.print_pages(",".join(map(str, range(MAX_NUM, 0, -1)))) == list(
        range(1, MAX_NUM + 1)
    )
    _random_test(100, 20)
    _random_test(100, 40)


def _generate_random_numbers(num_of_items, max_number=100):
    rand_numbers = [random.randint(1, max_number) for i in range(num_of_items)]
    return ",".join(map(str, rand_numbers)), rand_numbers


def _generate_random_ranges(num_of_items, max_number=100):
    rand_numbers = random.choices(range(2, max_number), k=num_of_items)
    rand_pairs = [(random.randint(1, b - 1), b) for b in rand_numbers]
    rand_sequence = ",".join("-".join(map(str, t)) for t in rand_pairs)
    rand_range_lists = sum((list(range(a, b + 1)) for a, b in rand_pairs), [])
    return rand_sequence, rand_range_lists


def _random_test(test_times, num_of_elements):  # name to not be discovered by pytest
    for _ in range(test_times):
        selected_numbers = []
        selected_strings = []
        for _ in range(num_of_elements):
            if random.choice([0, 1]):
                s, nums = _generate_random_numbers(10, 100)
            else:
                s, nums = _generate_random_ranges(10, 100)
            selected_strings.append(s)
            selected_numbers += nums
        selected_string = ",".join(selected_strings)
        selected_numbers = sorted(set(selected_numbers))
        assert exam.print_pages(selected_string) == selected_numbers
