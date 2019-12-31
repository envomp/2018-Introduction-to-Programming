"""Minesweeper has to swipe the mines."""
import copy


def create_minefield(height: int, width: int) -> list:
    """
    Create and return minefield.

    Minefield must be height high and width wide. Each position must contain single dot (`.`).
    :param height: int
    :param width: int
    :return: list
    """
    return [['.' for col in range(width)] for row in range(height)]


def add_mines(minefield: list, mines: list) -> list:
    """
    Add mines to a minefield and return minefield.

    Minefield must be length long and width wide. Each non-mine position must contain single dot.
    If a position is empty ("."), then a small mine is added ("x").
    If a position contains small mine ("x"), a large mine is added ("X").
    Mines are in a list.
    Mine is a list. Each mine has 4 integer parameters in the format [N, S, E, W].
        - N is the distance between area of mines and top of the minefield.
        - S ... area of mines and bottom of the minefield.
        - E ... area of mines and right of the minefield.
        - W ... area of mines and left of the minefield.

    :param mf: minefield list
    :param mines: list
    :return: list
    """
    if not len(minefield):
        return []

    if not len(mines):
        return minefield

    height = len(minefield)
    width = len(minefield[0])

    # minefield = [[minefield[row][col] for col in range(width)] for row in range(height)]
    minefield = copy.deepcopy(minefield)

    for mine in mines:
        if 0 <= mine[0] < height and 0 <= mine[1] < height and 0 <= mine[2] < width and 0 <= mine[3] < width \
                and height - (mine[1] + mine[0]) >= 1 and width - (mine[3] + mine[2]) >= 1:
            for row in range(mine[0], height - mine[1]):
                for col in range(mine[3], width - mine[2]):
                    minefield[row][col] = 'x' if minefield[row][col] == '.' else 'X'

    return minefield


def get_minefield_string(minefield: list) -> str:
    """
    Return minefield's string representation.

    :param minefield:
    :return:
    """
    if not len(minefield):
        return ""

    minefield_str = [
        minefield[i][j] + '\n' if i < len(minefield) - 1 and j == len(minefield[i]) - 1 else minefield[i][j]
        for i in range(len(minefield)) for j in range(len(minefield[i]))]

    return ''.join(minefield_str)


def calc_mine_count_near(minefield: list, row: int, col: int) -> int:
    """Calculate mine count near given cell.

    :param minefield: minefield list
    :param row: row
    :param col: col
    :return: mine count
    """
    height = len(minefield)
    width = len(minefield[0])

    prev_row = row if row == 0 else row - 1
    next_row = row if row == height - 1 else row + 1
    prev_col = col if col == 0 else col - 1
    next_col = col if col == width - 1 else col + 1
    mines = 0

    for i in range(prev_row, next_row + 1):
        for j in range(prev_col, next_col + 1):
            if minefield[i][j] == 'x' or minefield[i][j] == 'X':
                mines += 1

    return mines


def calculate_mine_count(minefield: list) -> list:
    """
    For each cell in minefield, calculate how many mines are nearby.

    This function cannot modify the original list.
    So, the result should be a new list (or copy of original).

    :param minefield:
    :return:
    """
    if not len(minefield):
        return []

    height = len(minefield)
    width = len(minefield[0])

    # mf = [[minefield[row][col] for col in range(width)] for row in range(height)]
    mf = copy.deepcopy(minefield)

    for row in range(height):
        for col in range(width):
            if mf[row][col] == '.' or mf[row][col] == '#':
                mf[row][col] = str(calc_mine_count_near(mf, row, col))

    return mf


