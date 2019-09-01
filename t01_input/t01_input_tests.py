import io
import os

import pytest


def is_not_blank(s: str):
    return len(s.replace(" ", "")) > 0


def mock_input_and_import_module(monkeypatch, value="abc"):
    monkeypatch.setattr('builtins.input', lambda _: value)
    import t01 as a
    return a


def run_introduction_script(runner):
    script_name = "t01.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=io.StringIO('a\nb'), cwd=working_dir)
    return script


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
def test__asks_first_name(script_runner):
    s = run_introduction_script(script_runner)
    assert 'What is your first name?' in s.stdout


@pytest.mark.timeout(1.0)
def test__user_first_name_is_correct(monkeypatch):
    try:
        s = mock_input_and_import_module(monkeypatch)
        assert s.user_first_name == 'abc'
    except AttributeError:
        pytest.fail('Variable not found!')


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
def test__asks_last_name(script_runner):
    s = run_introduction_script(script_runner)
    assert 'What is your first name?' in s.stdout


@pytest.mark.timeout(1.0)
def test__user_last_name_is_correct(monkeypatch):
    try:
        s = mock_input_and_import_module(monkeypatch)
        assert s.user_last_name == 'abc'
    except AttributeError:
        pytest.fail('Variable not found!')
