import math
import random

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


def run_introduction_script(runner, shape, dimension) -> "tuple[str, str]":
    script_name = "geometry.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=MockStdin([shape, dimension]),
                        cwd=working_dir)
    return script.stdout, script.stderr


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_geometry_ask_shape(script_runner):
    output, _ = run_introduction_script(script_runner, shape="circle", dimension="3")

    expected_output_text = "Please insert geometric shape:"
    assert expected_output_text in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_geomtry_ask_radius_circle(script_runner):
    output, _ = run_introduction_script(script_runner, shape="circle", dimension="3")

    expected_output_text = "Please insert radius in cm:"
    assert expected_output_text in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_geomtry_ask_side_length_square(script_runner):
    output, _ = run_introduction_script(script_runner, shape="square", dimension="3")

    expected_output_text = "Please insert side length in cm:"
    assert expected_output_text in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_geomtry_ask_side_length_triangle(script_runner):
    output, _ = run_introduction_script(script_runner, shape="triangle", dimension="3")

    expected_output_text = "Please insert side length in cm:"
    assert expected_output_text in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_geometry_triangle_example_output(script_runner):
    dimension = "3"
    shape = "triangle"
    output, _ = run_introduction_script(script_runner, shape, dimension)
    area = float(dimension) ** 2 / 4 * math.sqrt(3)
    expected_output_text = f"The area is {round(area, 2)} cm^2"
    expected_output_text_fstring_round = f"The area is {area:.2f} cm^2"
    assert expected_output_text in output or expected_output_text_fstring_round in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_geometry_circle_example_output(script_runner):
    dimension = "9"
    shape = "circle"
    output, _ = run_introduction_script(script_runner, shape, dimension)

    expected_output_text = f"The area is {round(float(dimension)**2 * 3.14, 2)} cm^2"
    expected_output_text_math_pi = f"The area is {round(float(dimension)**2 * math.pi, 2)} cm^2"
    assert expected_output_text in output or expected_output_text_math_pi in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_geometry_square_random_output(script_runner):
    dimension = str(random.randint(0, 100))
    shape = "square"
    output, _ = run_introduction_script(script_runner, shape, dimension)
    area = float(dimension) ** 2
    expected_output_text = f"The area is {round(area, 2)} cm^2"
    expected_output_text_fstring_round = f"The area is {area:.2f} cm^2"
    assert expected_output_text in output or expected_output_text_fstring_round in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_geometry_triangle_random_output(script_runner):
    dimension = str(random.randint(0, 1000))
    shape = "triangle"
    output, _ = run_introduction_script(script_runner, shape, dimension)
    area = float(dimension) ** 2 / 4 * math.sqrt(3)
    expected_output_text = f"The area is {round(area, 2)} cm^2"
    expected_output_text_math_pi = f"The area is {area:.2f} cm^2"
    assert expected_output_text in output or expected_output_text_math_pi in output


@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
@pytest.mark.incgroupdepend("syntax")
def test_geometry_else_output(script_runner):
    dimension = "0"
    shape = "another_shape"
    output, _ = run_introduction_script(script_runner, shape, dimension)

    expected_output_text = f"Shape is not supported."
    assert expected_output_text in output
