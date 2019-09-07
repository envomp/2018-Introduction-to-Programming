

import io
import os
import random

import pytest


def run_introduction_script(runner, value="abc"):
    script_name = "t02.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=io.StringIO(value), cwd=working_dir)
    return script

input_prefix5 = "Mati\n7\n8\n1\n4\n1\n"

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