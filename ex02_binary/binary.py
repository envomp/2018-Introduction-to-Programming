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
    return bin_ans


def binary_to_dec(binary: str) -> int:
    """
    Convert binary number into decimal.

    :param binary: binary number to convert
    :return: number in decimal
    """
    int_sum, step = 0, 1
    for element in list(reversed(binary)):
        int_sum += step if element == '1' else 0
        step *= 2
    return int_sum


if __name__ == "__main__":
    print(dec_to_binary(145))  # -> 10010001
    print(dec_to_binary(245))  # -> 11110101
    print(dec_to_binary(255))  # -> 11111111

    print(binary_to_dec("1111"))  # -> 15
    print(binary_to_dec("10101"))  # -> 21
    print(binary_to_dec("10010"))  # -> 18
