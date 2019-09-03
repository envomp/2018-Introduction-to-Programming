import io
import os
import random

import pytest


def run_introduction_script(runner, value="abc"):
    script_name = "t02.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python', script_name, stdin=io.StringIO(value), cwd=working_dir)
    return script

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