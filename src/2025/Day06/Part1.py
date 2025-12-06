sum = 0
equations = []
with open("/home/user/Downloads/advent.txt") as file:
    while (line := file.readline().strip()):
        equations.append(line.split())

    for i in range(len(equations[0])):
        equation = [equation[i] for equation in equations]

        sum += eval(equation[-1].join(equation[:-1]))

    print(sum)
