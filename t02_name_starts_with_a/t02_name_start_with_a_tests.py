import io
import os
import random

import pytest


def run_introduction_script(runner, value="abc"):
    script_name = "t02.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python', script_name, stdin=io.StringIO(value), cwd=working_dir)
    return script

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