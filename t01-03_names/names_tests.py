import pytest
from names import *


@pytest.mark.timeout(1.0)
def test_list_exists():
    try:
        names
    except:
        assert False


@pytest.mark.timeout(1.0)
def test_variable_type():
    assert isinstance(names, list)


@pytest.mark.timeout(1.0)
def test_list_length():
    assert len(names) == 3


@pytest.mark.timeout(1.0)
def test_list_contains_bill_gates():
    assert "Bill Gates" in names


@pytest.mark.timeout(1.0)
def test_list_contains_jeff_bezos():
    assert "Jeff Bezos" in names


@pytest.mark.timeout(1.0)
def test_list_contains_ago_luberg():
    assert "Ago Luberg" in names
