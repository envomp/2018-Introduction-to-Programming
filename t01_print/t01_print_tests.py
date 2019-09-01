import io
import sys

import pytest


@pytest.mark.timeout(1.0)
def test__prints_are_correct(monkeypatch):
    try:
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        monkeypatch.setattr('builtins.input', lambda _: "abc")
        import t01 as m
        value = new_stdout.getvalue()
        assert f'My name is {m.first_name} {m.last_name}' in value
        assert 'I am glad to see you here' in value
    except AttributeError:
        pytest.fail('Variable not found!')
    finally:
        sys.stdout = sys.__stdout__
