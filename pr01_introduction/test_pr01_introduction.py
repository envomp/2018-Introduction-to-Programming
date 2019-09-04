import pytest
import os


class MockStdin():
    """
    Pytest-console-scripts wants file-like object for stbydin so we wrap input in a class.

    Pytest-console-scripts docs see: https://github.com/kvas-it/pytest-console-scripts
    """

    def __init__(self, input_values: list):
        self.input = input_values

    def read(self):
        return "\n".join(self.input)


def run_introduction_script(runner, name, answer) -> "tuple[str, str]":
    script_name = "introduction.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=MockStdin([name, answer]),
                        cwd=working_dir)
    return script.stdout, script.stderr


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_introduction_ask_name(script_runner):
    output, _ = run_introduction_script(script_runner, name="Jack", answer="Yes")

    expected_output_text = "Hello, my name is Python! Please type your name to continue our conversation"
    assert expected_output_text in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_introduction_ask_question(script_runner):
    output, _ = run_introduction_script(script_runner, name="Bob", answer="Yes")

    expected_output_text = "Have you programmed before?"
    assert expected_output_text in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_introduction_answer_yes_output(script_runner):
    name = "Bob"
    output, _ = run_introduction_script(script_runner, name, answer="Yes")

    expected_output_text = f"Congratulations, {name}! It will be a little bit easier for you."
    assert expected_output_text in output
    assert "incorrect" not in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_introduction_answer_no_output(script_runner):
    name = "Robert"
    output, _ = run_introduction_script(script_runner, name, answer="No")

    expected_output_text = f"Don`t worry, {name}! You will learn everything you need."
    assert expected_output_text in output
    assert "incorrect" not in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_introduction_answer_else_output(script_runner):
    output, _ = run_introduction_script(script_runner, name="Bob", answer="Idk")

    expected_output_text = "Your input is incorrect!"
    assert "You will learn everything you need." not in output
    assert "It will be a little bit easier for you." not in output
    assert expected_output_text in output
