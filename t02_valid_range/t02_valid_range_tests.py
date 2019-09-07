import io
import os
import random

import pytest


def run_introduction_script(runner, value="abc"):
    script_name = "t02.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=io.StringIO(value), cwd=working_dir)
    return script

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