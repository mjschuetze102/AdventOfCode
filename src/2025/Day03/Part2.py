sum = 0
with open("/home/user/Downloads/advent.txt") as file:
    while (line := file.readline().strip()):
        values = [0] * 12

        for index, digit in enumerate(line):
            digit = int(digit)

            for i in range(len(values)):
                if len(line) - index < 12 - i:
                    continue

                if digit > values[i]:
                    values[i] = digit
                    values = values[:i + 1] + [0] * (12 - 1 - i)
                    break

        sum += int("".join(map(str, values)))

    print(sum)