def walk(minefield, moves, lives) -> list:
    """
    Make moves on the minefield.

    Starting position is marked by #.
    There is always exactly one # on the field.
    The position you start is an empty cell (".").

    Moves is a list of move "orders":
    N - up,
    S - down,
    E - right,
    W - left.

    :param minefield:
    :param moves:
    :param lives:
    :return:
    """
    directions = {
        "S": (1, 0),
        "N": (-1, 0),
        "E": (0, 1),
        "W": (0, -1)
    }

    if not len(minefield):
        return []

    height = len(minefield)
    width = len(minefield[0])

    # minefield = [[minefield[row][col] for col in range(width)] for row in range(height)]
    minefield = copy.deepcopy(minefield)

    start_row, start_col = find_minesweeper(minefield)

    for move in moves:
        test_row = start_row + directions[move][0]
        test_col = start_col + directions[move][1]

        if height > test_row >= 0 and width > test_col >= 0:  # inside borders
            if minefield[test_row][test_col] == "x":
                if calc_mine_count_near(minefield, start_row, start_col) >= 5:
                    if lives:
                        lives -= 1
                    else:
                        return minefield
                minefield[test_row][test_col] = "."
            else:
                if minefield[test_row][test_col] == "X":
                    if lives:
                        lives -= 1
                    else:
                        return minefield
                minefield[start_row][start_col] = '.'
                minefield[test_row][test_col] = "#"
                start_row += directions[move][0]
                start_col += directions[move][1]

    return minefield


def find_minesweeper(minefield: list):
    """Find minesweeper position.

    :param minefield:
    :return: row, col
    """
    height = len(minefield)
    width = len(minefield[0])

    for row in range(height):
        for col in range(width):
            if minefield[row][col] == '#':
                return row, col

    return None


if __name__ == '__main__':
    minefield_a = create_minefield(4, 3)
    print(minefield_a)  # ->
    """
    [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    """

    minefield_a = add_mines(minefield_a, [[0, 3, 2, 0], [2, 1, 0, 1]])
    print(minefield_a)  # ->
    """
    [
        ['x', '.', '.'],
        ['.', '.', '.'],
        ['.', 'x', 'x'],
        ['.', '.', '.']
    ]
    """

    print(get_minefield_string(minefield_a))
    minefield_ac = calculate_mine_count(minefield_a)
    print(get_minefield_string(minefield_ac))

    minefield_b = create_minefield(8, 7)
    minefield_b = add_mines(minefield_b, [[2, 1, 3, 2], [0, 5, 3, 0]])

    print(minefield_b)  # ->
    """
    [
        ['x', 'x', 'x', 'x', '.', '.', '.'],
        ['x', 'x', 'x', 'x', '.', '.', '.'],
        ['x', 'x', 'X', 'X', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.']
    ]
    """

    minefield_c = create_minefield(5, 5)
    minefield_c = add_mines(minefield_c, [[0, 0, 2, 2]])
    print(minefield_c)  # ->
    """
    [
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.']
    ]
    """

    mf = [['.', '.', '.', '.'], ['.', '.', 'x', '.'], ['X', '.', 'X', '.'], ['x', '.', '.', 'X']]
    print(calculate_mine_count(mf))

    """
    [
        ['0', '1', '1', '1'],
        ['1', '3', 'x', '2'],
        ['X', '4', 'X', '3'],
        ['x', '3', '2', 'X']
    ]
    """

    mf = copy.deepcopy(minefield_c)
    mf[0][0] = '#'
    print(get_minefield_string(walk(mf, "WEESE", 2)))
    """
    .....
    .#...
    ..x..
    ..x..
    ..x..
    """

    mf = create_minefield(3, 5)
    mf = add_mines(mf, [[0, 0, 1, 2]])
    mf = add_mines(mf, [[0, 1, 1, 1]])
    print(get_minefield_string(mf))
    """
    .xXX.
    .xXX.
    ..xx.
    """
    mf[0][4] = "#"
    mf = walk(mf, "WSSWN", 2)
    print(get_minefield_string(mf))
    """
    .xX..
    .xX#.
    ..x..
    """

    mv = create_minefield(20, 20)
    mv = add_mines(mv, [[0, 7, 4, 13], [19, 0, 12, 4], [17, 2, 0, 3], [8, 10, 3, 13], [7, 7, 2, 11]])
    print(get_minefield_string(mv))
    print()
    print(get_minefield_string(calculate_mine_count(mv)))
    print()
    mv[6][12] = '#'
    print(get_minefield_string(walk(mv, "WEESESENNNWWS", 7)))
