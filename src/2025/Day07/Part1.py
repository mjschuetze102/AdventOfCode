grid = []
with open("/home/user/Downloads/advent.txt") as file:
    while (line := file.readline().strip()):
        grid.append(list(line))

grid = grid[::2]
grid[0] = ['|' if val == 'S' else val for val in grid[0]]

count = 0
for row in range(1, len(grid)):
    locations = [col for col in range(len(grid[row])) if grid[row - 1][col] == '|']

    for location in locations:
        if grid[row][location] == '.':
            grid[row][location] = "|"

        if grid[row][location] == '^':
            grid[row][location - 1] = '|'
            grid[row][location + 1] = '|'
            count += 1

print(count)
