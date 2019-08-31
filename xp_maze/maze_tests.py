import random
import time
from queue import PriorityQueue

import pytest
import maze as lab


class MazeSolver:
    def __init__(self, maze_str: str, configuration: dict = None):
        maze = []
        if configuration is None:
            configuration = {
                ' ': 1,
                '#': -1,
                '.': 2,
                '-': 5,
                'w': 10
            }
        self.starts = []
        self.goals = []
        self.configuration = configuration
        for y, line in enumerate(maze_str.strip().split("\n")):
            row = []
            for x, c in enumerate(line):
                if c == '|':
                    row.append(0)
                    if x == 0:
                        self.starts.append((y, x))
                    else:
                        self.goals.append((y, x))
                else:
                    if c in configuration:
                        row.append(configuration[c])
            maze.append(row)

        self.maze = maze

    def dist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, cell):
        result = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                if y == 0 and x == 0: continue
                if y != 0 and x != 0: continue
                if 0 <= cell[0] + y < len(self.maze) and 0 <= cell[1] + x < len(self.maze[cell[0] + y]):
                    result.append((cell[0] + y, cell[1] + x))
        return result

    def get_shortest_path(self, start, goal):
        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            # print(cost_so_far)
            current = frontier.get()[1]
            # print("current", current)

            if current == goal:
                break

            for next in self.get_neighbors(current):
                # print("next", next)
                if self.maze[next[0]][next[1]] == -1: continue
                new_cost = cost_so_far[current] + self.maze[next[0]][next[1]]
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.dist(goal, next)
                    frontier.put((priority, next))
                    came_from[next] = current

        # print(came_from)
        if goal not in came_from:
            return None, -1
        current = goal
        # path = [(current[1], len(self.maze) - current[0] - 1)]
        path = [current]
        while current != start:
            current = came_from[current]
            # path.append((current[1], len(self.maze) - current[0] - 1))
            path.append(current)

        # print(cost_so_far)
        # print(came_from)
        path.reverse()
        return path, cost_so_far[goal]

    def solve(self):
        starts = self.starts
        goals = self.goals

        best_cost = None
        best_path = None
        for start in starts:
            for goal in goals:
                # print(f"start: {start} goal: {goal}:")
                path, cost = self.get_shortest_path(start, goal)
                # print(f" cost: {cost}, path:{path}")
                if path is not None and (best_cost is None or cost < best_cost):
                    best_cost = cost
                    best_path = path
        return best_path, best_cost if best_cost is not None else -1


def _maze_solve(maze):
    m = lab.MazeSolver(maze)
    return m.solve()


@pytest.mark.timeout(1.0)
def test_medium():
    labyrinth = """
#######################
# #    #     # #      #
#   #### ###   # ## ###
| #  # # # # # #    # |
###    #   # # # #    #
#    #   # # #   #  # #
#######################
    """
    assert len(_maze_solve(labyrinth)[0]) == 39


@pytest.mark.timeout(1.0)
def test_agoraphobia():
    labyrinth = """
#######################
#                     #
#                     #
|                     |
#                     #
#                     #
#######################
    """
    assert len(_maze_solve(labyrinth)[0]) == 23


@pytest.mark.timeout(1.0)
def test_large():
    labyrinth = """
#######################
# #    #     # #      #
#   #### ###   # ## ###
| #  # # # # # #    # #
###    #   # # # #    #
#    #   # # #   #  # #
########## ############
#              #      #
# ##### #### ###### ###
# # #   #       #    ##
#   # #   # # #   #   |
#######################
    """
    assert len(_maze_solve(labyrinth)[0]) == 36


@pytest.mark.timeout(1.0)
def test_ridiculously_small():
    labyrinth = """
##
||
##
    """
    assert len(_maze_solve(labyrinth)[0]) == 2


@pytest.mark.timeout(1.0)
def test_no_exit():
    labyrinth = """
###
| #
###
    """
    assert _maze_solve(labyrinth) == (None, -1)


