numbers = []
with open("/home/user/Downloads/advent.txt") as file:
    for line in file:
        numbers = [int(x) for x in line.split(" ")]


def change_number(number):
    length = len(str(number))

    if length % 2 == 0:
        mid = length // 2
        string = str(number)
        return int(string[:mid]), int(string[mid:])

    return [1] if number == 0 else [number * 2024]


for _ in range(25):
    numbers = [x for num in numbers for x in change_number(num)]

print(len(numbers))
