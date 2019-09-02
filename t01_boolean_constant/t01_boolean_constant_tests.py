import pytest


def mock_input_and_import_module(monkeypatch, value="a\nb\nc"):
    monkeypatch.setattr('builtins.input', lambda _: value)
    import t01 as a
    return a


@pytest.mark.timeout(1.0)
def test__constant_boolean_value_is_correct(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert m.constant_boolean_value