@pytest.mark.timeout(1.0)
def test_no_path():
    labyrinth = """
###
|#|
###
    """
    assert _maze_solve(labyrinth) == (None, -1)


@pytest.mark.timeout(1.0)
def test_multiple_correct_exits():
    labyrinth = """
############
# #    #   |
#   #### ###
| #  # # # |
###    #   #
|    #   # |
############
    """
    shortest = _maze_solve(labyrinth)

    assert len(shortest[0]) == 16
    assert shortest[0] in (
        [(5, 0), (5, 1), (5, 2), (5, 3), (4, 3), (4, 4), (4, 5), (4, 6), (5, 6), (5, 7), (5, 8), (4, 8), (4, 9),
         (4, 10), (3, 10), (3, 11)],
        [(5, 0), (5, 1), (5, 2), (5, 3), (4, 3), (4, 4), (4, 5), (4, 6), (5, 6), (5, 7), (5, 8), (4, 8), (4, 9),
         (4, 10), (5, 10), (5, 11)],
        [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (5, 6), (5, 7), (5, 8), (4, 8), (4, 9),
         (4, 10), (5, 10), (5, 11)],
    ), f"shortest: {shortest}"


@pytest.mark.timeout(1.0)
def test_multiple_correct_paths():
    labyrinth = """
####
|  #
#  |
|  #
#  |
|  #
####
    """
    shortest = _maze_solve(labyrinth)

    assert len(shortest[0]) == 5
    assert shortest[0] in (
        [(1, 0), (1, 1), (2, 1), (2, 2), (2, 3)],
        [(1, 0), (1, 1), (1, 2), (2, 2), (2, 3)],
        [(3, 0), (3, 1), (3, 2), (2, 2), (2, 3)],
        [(3, 0), (3, 1), (2, 1), (2, 2), (2, 3)],
        [(3, 0), (3, 1), (4, 1), (4, 2), (4, 3)],
        [(3, 0), (3, 1), (3, 2), (4, 2), (4, 3)],
        [(5, 0), (5, 1), (5, 2), (4, 2), (4, 3)],
        [(5, 0), (5, 1), (4, 1), (4, 2), (4, 3)]
    )


