count = 0
ranges = []
with open("/home/user/Downloads/advent.txt") as file:
    while (line := file.readline().strip()):
        if (line == ""):
            break

        ranges.append(list(map(int, line.split("-"))))

    while (line := file.readline().strip()):
        line = int(line)
        for range in ranges:
            if line >= range[0] and line <= range[1]:
                count += 1
                break

    print(count)
