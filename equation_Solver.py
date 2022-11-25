def equation_solver(equation):
    k, start, end = 0, 0, 0
    number, temp, temp2 = [], [], []
    equation = list(equation)
    eq = equation[equation.index("=")::-1][::-1]
    output = equation[equation.index("=") + 1::]
    for i in range(len(eq)):
        temp.append(eq[i])  # all values of the loop
        if (eq[i + 1] == "+" or eq[i + 1] == "-" or eq[i - 1] == "+" or eq[i - 1] == "-") and (
                eq[i + 1] != "*" and eq[i - 1] != "*"):  # the number with this conditions
            temp3 = []
            j = i
            if all(item.isdigit() for item in temp):  # specific problem
                number = temp
                end = len(temp)
                break
            while eq[j] != "*" and eq[j] != '=':  # loop to solve -5(5) * x + (3)3 =
                temp3.append(eq[j])
                j += 1
                if eq[j] == "*" or eq[j] == "=":
                    temp3.append(eq[j])
            if temp3[len(temp3) - 1] != "*":  # start adding
                if eq[i - 1] == "-":
                    number.append("-")
                    k = 1
                h = i
                while eq[h] != "=" and eq[h] != "+" and eq[h] != "-" and eq[h] != "*":
                    number.append(eq[h])
                    h += 1
                start = i - k
                end = h
                break
    if len(number) == 0:  # simple equation problem
        for d in eq:
            if d.isdigit() or d == "+" or d == "-":
                temp2.append(d)
        if temp2[len(temp2) - 1] == "+" or temp2[len(temp2) - 1] == "-":
            temp2.pop()
        temp2 = "".join(temp2)
        output = "".join(output)
        return eval(output) / eval(temp2)

    if number[0] != "+" and number[0] != "-":
        output.append("-")
        for m in range(start, end):
            output.append(eq[m])
        for p in range(len(number)):
            eq.pop(start)
        if eq[0] == "*":
            eq.pop(0)
    elif number[0] == '-':
        output.append("+")
        for m in range(start + 1, end):
            output.append(eq[m])
        for p in range(len(number)):
            eq.pop(start)
        if eq[0] == "*":
            eq.pop(0)
    elif number[0] == '+':
        output.append("-")
        for m in range(start, end):
            output.append(eq[m])
        for p in range(len(number)):
            eq.pop(start)
        if eq[0] == "*":
            eq.pop(0)
    for d in eq:
        if d.isdigit() or d == "+" or d == "-" or d == ".":
            temp2.append(d)
    if temp2[len(temp2) - 1] == "+" or temp2[len(temp2) - 1] == "-":
        temp2.pop()

    output = eval("".join(output))
    temp2 = eval("".join(temp2))
    return output / temp2


print(equation_solver("78.5*y+33=10.5"))