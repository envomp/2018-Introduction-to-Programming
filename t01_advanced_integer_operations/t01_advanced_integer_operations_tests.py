import pytest


def mock_input_and_import_module(monkeypatch, value="a\nb\nc"):
    monkeypatch.setattr('builtins.input', lambda _: value)
    import t01 as a
    return a


@pytest.mark.timeout(1.0)
def test__power_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert m.power_of_numbers == 19 ** 7
    except AttributeError:
        pytest.fail('Variable not found!')


@pytest.mark.timeout(1.0)
def test__remainder_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert m.remainder_of_numbers_division == 19 % 7
    except AttributeError:
        pytest.fail('Variable not found!')
