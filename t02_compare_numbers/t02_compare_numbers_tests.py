import io
import os
import random

import pytest


def run_introduction_script(runner, value="abc"):
    script_name = "t02.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=io.StringIO(value), cwd=working_dir)
    return script


input_prefix3 = "Mati\n7\n8\n"

@pytest.mark.script_launch_mode('subprocess')
def test__check_ask_two_numbers(script_runner):
    result = run_introduction_script(script_runner, input_prefix3 + "1\n2\n")
    assert result.stdout.find("Enter A:") > -1
    assert result.stdout.find("Enter B:") > -1


@pytest.mark.script_launch_mode('subprocess')
def test__two_numbers_are_the_same(script_runner):
    result = run_introduction_script(script_runner, input_prefix3 + "11\n11\n")
    assert result.stdout.find("11 == 11") > -1


@pytest.mark.script_launch_mode('subprocess')
def test__two_numbers_a_is_bigger(script_runner):
    result = run_introduction_script(script_runner, input_prefix3 + "13\n2\n")
    assert result.stdout.find("Bigger number: 13") > -1


@pytest.mark.script_launch_mode('subprocess')
def test__two_numbers_b_is_bigger(script_runner):
    result = run_introduction_script(script_runner, input_prefix3 + "13\n24\n")
    assert result.stdout.find("Bigger number: 24") > -1