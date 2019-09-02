import pytest


def mock_input_and_import_module(monkeypatch, value="a\nb\nc"):
    monkeypatch.setattr('builtins.input', lambda _: value)
    import t01 as a
    return a


@pytest.mark.timeout(1.0)
def test__first_number_variable_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.first_number == 19


@pytest.mark.timeout(1.0)
def test__second_number_variable_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.second_number == 7
