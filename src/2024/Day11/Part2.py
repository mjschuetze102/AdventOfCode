from collections import defaultdict


numbers = defaultdict(int)
with open("/home/user/Downloads/advent.txt") as file:
    for line in file:
        for x in line.split(" "):
            numbers[int(x)] += 1


def change_number(number):
    length = len(str(number))

    if length % 2 == 0:
        mid = length // 2
        string = str(number)
        return int(string[:mid]), int(string[mid:])

    return [1] if number == 0 else [number * 2024]


for _ in range(75):
    temp = defaultdict(int)

    for num in numbers.keys():
        val = numbers[num]
        for x in change_number(num):
            temp[x] += val

    numbers = temp

print(sum(numbers.values()))
