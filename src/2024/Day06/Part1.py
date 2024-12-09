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
direction = 0

grid = []
position = [0, 0]
with open("/home/user/Downloads/advent.txt") as file:
    count = 0
    for line in file:
        grid.append([Node(cell == "#") for cell in line.strip()])

        if match := re.search("<|\\^|>|v", line):
            position = [count, match.start()]
            direction = list(directions.keys()).index(match.group())

        count += 1


def in_bounds(grid, position):
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])


while in_bounds(grid, move := [x + y for x, y in zip(position, directions[list(directions.keys())[direction]])]):
    if grid[move[0]][move[1]].can_visit():
        position = move
        grid[position[0]][position[1]].visit()

    if not grid[move[0]][move[1]].can_visit():
        direction = (direction + 1) % len(list(directions.keys()))

print(sum(cell.visited for row in grid for cell in row))
