import pytest
from temperature import *


@pytest.mark.timeout(1.0)
def test_variable_exists():
    try:
        temperature
    except:
        assert False


@pytest.mark.timeout(1.0)
def test_variable_type():
    assert isinstance(temperature, int)


@pytest.mark.timeout(1.0)
def test_variable_value():
    assert temperature == 20
