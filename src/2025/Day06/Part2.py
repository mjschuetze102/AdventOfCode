sum = 0
equations = []
with open("/home/user/Downloads/advent.txt") as file:
    while (line := file.readline()):
        equations.append(line)

    op_positions = [index for index, char in enumerate(equations[-1]) if not char.isspace()] + [len(equations[0])]

    equations = [[equation[op_positions[i]:op_positions[i+1] - 1] for equation in equations] for i in range(len(op_positions) - 1)]

    terms = []
    for equation in equations:
        sum += eval(equation[-1].join(["".join([term[i] for term in equation[:-1]]).strip() for i in range(len(equation[0]))]))

    print(sum)