@pytest.mark.timeout(10.0)
def test_huge_thing():
    labyrinth = """
##################################################
#                                ##   ##### ##   #
| #### ### #### #### # # # # ### #  #      # ##  #
## ##### #### ### ##### ### ## # # #  #######  # #
#                              #   # #### #####  #
# ########################     ##### #### #   #  #
#                      # #     #        # # # #  #
###################### # #     # ###### ### # #  #
|     #     ##    #### # #     #    ###     # #  #
######### ####### #### # #     # ############ #  #
##                   # # #    #        #    # #  #
## ########### ##### # # ##    #### ####    # #  #
##      #            # #####    ### ####    # #  #
## ########### ####### #    #   ##    #     # #  #
##          ## #    ## ###  ##  ##### #     # #  #
| ##### ### ## #  # ## # # #   #      #     # #  #
# #   #     ## ## #    # # ##  ##   #########  ###
# # # ##### ## ####### ###  ##   #############   #
#   #       ##         #  ######                 |
##################################################

    """
    shortest = _maze_solve(labyrinth)

    assert len(shortest[0]) == 82
    assert shortest[0] in (
        [(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11),
         (1, 12),
         (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (1, 24),
         (1, 25), (1, 26), (1, 27), (1, 28), (1, 29), (1, 30), (1, 31), (1, 32), (2, 32), (3, 32), (4, 32), (4, 33),
         (4, 34), (3, 34), (2, 34), (2, 35), (1, 35), (1, 36), (1, 37), (2, 37), (3, 37), (3, 36), (4, 36), (5, 36),
         (6, 36), (6, 37), (6, 38), (6, 39), (7, 39), (8, 39), (8, 40), (8, 41), (8, 42), (8, 43), (7, 43), (6, 43),
         (5, 43), (5, 44), (5, 45), (6, 45), (7, 45), (8, 45), (9, 45), (10, 45), (11, 45), (12, 45), (13, 45),
         (14, 45),
         (15, 45), (16, 45), (16, 46), (17, 46), (17, 47), (17, 48), (18, 48), (18, 49)],
        [(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11),
         (1, 12),
         (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (1, 24),
         (1, 25), (1, 26), (1, 27), (1, 28), (1, 29), (1, 30), (1, 31), (1, 32), (2, 32), (3, 32), (4, 32), (4, 33),
         (4, 34), (3, 34), (2, 34), (2, 35), (1, 35), (1, 36), (1, 37), (2, 37), (3, 37), (3, 36), (4, 36), (5, 36),
         (6, 36), (6, 37), (6, 38), (6, 39), (7, 39), (8, 39), (8, 40), (8, 41), (8, 42), (8, 43), (7, 43), (6, 43),
         (5, 43), (5, 44), (5, 45), (6, 45), (7, 45), (8, 45), (9, 45), (10, 45), (11, 45), (12, 45), (13, 45),
         (14, 45),
         (15, 45), (16, 45), (16, 46), (17, 46), (18, 46), (18, 47), (18, 48), (18, 49)],
        [(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11),
         (1, 12),
         (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (1, 24),
         (1, 25), (1, 26), (1, 27), (1, 28), (1, 29), (1, 30), (1, 31), (1, 32), (2, 32), (3, 32), (4, 32), (4, 33),
         (4, 34), (3, 34), (2, 34), (2, 35), (1, 35), (1, 36), (1, 37), (2, 37), (3, 37), (3, 36), (4, 36), (5, 36),
         (6, 36), (6, 37), (6, 38), (6, 39), (7, 39), (8, 39), (8, 40), (8, 41), (8, 42), (8, 43), (7, 43), (6, 43),
         (5, 43), (5, 44), (5, 45), (6, 45), (7, 45), (8, 45), (9, 45), (10, 45), (11, 45), (12, 45), (13, 45),
         (14, 45),
         (15, 45), (16, 45), (16, 46), (17, 46), (17, 47), (18, 47), (18, 48), (18, 49)],
    )


@pytest.mark.timeout(2.0)
def test_huge_thing_with_some_walls():
    labyrinth = """
##################################################
#                                                |
| ################################################
################################################ |
###############################################  #
############################################### ##
############################################### ##
############################################### ##
|                                               ##
############################################### ##
############################################### ##
############################################### ##
############################################### ##
############################################### ##
############################################### ##
|                                               ##
##################################################
##################################################
##################################################
##################################################

    """
    shortest = _maze_solve(labyrinth)

    assert len(shortest[0]) == 51
    assert shortest[0] == [(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
                           (1, 10),
                           (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 20),
                           (1, 21), (1, 22), (1, 23), (1, 24), (1, 25), (1, 26), (1, 27), (1, 28), (1, 29), (1, 30),
                           (1, 31), (1, 32), (1, 33), (1, 34), (1, 35), (1, 36), (1, 37), (1, 38), (1, 39), (1, 40),
                           (1, 41), (1, 42), (1, 43), (1, 44), (1, 45), (1, 46), (1, 47), (1, 48), (1, 49)]


@pytest.mark.timeout(5.0)
def test_huge_thing_no_path():
    labyrinth = """
##################################################
#                                                |
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
##################################################
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
|                                                #
##################################################
    """
    shortest = _maze_solve(labyrinth)

    assert shortest == (None, -1)


def test_different_weights_simple():
    maze = """
##########
|........|
##########
"""
    shortest = _maze_solve(maze)

    # assert shortest == (, -1)


@pytest.mark.timeout(5.0)
def test_long_path_binary_configuration():
    # by Enrico Vompa
    maze = """
000000000000000000000
011111110111011100110
010000010101110100100
011101110100001111100
000101000100110000100
|1110111111110000011|
000000000000000000000
"""
    configuration = {
        "0": -1,
        "1": 1,
        "2": 2,
        "5": 5,
        "10": 10
    }

    solver = lab.MazeSolver(maze, configuration)
    assert solver.solve() == (
    [(5, 0), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
     (1, 6), (1, 7), (2, 7), (3, 7), (3, 6), (3, 5), (4, 5), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 9), (3, 9),
     (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (2, 12), (2, 13), (1, 13), (1, 14), (1, 15), (2, 15), (3, 15), (3, 16),
     (3, 17), (3, 18), (4, 18), (5, 18), (5, 19), (5, 20)], 45)


@pytest.mark.timeout(5.0)
def test_one_path_huge_cost_many_obstacles_special_configuration():
    # by Enrico Vompa
    maze = """
#####################
|https://www.ttu.ee/|
#####################
"""
    configuration = {
        ' ': 1,
        '#': -1,
        '.': 2,
        't': 10,
        'p': 20,
        's': 40,
        'w': 50,
        'ü': 120,
        ':': 199,
        '/': 200,
        'e': 3220,
        'h': 9780,
        'u': 100080,
    }
    solver = lab.MazeSolver(maze, configuration)
    assert solver.solve() == (
    [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13),
     (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 20)], 117353)


@pytest.mark.timeout(5.0)
def test_paths_same_length_different_cost():
    # by Enrico Vompa
    maze = """
#####################
##. ... w . . # . . |
##. ..w - # ..# . . #
|. - w    #. . . . .|
##. ..w - #.. # . . #
##. ... w . . # . . |
#####################
"""
    solver = lab.MazeSolver(maze)
    assert solver.solve() in \
           (
               ([(3, 0), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (3, 8),
                 (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15),
                 (3, 16), (3, 17), (3, 18), (3, 19), (3, 20)], 38),
               ([(3, 0), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (3, 8),
                 (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (2, 11), (2, 12), (3, 12), (3, 13), (3, 14), (3, 15),
                 (3, 16), (3, 17), (3, 18), (3, 19), (3, 20)], 38)
           )


@pytest.mark.timeout(5.0)
def test_ascii_version_of_agos_profile_picture():
    maze = """
##########################################
#NMMMMN88?+?+=,.,=NZ??+=~~~~~,,~+++::~~~~#
|MMN8O7+:~??+=::8O7?+?+=~~~::,,~=++::::::#
#O77I?+=~+++++:,~?+=+?+~~~~::,,:+?+:::::~#
#8IIII+=??++++~=+====++~~~::::,~+N+:::::~#
#O?~~+?77++++===?NZZ$$$~~~:::,,:+::::::::#
#MMZ??$D7++====O?I$$DO8Z~:::::,:,,:::::::#
#MMMMMNN$?+===I::~~==+ZZ7:::::.,,,.::::::#
#NMMMMMMNZ?===?::~~=??+8O:::::.,.,,::::::#
#NNNMMMMMM8?==+==I?7I?++?~::::,,.,,::::::#
#NNMMMMMM8$I???=+:=?==+=?:::::,,,.,::::::#
#DDNMMMMM$?I???=~=~?+I+=D:::::,,,.,,:::::#
#DDNMMMMM$?????=:~:=+++++::::::,,.,,,::::#
#D8NMMMMNOII???++::~?I??,M:::::::,,.,::::#
#88DNMMMM87I???++?::==:MMMM::::::,,.,::::#
#88NMMMMMD$77II??I:,.~NMMDNND:,::,,,,::::#
#D8DNMMMMDO$Z$$IIM,.:NNMDDDNMN=::::,,::::#
#DD8NMMMNN8OOZ$DMN.,DDNDDMMMMMMM::,,,::::#
#DDDNMMMNN8$$MNMO.,DDDDNMMMMMMMM::::,::::#
#D8DNMMMNN8ZZDNDM.ND888DMMMMMMMM:::::::::#
#NDNMMMMMND8DM8O,:=,MMDDMMMMMMMM~::::::::#
#NNNMNDDD88DNND?,,,~NMDDNMMMMMMM:::::~:::#
#NNND888888MMDOMZINNN8NDNMMMMMMM:::::~:::#
#D8888OO8MMMMMN.7~MM$O8DNMMMMMMM:::::~:::#
#88OOOZDNNN88..+:::IO8NNMMMMMMMM~::::~::~#
#OOZZZZDNMD8~.~?~NODDDNMMMMMMMMM:~:::::~~#
#ZZZZZZMD8DDI?:MDDDNMMMMMMMMMMMO~~::::~~:#
#OOZZZZMNMMMNMMMNDNMMMMMMMMMMMM=~~~:~~~~=#
#OOOOOZZNMMO7DNNMNMMMMMMMMMMMMM=~~=~~~~~~#
#8OOOZOZZZZ$$NMMMMMMMMMMMMMMMM==~~~~?~~=~#
#OZZZZZZ$$$7NNNOMMMMMMMMMMMMMMM~~~==+~=~=#
#8OOOZOOO$$$NMNNNMMMMMMMMMMMMMM+~~==++~~=#
#O88ZOOZOO7$NMNMNMMMMMMMMMMMMMM++==++?===#
#8OO8888OO$ZMMMMMMMMMMMMMMMMMMMD?+++++?++#
#OZZO888OZ$NMMMMMMMMMMMMMMMMMMMMI?I+?++?+#
#8O8888OO$$MNMMMMMMMMMMMMMMMMMMMM7II?=+I+#
#DDDDZZOO$NMMMMMMMMMMMMMMMMMMMMMM$777?+I7#
#D888OZZOZMMMMMMMMMMMMMMMMMMMMMMMM7$ZI+?+|
#8NNOO8DZZMMMMMMMMMMMMMMMMMMMMMMMM$$777+7#
##########################################
"""
    configuration = {
        '#': -1,
        'N': 91,
        'M': 76,
        '8': 63,
        '?': 28,
        '+': 19,
        '=': 3,
        ',': 54,
        '.': 47,
        'Z': 3,
        '~': 58,
        ':': 48,
        'O': 98,
        '7': 4,
        'I': 51,
        '$': 22,
        'D': 51
    }
    solver = lab.MazeSolver(maze, configuration)
    assert solver.solve()[1] == 1869


_start_time = None


def _start_timer():
    global _start_time
    _start_time = time.time()


def _time(msg):
    print(time.time() - _start_time, msg)


def _test_random(y_len, x_len, nr_of_doors, configuration):
    _start_timer()
    maze = _random_map_maker(y_len, x_len, nr_of_doors, configuration)
    _time("Maze created")
    student_solution = lab.MazeSolver(maze, configuration).solve()
    _time("Student solver done")
    real_solution = MazeSolver(maze, configuration).solve()
    _time("Real solver done")
    assert real_solution[1] == student_solution[1]


@pytest.mark.timeout(3.0)
def test_small_random_map_special_configuration():
    """maze."""
    configuration = {
        "#": -1,
        "f": 1,
        "x": 2,
        "4": 3,
        "!": 4,
        "¤": 5,
        "S": 6,
        "0": 7,
        "%": 8
    }
    _test_random(20, 20, 10, configuration)


@pytest.mark.timeout(5.0)
def test_medium_random_map_special_configuration():
    """maze."""
    configuration = {
        "#": -1,
        "f": 1,
        "x": 2,
        "4": 3,
        "!": 4,
        "¤": 5,
        "S": 6,
        "0": 7,
        "%": 8
    }
    _test_random(40, 40, 5, configuration)


@pytest.mark.timeout(5.0)
def test_big_random_map_special_configuration():
    """maze."""
    configuration = {
        "#": -1,
        "f": 1,
        "x": 2,
        "4": 3,
        "!": 4,
        "¤": 5,
        "S": 6,
        "0": 7,
        "%": 8
    }
    _test_random(60, 60, 4, configuration)


@pytest.mark.weight(5)
@pytest.mark.timeout(15.0)
def test_enormous_random_map_special_configuration():
    """maze."""
    configuration = {
        "#": -1,
        "f": 1,
        "x": 2,
        "4": 3,
        "!": 4,
        "¤": 5,
        "S": 6,
        "0": 7,
        "%": 8
    }
    _test_random(100, 100, 4, configuration)


def _random_map_maker(y_len, x_len, nr_of_doors, configuration=None):
    """random."""
    if configuration is None:
        configuration = {
            ' ': 1,
            '#': -1,
            '.': 2,
            '-': 5,
            'w': 10
        }
    config = list(configuration.keys())
    # config = ["#", "f", "x", "4", "!", "¤", "S", "0", "%"]
    test_map_y_coord = ""
    for y in range(y_len):
        for x in range(x_len):
            if (x == 0 or x == x_len - 1) and y % (y_len / nr_of_doors) == 0 and y != 0 and y != y_len and x != x_len:
                test_map_y_coord += "|"
            elif y == 0 or y == y_len - 1 or x == 0 or x == x_len - 1:
                test_map_y_coord += "#"
            else:
                a = config[random.randint(0, len(config) - 1)]
                test_map_y_coord += a
        test_map_y_coord += "\n"
    return test_map_y_coord


# ====================== PATH TESTS ==============

@pytest.mark.weight(1)
@pytest.mark.timeout(1.0)
def test_0_path():
    maze = """
.  
|w|
.-|
"""
    all_points = [(x, y) for y in range(3) for x in range(3)]
    _test_all_the_paths(maze, paths=[(p1, p1) for p1 in all_points])


def _test_all_the_paths(maze, number_of_paths=0, paths=None, debug=False):
    student_solver = lab.MazeSolver(maze)
    test_solver = MazeSolver(maze)
    if paths is None:
        maze_rows = maze.strip().split("\n")
        all_the_points = [(x, y) for y in range(len(maze_rows)) for x in range(len(maze_rows[y]))]
        paths = [(p1, p2) for p1 in all_the_points for p2 in all_the_points if p1 != p2]
        if number_of_paths == 0:
            # try everything
            # print(all_the_points)
            # print(paths)
            pass
        else:
            # take random N paths
            # paths = [(random.) for _ in range(number_of_paths)]
            paths = random.sample(paths, k=number_of_paths)

    for p1, p2 in paths:
        if debug: print(p1, p2)
        # check only the cost
        expected = test_solver.get_shortest_path(p1, p2)
        expected_cost = expected[1]
        actual = student_solver.get_shortest_path(p1, p2)
        actual_cost = actual[1]
        assert expected_cost == actual_cost, f"p1 {p1} -> p2 {p2}\nMaze:\n{maze}\nexpected path:{expected[0]}\nactual path:  {actual[0]}\n"


@pytest.mark.timeout(5.0)
@pytest.mark.weight(5)
def test_custom_path_small():
    maze = """
.  
|w|
.-|
"""
    _test_all_the_paths(maze)


@pytest.mark.timeout(5.0)
@pytest.mark.weight(5)
def test_custom_path_small_random():
    for _ in range(10):
        maze = _random_map_maker(10, 10, 2)
        print(maze)
        print()
        _test_all_the_paths(maze, 10, debug=True)


@pytest.mark.timeout(5.0)
@pytest.mark.weight(5)
def test_custom_path_large_random():
    for _ in range(100):
        maze = _random_map_maker(10, 10, 2)
        _test_all_the_paths(maze, 10)
