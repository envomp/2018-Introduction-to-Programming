import pytest


def is_not_blank(s: str):
    return len(s.replace(" ", "")) > 0


def mock_input_and_import_module(monkeypatch, value="a\nb\nc"):
    monkeypatch.setattr('builtins.input', lambda _: value)
    import t01 as a
    return a


@pytest.mark.timeout(1.0)
def test__self_description_sentence_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert is_not_blank(m.first_name)
        assert is_not_blank(m.last_name)
        assert m.self_description_sentence == f'My name is {m.first_name} {m.last_name}'
    except AttributeError:
        pytest.fail('Variable not found!')


@pytest.mark.timeout(1.0)
def test__name_is_correct(monkeypatch):
    try:
        m = mock_input_and_import_module(monkeypatch)
        assert is_not_blank(m.first_name)
        assert is_not_blank(m.last_name)
        assert m.name == f'{m.first_name} {m.last_name}'
    except AttributeError:
        pytest.fail('Variable not found!')
