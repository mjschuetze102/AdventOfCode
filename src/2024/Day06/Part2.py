import re


class Node:

    def __init__(self, is_wall):
        self._wall = is_wall
        self._visited = False

    @property
    def visited(self):
        return self._visited

    def visit(self):
        self._visited = True

    def can_visit(self):
        return not self._wall

    def __str__(self):
        if self._wall:
            return "#"

        if self._visited:
            return "X"

        return "."

    def __repr__(self):
        return self.__str__()


directions = {
    "<": [ 0, -1],  # noqa: E201
    "^": [-1,  0],  # noqa: E201
    ">": [ 0,  1],  # noqa: E201
    "v": [ 1,  0]   # noqa: E201
}
direction = saved_dir = 0

grid = []
position = saved_pos = [0, 0]
with open("/home/user/Downloads/advent.txt") as file:
    count = 0
    for line in file:
        grid.append([Node(cell == "#") for cell in line.strip()])

        if match := re.search("<|\\^|>|v", line):
            position = saved_pos = [count, match.start()]
            direction = saved_dir = list(directions.keys()).index(match.group())

        count += 1


def in_bounds(grid, position):
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])


while in_bounds(grid, move := [x + y for x, y in zip(position, directions[list(directions.keys())[direction]])]):
    if grid[move[0]][move[1]].can_visit():
        position = move
        grid[position[0]][position[1]].visit()

    if not grid[move[0]][move[1]].can_visit():
        direction = (direction + 1) % len(list(directions.keys()))

loops = []
visited = [[row, col] for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col].visited]
for cell in visited:
    grid[cell[0]][cell[1]] = Node(True)

    position, direction = saved_pos, saved_dir
    moves, last_moves = [], [position] * 3
    while in_bounds(grid, move := [x + y for x, y in zip(position, directions[list(directions.keys())[direction]])]):
        if grid[move[0]][move[1]].can_visit():
            position = move
            last_moves.pop(0)
            last_moves.append(position)

            if len(moves) >= len(last_moves) and any(moves[i: i + len(last_moves)] == last_moves for i in range(len(moves) - len(last_moves) + 1)):
                loops.append(cell)
                break

            moves.append(position)

        if not grid[move[0]][move[1]].can_visit():
            direction = (direction + 1) % len(list(directions.keys()))

    grid[cell[0]][cell[1]] = Node(False)

print(len(loops))
