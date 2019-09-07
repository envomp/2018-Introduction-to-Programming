import pytest


def is_not_blank(s: str):
    return len(s.replace(" ", "")) > 0


def mock_input_and_import_module(monkeypatch, value="a\nb\nc"):
    monkeypatch.setattr('builtins.input', lambda _: value)
    import t01 as a
    return a


@pytest.mark.timeout(1.0)
def test__first_name_is_not_blank(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert is_not_blank(m.first_name)


@pytest.mark.timeout(1.0)
def test__last_name_is_not_blank(monkeypatch):
    m = mock_input_and_import_module(monkeypatch)
    assert is_not_blank(m.last_name)
