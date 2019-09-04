

import io
import os
import random

import pytest


def run_introduction_script(runner, value="abc"):
    script_name = "t02.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=io.StringIO(value), cwd=working_dir)
    return script


input_prefix8 = "Mati\n7\n8\n1\n4\n1\n123\ny\na\nb\ncat\n"

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
