import io
import os
import random

import pytest


def run_introduction_script(runner, value="abc"):
    script_name = "t02.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python', script_name, stdin=io.StringIO(value), cwd=working_dir)
    return script

# part 1


@pytest.mark.script_launch_mode('subprocess')
def test__ask_name(script_runner):
    result = run_introduction_script(script_runner, "Mati\n")
    assert result.stdout.find("Enter your name") > -1


@pytest.mark.script_launch_mode('subprocess')
def test__greeting(script_runner):
    result = run_introduction_script(script_runner, "Mati\n")
    assert result.stdout.find("Welcome, Mati!") > -1


@pytest.mark.script_launch_mode('subprocess')
def test__check_names_with_a(script_runner):
    result = run_introduction_script(script_runner, "Ago")
    assert result.stdout.find("Your name starts with A.") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__check_names_without_a(script_runner):
    result = run_introduction_script(script_runner, "Mati\n")
    assert result.stdout.find("Your name starts with A.") == -1

# part 2

input_prefix1 = "Mati\n"

@pytest.mark.script_launch_mode('subprocess')
def test__check_ask_number(script_runner):
    result = run_introduction_script(script_runner, input_prefix1)
    assert result.stdout.find("Enter a number:") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__check_odd_number(script_runner):
    result = run_introduction_script(script_runner, input_prefix1 + "1\n")
    assert result.stdout.find("1 is an odd number") > -1

    result = run_introduction_script(script_runner, input_prefix1 + "11\n")
    assert result.stdout.find("11 is an odd number") > -1

    result = run_introduction_script(script_runner, input_prefix1 + "-243\n")
    assert result.stdout.find("-243 is an odd number") > -1


@pytest.mark.script_launch_mode('subprocess')
def test__check_even_number(script_runner):
    result = run_introduction_script(script_runner, input_prefix1 + "2\n")
    assert result.stdout.find("2 is an even number") > -1

    result = run_introduction_script(script_runner, input_prefix1 + "0\n")
    assert result.stdout.find("0 is an even number") > -1

    result = run_introduction_script(script_runner, input_prefix1 + "-98\n")
    assert result.stdout.find("-98 is an even number") > -1

# part 3

input_prefix2 = "Mati\n7\n"

@pytest.mark.script_launch_mode('subprocess')
def test__check_ask_number_between_1_and_10(script_runner):
    result = run_introduction_script(script_runner, input_prefix2)
    assert result.stdout.find("Enter a number between 1-10:") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__check_valid_number(script_runner):
    for i in range(1, 11):
        result = run_introduction_script(script_runner, input_prefix2 + f"{i}\n")
        assert result.stdout.find("invalid") == -1
        assert result.stdout.find("Thank you!") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__check_invalid_number_too_small(script_runner):
    for i in range(-5, 1):
        result = run_introduction_script(script_runner, input_prefix2 + f"{i}\n")
        assert result.stdout.find(f"{i} is an invalid number!") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__check_invalid_number_too_high(script_runner):
    for i in range(11, 20):
        result = run_introduction_script(script_runner, input_prefix2 + f"{i}\n")
        assert result.stdout.find(f"{i} is an invalid number!") > -1

# part 4

input_prefix3 = input_prefix2 + "8\n"

@pytest.mark.script_launch_mode('subprocess')
def test__check_ask_two_numbers(script_runner):
    result = run_introduction_script(script_runner, input_prefix3 + "1\n2\n")
    assert result.stdout.find("Enter A:") > -1
    assert result.stdout.find("Enter B:") > -1


@pytest.mark.script_launch_mode('subprocess')
def test__two_numbers_are_the_same(script_runner):
    result = run_introduction_script(script_runner, input_prefix3 + "1\n2\n")
    assert result.stdout.find("Enter A:") > -1

# part 5 - fizzbuzz
input_prefix4 = input_prefix3 + "1\n4\n"

def _test_fizz_buzz(script_runner, nr):
    result = run_introduction_script(script_runner, input_prefix4 + str(nr))
    expected = str(nr)
    if nr % 15 == 0:
        expected = "FizzBuzz"
    elif nr % 3 == 0:
        expected = "Fizz"
    elif nr % 5 == 0:
        expected = "Buzz"
    assert result.stdout.find(f"FizzBuzz for number {nr} is: {expected}") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__ask_fizz_buzz_number(script_runner):
    result = run_introduction_script(script_runner, input_prefix4)
    assert result.stdout.find("Enter a FizzBuzz number:") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__fizz_buzz_number_when_fizz(script_runner):
    _test_fizz_buzz(script_runner, 3)
    _test_fizz_buzz(script_runner, 6)
    _test_fizz_buzz(script_runner, 9)
    _test_fizz_buzz(script_runner, 39969)

