"""Day 2."""


def get_fresh_data():
    """Fresh data."""
    return [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 19, 9, 23, 1, 5, 23, 27, 1, 27, 9,
            31, 1, 6, 31, 35, 2, 35, 9, 39, 1, 39, 6, 43, 2, 9, 43, 47, 1, 47, 6, 51, 2, 51, 9, 55, 1, 5, 55,
            59, 2, 59, 6, 63, 1, 9, 63, 67, 1, 67, 10, 71, 1, 71, 13, 75, 2, 13, 75, 79, 1, 6, 79, 83, 2, 9, 83,
            87, 1, 87, 6, 91, 2, 10, 91, 95, 2, 13, 95, 99, 1, 9, 99, 103, 1, 5, 103, 107, 2, 9, 107, 111, 1, 111,
            5, 115, 1, 115, 5, 119, 1, 10, 119, 123, 1, 13, 123, 127, 1, 2, 127, 131, 1, 131, 13, 0, 99, 2, 14, 0, 0]


def execute(data: list) -> list:
    """Excecute commands."""
    for i in range(0, len(data), 4):
        if data[i] == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
        elif data[i] == 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
        elif data[i] == 99:
            break
    return data


if __name__ == '__main__':
    # Part 1
    data = get_fresh_data()
    data[1] = 12
    data[2] = 2
    data = execute(data)
    print(f"Answer 1: {data[0]}")

    # Part 2
    exit = False
    for x in range(len(data)):
        for y in range(len(data)):
            data = get_fresh_data()
            data[1] = x
            data[2] = y
            data = execute(data)
            if data[0] == 19690720:
                exit = True
                break
        if exit:
            break
    print(f"Answer 2: {x * 100 + y}")
