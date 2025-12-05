ranges = []
with open("/home/user/Downloads/advent.txt") as file:
    while (line := file.readline().strip()):
        if (line == ""):
            break

        ranges.append(list(map(int, line.split("-"))))

    ranges.sort(key=lambda x: x[0])

    i = 0
    while i < len(ranges) - 1:
        modified = False

        if ranges[i][0] <= ranges[i + 1][0] and ranges[i][1] >= ranges[i + 1][0]:
            ranges[i + 1][0] = ranges[i][0]
            modified = True

        if ranges[i][0] <= ranges[i + 1][1] and ranges[i][1] >= ranges[i + 1][1]:
            ranges[i + 1][1] = ranges[i][1]
            modified = True

        if modified:
            del ranges[i]
        else:
            i += 1

    print(sum([range[1] - range[0] + 1 for range in ranges]))
