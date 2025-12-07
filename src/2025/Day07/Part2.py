grid = []
with open("/home/user/Downloads/advent.txt") as file:
    while (line := file.readline().strip()):
        grid.append(list(line))

grid = grid[::2]

paths = [0] * len(grid[0])
paths[grid[0].index('S')] = 1

for row in range(1, len(grid)):
    locations = [col for col in range(len(paths)) if paths[col] != 0]

    for location in locations:
        if grid[row][location] == '^':
            paths[location - 1] += paths[location]
            paths[location + 1] += paths[location]
            paths[location] = 0

print(sum(paths))
