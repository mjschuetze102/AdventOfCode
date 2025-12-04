import itertools


grid = []
with open("/home/user/Downloads/advent.txt") as file:
    for line in file:
        grid.append(list(line.strip()))


def number_of_matches(grid, position):
    directions_to_check = [[[-1, -1], [-1, 0], [-1, 1]],  # noqa: E201
                           [[ 0, -1],          [ 0, 1]],  # noqa: E201
                           [[ 1, -1], [ 1, 0], [ 1, 1]]]  # noqa: E201

    height, width = len(grid), len(grid[0])
    if position[0] <= 0:
        del directions_to_check[0]

    if position[0] >= height - 1:
        del directions_to_check[-1]

    if position[1] <= 0:
        directions_to_check = [group[1:] for group in directions_to_check]

    if position[1] >= width - 1:
        directions_to_check = [group[:-1] for group in directions_to_check]

    directions_to_check = list(itertools.chain.from_iterable(directions_to_check))

    matches = 0
    for [row, col] in directions_to_check:
        matches += grid[position[0] + row][position[1] + col] == "@"

    return matches


num = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "@":
            num += number_of_matches(grid, [row, col]) < 4

print(num)
