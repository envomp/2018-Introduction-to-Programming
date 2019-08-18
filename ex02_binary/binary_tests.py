import pytest
from binary import dec_to_binary
from binary import binary_to_dec


def test_dec_to_binary(dec: int) -> str:
    """
    Convert decimal number into binary.

    :param dec: decimal number to convert
    :return: number in binary
    """
    return bin(dec)[2::]


def test_binary_to_dec(bin: str) -> int:
    """
    Convert binary number into decimal.

    :param bin: binary number to convert
    :return: number in decimal
    """
    return int(bin, 2)


@pytest.mark.timeout(1.0)
def test_different_numbers_dec_to_bin():
    assert dec_to_binary(0) == "0"
    assert dec_to_binary(1) == "1"
    assert dec_to_binary(12) == test_dec_to_binary(12)
    assert dec_to_binary(35) == test_dec_to_binary(35)
    assert dec_to_binary(67) == test_dec_to_binary(67)
    assert dec_to_binary(1222) == test_dec_to_binary(1222)
    assert dec_to_binary(24) == test_dec_to_binary(24)
    assert dec_to_binary(859) == test_dec_to_binary(859)


@pytest.mark.timeout(1.0)
def test_different_numbers_bin_to_dec():
    assert binary_to_dec("0") == 0
    assert binary_to_dec("1") == 1
    assert binary_to_dec("100111001") == test_binary_to_dec("100111001")
    assert binary_to_dec("10001101") == test_binary_to_dec("10001101")
    assert binary_to_dec("10110") == test_binary_to_dec("10110")
    assert binary_to_dec("11101") == test_binary_to_dec("11101")
    assert binary_to_dec("1111111") == test_binary_to_dec("1111111")
    assert binary_to_dec("1100110") == test_binary_to_dec("1100110")
