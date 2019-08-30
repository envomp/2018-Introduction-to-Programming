import pytest
import importlib

from your_name import *
import your_name


@pytest.mark.timeout(1.0)
def test_first_name_exists():
    try:
        first_name
    except:
        assert False


@pytest.mark.timeout(1.0)
def test_last_name_exists():
    try:
        last_name
    except:
        assert False


@pytest.mark.timeout(1.0)
def test_name_exists():
    try:
        name
    except:
        assert False


@pytest.mark.timeout(1.0)
def test_first_name_type():
    assert isinstance(first_name, str)


@pytest.mark.timeout(1.0)
def test_last_name_type():
    assert isinstance(last_name, str)


@pytest.mark.timeout(1.0)
def test_name_type():
    assert isinstance(name, str)


@pytest.mark.timeout(1.0)
def test_first_name_is_not_empty():
    assert len(first_name) > 0


@pytest.mark.timeout(1.0)
def test_last_name_is_not_empty():
    assert len(last_name) > 0


@pytest.mark.timeout(1.0)
def test_name_is_not_empty():
    assert len(name) > 0


def test_name_is_made_of_first_and_last_name():
    assert name == first_name + " " + last_name


@pytest.mark.timeout(1.0)
def test_name_is_printed(capsys):
    importlib.reload(your_name)
    captured = capsys.readouterr()
    assert captured.out == name + "\n"
