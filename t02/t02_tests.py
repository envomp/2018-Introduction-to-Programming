import io
import os

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