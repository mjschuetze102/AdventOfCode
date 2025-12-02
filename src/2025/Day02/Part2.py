import re

sum = 0
with open("/home/user/Downloads/advent.txt") as file:
    for line in file.readline().strip().split(","):
        vals = line.split("-")

        for num in range(int(vals[0]), int(vals[1]) + 1):
            if re.match("^(\\d+)\\1{1,}$", str(num)):
                sum += num

    print(sum)
