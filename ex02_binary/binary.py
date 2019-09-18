"""Converter."""


def dec_to_binary(dec: int) -> str:
    """
    Convert decimal number into binary.

    :param dec: decimal number to convert
    :return: number in binary
    """
    bin_ans = ""
    while dec != 0:
        bin_ans += '0' if dec % 2 == 0 else '1'
        dec = int(dec / 2)
    return "0" if not bin_ans else bin_ans[::-1]


def binary_to_dec(binary: str) -> int:
    """
    Convert binary number into decimal.

    :param binary: binary number to convert
    :return: number in decimal
    """
    binary = binary[::-1]
    results = []
    for i in range(len(binary)):
        results.append(int(binary[i]) * (2 ** i))
    return sum(results)


if __name__ == "__main__":
    assert binary_to_dec("0") == 0
    assert binary_to_dec("1") == 1
    assert binary_to_dec("10001101") == int("10001101", 2)
    assert binary_to_dec("10110") == int("10110", 2)
    assert binary_to_dec("11101") == int("11101", 2)
