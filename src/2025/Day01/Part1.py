num = 50
count = 0
with open("/home/user/Downloads/advent.txt") as file:
    while (line := file.readline().strip()):
        num += int(line[1:]) if line[0] == 'R' else -int(line[1:])

        if num <= 0 or num >= 100:
            num %= 100

        if num == 0:
            count += 1

    print(count)
