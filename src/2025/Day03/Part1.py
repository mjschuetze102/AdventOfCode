sum = 0
with open("/home/user/Downloads/advent.txt") as file:
    while (line := file.readline().strip()):
        i, j = 0, 0

        for index, digit in enumerate(line):
            digit = int(digit)

            if digit > i and index != len(line) - 1:
                i = digit
                j = 0
                continue

            if digit > j:
                j = digit

        sum += i * 10 + j

    print(sum)
