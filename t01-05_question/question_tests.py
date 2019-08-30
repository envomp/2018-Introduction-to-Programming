import pytest
from question import *


@pytest.mark.timeout(1.0)
def test_variable_exists():
    try:
        question
    except:
        assert False


@pytest.mark.timeout(1.0)
def test_variable_type():
    assert isinstance(question, str)


@pytest.mark.timeout(1.0)
def test_variable_value():
    assert question == "What’s up?"
