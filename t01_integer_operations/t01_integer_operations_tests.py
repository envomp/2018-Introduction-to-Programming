import pytest


def mock_input_and_import_module(monkeypatch, value="a\nb\nc"):
    monkeypatch.setattr('builtins.input', lambda _: value)
    import t01 as a
    return a


@pytest.mark.timeout(1.0)
def test__sum_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert m.sum_of_numbers == 19 + 7
    except AttributeError:
        pytest.fail('Variable not found!')


@pytest.mark.timeout(1.0)
def test__diff_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert m.dif_of_numbers == 19 - 7
    except AttributeError:
        pytest.fail('Variable not found!')


@pytest.mark.timeout(1.0)
def test__composition_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert m.composition_of_numbers == 19 * 7
    except AttributeError:
        pytest.fail('Variable not found!')


@pytest.mark.timeout(1.0)
def test__quotient_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert m.quotient_of_numbers == 19 / 7
    except AttributeError:
        pytest.fail('Variable not found!')
