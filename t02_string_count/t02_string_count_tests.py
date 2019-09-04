import io
import os
import random

import pytest


def run_introduction_script(runner, value="abc"):
    script_name = "t02.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=io.StringIO(value), cwd=working_dir)
    return script

input_prefix7 = "Mati\n7\n8\n1\n4\n1\n123\ny\na\nb\n"

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
