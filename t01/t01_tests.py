import io
import os

import pytest


def is_not_blank(s: str):
    return len(s.replace(" ", "")) > 0


def mock_input_and_import_module(monkeypatch, value="abc"):
    monkeypatch.setattr('builtins.input', lambda _: value)
    import t01 as a
    return a


def run_introduction_script(runner, value="abc"):
    script_name = "t01.py"
    working_dir = os.path.dirname(os.path.abspath(__file__))
    script = runner.run('python3.7', script_name, stdin=io.StringIO(value), cwd=working_dir)
    return script


@pytest.mark.incgroup("int_var_declar")
@pytest.mark.timeout(1.0)
def test__first_number_variable_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.first_number == 19


@pytest.mark.incgroup("int_var_declar")
@pytest.mark.timeout(1.0)
def test__second_number_variable_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.second_number == 7


@pytest.mark.incgroupdepend("int_var_declar")
@pytest.mark.incgroup("int_oper")
@pytest.mark.timeout(1.0)
def test__sum_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.sum_of_numbers == 19 + 7


@pytest.mark.incgroupdepend("int_var_declar")
@pytest.mark.incgroup("int_oper")
@pytest.mark.timeout(1.0)
def test__diff_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.dif_of_numbers == 19 - 7


@pytest.mark.incgroupdepend("int_var_declar")
@pytest.mark.incgroup("int_oper")
@pytest.mark.timeout(1.0)
def test__composition_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.composition_of_numbers == 19 * 7


@pytest.mark.incgroupdepend("int_var_declar")
@pytest.mark.incgroup("int_oper")
@pytest.mark.timeout(1.0)
def test__quotient_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.quotient_of_numbers == 19 / 7


@pytest.mark.incgroupdepend("int_oper")
@pytest.mark.incgroup("int_adv_oper")
@pytest.mark.timeout(1.0)
def test__power_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.power_of_numbers == 19 ** 7


@pytest.mark.incgroupdepend("int_oper")
@pytest.mark.incgroup("int_adv_oper")
@pytest.mark.timeout(1.0)
def test__remainder_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.remainder_of_numbers_division == 19 % 7


@pytest.mark.incgroupdepend("int_adv_oper")
@pytest.mark.incgroup("boolean_const_declar")
@pytest.mark.timeout(1.0)
def test__constant_boolean_value_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.constant_boolean_value


@pytest.mark.incgroupdepend("boolean_const_declar")
@pytest.mark.incgroup("bool_oper1")
@pytest.mark.timeout(1.0)
def test__equals_value_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert not m.are_numbers_equal


@pytest.mark.incgroupdepend("boolean_const_declar")
@pytest.mark.incgroup("bool_oper1")
@pytest.mark.timeout(1.0)
def test__greater_value_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.is_first_number_greater_than_second_number == (19 > 7)


@pytest.mark.incgroupdepend("boolean_const_declar")
@pytest.mark.incgroup("bool_oper1")
@pytest.mark.timeout(1.0)
def test__greater_or_equal_value_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.is_first_number_greater_than_or_equal_to_second_number == (19 >= 7)


@pytest.mark.incgroupdepend("boolean_const_declar")
@pytest.mark.incgroup("bool_oper1")
@pytest.mark.timeout(1.0)
def test__less_value_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.is_first_number_less_than_second_number == (19 < 7)


@pytest.mark.incgroupdepend("boolean_const_declar")
@pytest.mark.incgroup("bool_oper1")
@pytest.mark.timeout(1.0)
def test__less_or_equal_value_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.is_first_number_less_than_or_equal_to_second_number == (19 <= 7)


@pytest.mark.incgroupdepend("bool_oper1")
@pytest.mark.incgroup("bool_oper2")
@pytest.mark.timeout(1.0)
def test__third_number_variable_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.third_number == 14


@pytest.mark.incgroupdepend("bool_oper1")
@pytest.mark.incgroup("bool_oper2")
@pytest.mark.timeout(1.0)
@pytest.mark.timeout(1.0)
def test__number_in_between_value_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.third_number_is_between_first_and_second == (19 < 14 < 7)


@pytest.mark.incgroupdepend("bool_oper2")
@pytest.mark.incgroup("string_var_declar")
@pytest.mark.timeout(1.0)
def test__first_name_is_not_blank(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert is_not_blank(m.first_name)


@pytest.mark.incgroupdepend("bool_oper2")
@pytest.mark.incgroup("string_var_declar")
@pytest.mark.timeout(1.0)
def test__last_name_is_not_blank(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert is_not_blank(m.last_name)


@pytest.mark.incgroupdepend("string_var_declar")
@pytest.mark.incgroup("f_str")
@pytest.mark.timeout(1.0)
def test__greeting_sentence_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert is_not_blank(m.first_name)
    assert is_not_blank(m.last_name)
    assert m.self_description_sentence == f'My name is {m.first_name} {m.last_name}'


@pytest.mark.incgroupdepend("string_var_declar")
@pytest.mark.incgroup("f_str")
@pytest.mark.timeout(1.0)
@pytest.mark.timeout(1.0)
def test__name_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert is_not_blank(m.first_name)
    assert is_not_blank(m.last_name)
    assert m.name == f'{m.first_name} {m.last_name}'


@pytest.mark.incgroupdepend("f_str")
@pytest.mark.incgroup("prints")
@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
def test__prints_are_correct(script_runner):
    s = run_introduction_script(script_runner, value='name\nlastname')
    assert 'My name is ' in s.stdout
    assert 'I am glad to see you here' in s.stdout


@pytest.mark.incgroupdepend("prints")
@pytest.mark.incgroup("input")
@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
def test__asks_first_name(script_runner):
    s = run_introduction_script(script_runner)
    assert 'What is your first name?' in s.stdout


@pytest.mark.incgroupdepend("prints")
@pytest.mark.incgroup("input")
@pytest.mark.timeout(1.0)
def test__user_first_name_is_correct(monkeypatch):
    s = mock_input_and_import_module(monkeypatch)
    assert s.user_first_name == 'abc'


@pytest.mark.incgroupdepend("prints")
@pytest.mark.incgroup("input")
@pytest.mark.timeout(1.0)
@pytest.mark.script_launch_mode('subprocess')
def test__asks_last_name(script_runner):
    s = run_introduction_script(script_runner)
    assert 'What is your first name?' in s.stdout


@pytest.mark.incgroupdepend("prints")
@pytest.mark.incgroup("input")
@pytest.mark.timeout(1.0)
def test__user_last_name_is_correct(monkeypatch):
    s = mock_input_and_import_module(monkeypatch)
    assert s.user_last_name == 'abc'