@pytest.mark.script_launch_mode('subprocess')
def test__fizz_buzz_number_when_buzz(script_runner):
    _test_fizz_buzz(script_runner, 5)
    _test_fizz_buzz(script_runner, 10)
    _test_fizz_buzz(script_runner, 20)
    _test_fizz_buzz(script_runner, 124385)


@pytest.mark.script_launch_mode('subprocess')
def test__fizz_buzz_number_when_fizzbuzz(script_runner):
    _test_fizz_buzz(script_runner, 15)
    _test_fizz_buzz(script_runner, 30)
    _test_fizz_buzz(script_runner, 45)
    _test_fizz_buzz(script_runner, 124390)


@pytest.mark.script_launch_mode('subprocess')
def test__fizz_buzz_number_when_number(script_runner):
    _test_fizz_buzz(script_runner, 1)
    _test_fizz_buzz(script_runner, 2)
    _test_fizz_buzz(script_runner, 4)
    _test_fizz_buzz(script_runner, 16)
    _test_fizz_buzz(script_runner, 7)
    _test_fizz_buzz(script_runner, 29)
    _test_fizz_buzz(script_runner, 31)
    _test_fizz_buzz(script_runner, 124391)

# grade
input_prefix5 = input_prefix4 + "1\n"

def _check_grade(script_runner, points, good_mood):
    mood_str = random.choice(("n", "no", "jah", "j", "True", "False", "1"))
    if good_mood:
        mood_str = random.choice(("y",  "yes"))
    result = run_introduction_script(script_runner, input_prefix5 + f"{points}\n{mood_str}")
    grade = 0
    if good_mood: points += 5
    if points > 900: grade = 5
    elif points > 800: grade = 4
    elif points > 700: grade = 3
    elif points > 600: grade = 2
    elif points > 500: grade = 1
    assert result.stdout.find(f"Your grade is: {grade}") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__ask_points(script_runner):
    result = run_introduction_script(script_runner, input_prefix5 + "12\n")
    assert result.stdout.find("Enter your points:") > -1
    assert result.stdout.find("Teacher in a good mood?") > -1


@pytest.mark.script_launch_mode('subprocess')
def test__grade_0(script_runner):
    _check_grade(script_runner, 0, True)
    _check_grade(script_runner, 0, False)
    _check_grade(script_runner, 400, True)
    _check_grade(script_runner, 400, False)
    _check_grade(script_runner, 499, False)
    _check_grade(script_runner, 500, False)
    _check_grade(script_runner, 495, True)


def _test_grade(script_runner, grade):
    p = (grade - 1) * 100
    _check_grade(script_runner, 496 + p, True)
    _check_grade(script_runner, 499 + p, True)
    _check_grade(script_runner, 501 + p, True)
    _check_grade(script_runner, 501 + p, False)
    _check_grade(script_runner, 563 + p, True)
    _check_grade(script_runner, 523 + p, False)
    _check_grade(script_runner, 599 + p, False)
    _check_grade(script_runner, 600 + p, False)
    _check_grade(script_runner, 595 + p, True)

@pytest.mark.script_launch_mode('subprocess')
def test__grade_1(script_runner):
    _test_grade(script_runner, 1)

@pytest.mark.script_launch_mode('subprocess')
def test__grade_2(script_runner):
    _test_grade(script_runner, 2)

@pytest.mark.script_launch_mode('subprocess')
def test__grade_3(script_runner):
    _test_grade(script_runner, 3)

@pytest.mark.script_launch_mode('subprocess')
def test__grade_4(script_runner):
    _test_grade(script_runner, 4)

@pytest.mark.script_launch_mode('subprocess')
def test__grade_5(script_runner):
    _test_grade(script_runner, 5)

# ---- longer string

input_prefix6 = input_prefix5 + "123\ny\n"

