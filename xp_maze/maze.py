from queue import PriorityQueue


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


if __name__ == '__main__':
    a = "".join(map(lambda x: 'K' if x else '', [True for _ in range(5)]))
    print(a)
