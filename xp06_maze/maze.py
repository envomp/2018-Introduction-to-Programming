"""Find shortest way thru maze."""
import copy
import heapq


class PriorityQueue:
    """Priority que class."""

    def __init__(self):
        """Initiate."""
        self.elements = []

    def empty(self):
        """Check is queue empty."""
        return len(self.elements) == 0

    def put(self, item, priority):
        """Put element to queue."""
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        """Get element from queue."""
        return heapq.heappop(self.elements)[1]


class MazeSolver:
    """Class MazeSolver."""

    def __init__(self, maze_str: str, configuration: dict = None):
        """Initialize MazeSolver."""
        self.maze = self.maze_list(maze_str)
        self.height = len(self.maze)

        if configuration is None:
            self.configuration = {
                '#': -1,
                ' ': 1,
                '.': 2,
                '-': 5,
                'w': 10
            }
        else:
            self.configuration = configuration

    def maze_list(self, maze_str: str) -> list:
        """Make maze list from maze string."""
        out = []
        row = []
        for col in maze_str:
            if col != '\n':
                row.append(col)
            elif len(row):
                out.append(row)
                row = []
        return out

    def inside_maze(self, pos: tuple) -> tuple:
        """Check if position is inside maze area."""
        row, col = pos
        return 0 <= row < self.height and 0 <= col < len(self.maze[row])

    def is_not_wall(self, pos: tuple) -> bool:
        """Check if position is not a wall."""
        row, col = pos
        if self.maze[row][col] in self.configuration.keys():
            return self.configuration[self.maze[row][col]] >= 0
        else:
            return True

    def neighbors(self, pos: tuple):
        """Return position neighbours."""
        row, col = pos
        results = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
        results = filter(self.inside_maze, results)
        results = filter(self.is_not_wall, results)
        return results

    def heuristic(self, a: tuple, b: tuple) -> int:
        """Heuristic function to find how close a is to the goal b."""
        (row1, col1) = a
        (row2, col2) = b
        return abs(row1 - row1) + abs(col1 - col2)

    def cost(self, next: tuple) -> int:
        """Return next move cost."""
        (row, col) = next

        if self.maze[row][col] in self.configuration.keys():
            return self.configuration[self.maze[row][col]]
        else:
            return 0

    def get_shortest_path(self, start: tuple, end: tuple) -> tuple:
        """Get shortest path using A* search algorithm."""
        if not self.is_not_wall(start) or not self.is_not_wall(end):
            return (None, -1)
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == end:
                break

            for next in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(end, next)
                    frontier.put(next, priority)
                    came_from[next] = current

        path = self.make_path(came_from, start, end)
        return (path, cost_so_far[end]) if end in came_from else (None, -1)

    def make_maze_string(self, maze: list) -> str:
        """Make maze string."""
        if not len(maze):
            return ""

        maze_str = [
            maze[i][j] + '\n' if i < len(maze) - 1 and j == len(maze[i]) - 1 else maze[i][j]
            for i in range(len(maze)) for j in range(len(maze[i]))]

        return ''.join(maze_str)

    def make_path(self, came_from: dict, start: tuple, end: tuple) -> list:
        """Make path."""
        if end not in came_from:
            return None
        current = end
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()

        return path

    def show_path(self, path: list) -> list:
        """Show path on the map."""
        if path is None:
            return self.maze
        out = copy.deepcopy(self.maze)
        for pos in path:
            (row, col) = pos
            # if out[row][col] != '|':
            if True:
                out[row][col] = "*"

        return out

    def solve(self):
        """
        Solve the given maze and return the path and the cost.

        Finds the shortest path from one of the doors on the left side to the one of the doors on the right side.
        Shortest path is the one with the lowest cost.

        This method should use get_shortest_path method and return the same values.
        If there are several paths with the same cost, return any of those.

        :return: shortest_path, cost
        """
        indoors = []
        outdoors = []
        paths = []

        for row in range(self.height):
            if self.maze[row][0] == '|':
                indoors.append((row, 0))
            if self.maze[row][-1] == '|':
                outdoors.append((row, len(self.maze[row]) - 1))

        for enter in indoors:
            for exit in outdoors:
                came_from, cost = self.get_shortest_path(enter, exit)
                if came_from:
                    paths.append((came_from, cost))

        return sorted(paths, key=lambda x: (x[1], len(x[0])))[0] if len(paths) else (None, -1)


if __name__ == '__main__':
    maze = """
. |
|w|
.-|
"""
    # solver = MazeSolver(maze)
    # ll, cost = solver.get_shortest_path((0, 1), (2, 1))
    # print(solver.make_maze_string(solver.show_path(ll)))
    # expected path:[(0, 1), (0, 2), (1, 2), (2, 2), (2, 1)]
    # actual path:  [(0, 1), (0, 0), (1, 0), (2, 0), (2, 1)]
    maze = """
########
#      #
#      #
|      |
########
"""
    # solver = MazeSolver(maze)
    # assert solver.solve() == ([(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)], 6)
    # assert solver.get_shortest_path((3, 0), (3, 1)) == ([(3, 0), (3, 1)], 1)
    # assert solver.get_shortest_path((3, 0), (2, 0)) == (None, -1)

    maze = """
#####
#   #
| # #
# # |
#####
"""
    # solver = MazeSolver(maze)
    # assert solver.solve() == ([(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)], 6)

    maze = """
#####
#   |
#   |
| # #
#####
| # |
#####
"""
    solver = MazeSolver(maze)
    print(solver.solve())
    assert solver.solve() == ([(3, 0), (3, 1), (2, 1), (2, 2), (2, 3), (2, 4)], 4)
    print(solver.get_shortest_path((3, 0), (1, 4)))
    # multiple paths possible, let's just assert the cost
    assert solver.get_shortest_path((3, 0), (1, 4))[1] == 4
    assert solver.get_shortest_path((5, 0), (5, 4)) == (None, -1)
