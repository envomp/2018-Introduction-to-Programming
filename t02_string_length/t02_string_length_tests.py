import io
import os
import random

import pytest


def run_introduction_script(runner, value="abc"):
    script_name = "t02.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=io.StringIO(value), cwd=working_dir)
    return script

input_prefix6 = "Mati\n7\n8\n1\n4\n1\n123\ny\n"

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