@pytest.mark.script_launch_mode('subprocess')
def test__ask_two_names(script_runner):
    result = run_introduction_script(script_runner, input_prefix6 + "ago\n")
    assert result.stdout.find("Enter name 1:") > -1
    assert result.stdout.find("Enter name 2:") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__two_names_same_length(script_runner):
    result = run_introduction_script(script_runner, input_prefix6 + "ago\nsam\n")
    assert result.stdout.find("Full name: Ago Sam") > -1

    result = run_introduction_script(script_runner, input_prefix6 + "Tiit\nJAAK\n")
    assert result.stdout.find("Full name: Tiit Jaak") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__two_names_first_longer(script_runner):
    result = run_introduction_script(script_runner, input_prefix6 + "ago\nle\n")
    assert result.stdout.find("Full name: Ago Le") > -1

    result = run_introduction_script(script_runner, input_prefix6 + "ago\nA\n")
    assert result.stdout.find("Full name: Ago A") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__two_names_first_shorter(script_runner):
    result = run_introduction_script(script_runner, input_prefix6 + "u\nago\n")
    assert result.stdout.find("Full name: Ago U") > -1

    result = run_introduction_script(script_runner, input_prefix6 + "ago\nmadis\n")
    assert result.stdout.find("Full name: Madis Ago") > -1

# -----------

input_prefix7 = input_prefix6 + "a\nb\n"

@pytest.mark.script_launch_mode('subprocess')
def test__ask_cat_count(script_runner):
    result = run_introduction_script(script_runner, input_prefix7)
    assert result.stdout.find("Cat counting:") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__counting_cats_no_cats(script_runner):
    result = run_introduction_script(script_runner, input_prefix7 + "tere\n")
    assert result.stdout.find("Cat count: 0") > -1

    result = run_introduction_script(script_runner, input_prefix7 + "\n")
    assert result.stdout.find("Cat count: 0") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__counting_cats_only_categories(script_runner):
    result = run_introduction_script(script_runner, input_prefix7 + "category category    category yes\n")
    assert result.stdout.find("Cat count: 0") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__counting_cats_only_cats(script_runner):
    result = run_introduction_script(script_runner, input_prefix7 + "cat\n")
    assert result.stdout.find("Cat count: 1") > -1

    result = run_introduction_script(script_runner, input_prefix7 + "cat cat\n")
    assert result.stdout.find("Cat count: 2") > -1

    result = run_introduction_script(script_runner, input_prefix7 + "cat " * 1000 + "nope\n")
    assert result.stdout.find("Cat count: 1000") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__counting_cats_cats_and_categories(script_runner):
    result = run_introduction_script(script_runner, input_prefix7 + "cat category\n")
    assert result.stdout.find("Cat count: 1") > -1
    result = run_introduction_script(script_runner, input_prefix7 + "category cat\n")
    assert result.stdout.find("Cat count: 1") > -1
    result = run_introduction_script(script_runner, input_prefix7 + "cat category cat\n")
    assert result.stdout.find("Cat count: 2") > -1
    words = ['cat'] * 15 + ['category'] * 17
    random.shuffle(words)

    result = run_introduction_script(script_runner, input_prefix7 + " ".join(words) + "\n")
    assert result.stdout.find("Cat count: 15") > -1


# ----------- replace

input_prefix8 = input_prefix7 + "cat\n"

@pytest.mark.script_launch_mode('subprocess')
def test__ask_replace_text(script_runner):
    result = run_introduction_script(script_runner, input_prefix8)
    assert result.stdout.find("Replace text:") > -1

@pytest.mark.script_launch_mode('subprocess')
def test__replace_text_only_e(script_runner):
    result = run_introduction_script(script_runner, input_prefix8 + "tere\n")
    assert result.stdout.find("Replaced text: toro") > -1

    result = run_introduction_script(script_runner, input_prefix8 + "eeee\n")
    assert result.stdout.find("Replaced text: oooo") > -1


@pytest.mark.script_launch_mode('subprocess')
def test__replace_text_only_a(script_runner):
    result = run_introduction_script(script_runner, input_prefix8 + "aaaaa\n")
    assert result.stdout.find("Replaced text: eeeee") > -1

    result = run_introduction_script(script_runner, input_prefix8 + "paat\n")
    assert result.stdout.find("Replaced text: peet") > -1


@pytest.mark.script_launch_mode('subprocess')
def test__replace_text_both_a_and_e(script_runner):
    result = run_introduction_script(script_runner, input_prefix8 + "aeo\n")
    assert result.stdout.find("Replaced text: eoo") > -1

    result = run_introduction_script(script_runner, input_prefix8 + "this is a longer text here\n")
    assert result.stdout.find("Replaced text: this is e longor toxt horo") > -1
