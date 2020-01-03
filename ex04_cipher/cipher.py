"""Encode and decode text using Rail-fence Cipher."""


def encode(message: str, key: int) -> str:
    """
    Encode text using Rail-fence Cipher.

    Replace all spaces with '_'.

    :param message: Text to be encoded.
    :param key: Encryption key.
    :return: Decoded string.
    """
    message = message.replace(" ", "_").replace(".", "")
    encoded = ""


    if key <= 1:
        return message

    matrix = [["" for col in range(len(message))] for row in range(key)]

    down_move = True
    row = 0

    for i in range(len(message)):
        matrix[row][i] = message[i]
        if row == 0:
            row += 1
            down_move = True
        elif row == key - 1:
            row -= 1
            down_move = False
        elif down_move:
            row += 1
        elif not down_move:
            row -= 1

    for list in matrix:
        encoded += "".join(list)

    return encoded


def decode(message: str, key: int) -> str:
    """
    Decode text knowing it was encoded using Rail-fence Cipher.

    '_' have to be replaced with spaces.

    :param message: Text to be decoded.
    :param key: Decryption key.
    :return: Decoded string.
    """
    message = message.replace("_", " ")

    if key <= 1:
        return message

    decoded = ""
    matrix = [["" for col in range(len(message))] for row in range(key)]
    index = 0

    for selected_row in range(0, len(matrix)):
        down_move = True
        row = 0
        for i in range(0, len(matrix[row])):
            if row == selected_row:
                matrix[row][i] += message[index]
                index += 1
            if row == 0:
                row += 1
                down_move = True
            elif row == key - 1:
                row -= 1
                down_move = False
            elif down_move:
                row += 1
            elif not down_move:
                row -= 1

    matrix = rotate(matrix)

    for list in matrix:
        decoded += "".join(list)

    return decoded


def rotate(matrix: list) -> list:
    """Rotate matrix.

    :param matrix: matrix to rotate
    :return: rotated matrix
    """
    result = [[0 for row in range(len(matrix))] for col in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]

    return result


if __name__ == '__main__':
    # print(encode("Mind on vaja krüpteerida", 3))  # => M_v_prido_aaküteiannjred
    # print(encode("Mind on", 3))  # => M_idonn
    # print(encode("hello", 1))  # => hello
    # print(encode("hello", 8))  # => hello
    # print(encode("kaks pead", 1))  # => kaks_pead
    # print(decode("kaks_pead", 1))  # => kaks pead
    # print(decode("M_idonn", 3))  # => Mind on
    print(decode("M_v_prido_aaküteiannjred", 3))  # => Mind on vaja krüpteerida
