import pytest


def mock_input_and_import_module(monkeypatch, value="a\nb\nc"):
    monkeypatch.setattr('builtins.input', lambda _: value)
    import t01 as a
    return a


@pytest.mark.timeout(1.0)
def test__equals_value_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert not m.are_numbers_equal
    except AttributeError:
        pytest.fail('Variable not found!')


@pytest.mark.timeout(1.0)
def test__greater_value_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert m.is_first_number_greater_than_second_number == (19 > 7)
    except AttributeError:
        pytest.fail('Variable not found!')


@pytest.mark.timeout(1.0)
def test__greater_or_equal_value_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert m.is_first_number_greater_than_or_equal_to_second_number == (19 >= 7)
    except AttributeError:
        pytest.fail('Variable not found!')


@pytest.mark.timeout(1.0)
def test__less_value_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert m.is_first_number_less_than_second_number == (19 < 7)
    except AttributeError:
        pytest.fail('Variable not found!')


@pytest.mark.timeout(1.0)
def test__less_or_equal_value_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert m.is_first_number_less_than_or_equal_to_second_number == (19 <= 7)
    except AttributeError:
        pytest.fail('Variable not found!')
