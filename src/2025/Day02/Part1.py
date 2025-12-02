sum = 0
with open("/home/user/Downloads/advent.txt") as file:
    for line in file.readline().strip().split(","):
        vals = line.split("-")

        for num in range(int(vals[0]), int(vals[1]) + 1):
            num = str(num)

            if num[:len(num) // 2] == num[len(num) // 2:]:
                sum += int(num)

    print(sum)
