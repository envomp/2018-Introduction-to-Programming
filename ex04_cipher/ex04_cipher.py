"""Encode and decode given string."""


def encode(message: str, key: int):
    text_with_replaced_spaces = message.replace(" ", "_")

    if key == 1:
        return text_with_replaced_spaces

    decoded_text_holder = pseudo_matrix(text_with_replaced_spaces, key)
    return "".join(decoded_text_holder).replace(".", "")


def pseudo_matrix(message, key):
    down_move = True
    position = 0
    text_holder = [""] * key
    for letter in message:
        for x in range(key):
            if x == position:
                text_holder[position] += letter
            else:
                text_holder[x] += "."

        if position == 0:
            position += 1
            down_move = True

        elif position == key - 1:
            position -= 1
            down_move = False

        elif down_move:
            position += 1
        elif not down_move:
            position -= 1
    return text_holder


def decode(message: str, key: int) -> str:
    if key == 1:
        return message.replace("_", " ")

    pseudo_matrix_ = pseudo_matrix("*" * len(message), key)

    result_matrix = [""] * key
    index = 0
    for row in range(key):
        for col in range(len(message)):
            if pseudo_matrix_[row][col] == "*":
                result_matrix[row] += message[index]
                index += 1
            else:
                result_matrix[row] += "."

    down_move = True
    row = 0
    result = ""
    for i in range(len(message)):
        if result_matrix[row][i] != ".":
            result += result_matrix[row][i]

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

    return result.replace("_", " ")


if __name__ == '__main__':
    print(encode("Mind on vaja kodeerida", 3))  # => M_v_edido_aakdeiannjor
    print(encode("hello", 3))  # => hoell

    print(encode("hello", 1))  # => hello
    print(encode("hello", 8))  # => hello

    print(decode("kaks_pead", 1))  # => kask pead

    print(decode("hoell", 3))  # => hello
    print(decode("hello", 1))  # => hello
    print(decode("M_idonn", 3))  # => Mind on
    print(decode("M_v_edido_aakdeiannjor", 3))  # => Mind on vaja kodeerida
