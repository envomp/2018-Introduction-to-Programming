import pytest


def mock_input_and_import_module(monkeypatch, value="a\nb\nc"):
    monkeypatch.setattr('builtins.input', lambda _: value)
    import t01 as a
    return a


@pytest.mark.timeout(1.0)
def test__third_number_variable_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.third_number == 14


@pytest.mark.timeout(1.0)
def test__number_in_between_value_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.third_number_is_between_first_and_second == (19 < 14 < 7)
