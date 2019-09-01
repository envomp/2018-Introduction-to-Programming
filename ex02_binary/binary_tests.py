import pytest
import inspect
import re
from binary import dec_to_binary
from binary import binary_to_dec


def tester_dec_to_binary(dec: int) -> str:
    return bin(dec)[2::]


def tester_binary_to_dec(binary: str) -> int:
    return int(binary, 2)


@pytest.mark.timeout(1.0)
def test_different_numbers_dec_to_bin():
    assert dec_to_binary(0) == '0'
    assert dec_to_binary(1) == '1'
    assert dec_to_binary(12) == tester_dec_to_binary(12)
    assert dec_to_binary(35) == tester_dec_to_binary(35)
    assert dec_to_binary(67) == tester_dec_to_binary(67)
    assert dec_to_binary(1222) == tester_dec_to_binary(1222)
    assert dec_to_binary(24) == tester_dec_to_binary(24)
    assert dec_to_binary(859) == tester_dec_to_binary(859)


@pytest.mark.timeout(1.0)
def test_cheating_dec_to_bin():
    cheat_found = bool(re.search(r"int\(\S+, 2\)", inspect.getsource(binary_to_dec)))
    assert not cheat_found


@pytest.mark.timeout(1.0)
def test_different_numbers_bin_to_dec():
    assert binary_to_dec("0") == 0
    assert binary_to_dec("1") == 1
    assert binary_to_dec("100111001") == tester_binary_to_dec("100111001")
    assert binary_to_dec("10001101") == tester_binary_to_dec("10001101")
    assert binary_to_dec("10110") == tester_binary_to_dec("10110")
    assert binary_to_dec("11101") == tester_binary_to_dec("11101")
    assert binary_to_dec("1111111") == tester_binary_to_dec("1111111")
    assert binary_to_dec("1100110") == tester_binary_to_dec("1100110")


@pytest.mark.timeout(1.0)
def test_cheating_bin_to_dec():
    assert 'bin(' not in inspect.getsource(dec_to_binary)
