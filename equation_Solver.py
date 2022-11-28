def equation_solver(equation):
    def is_number(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    k, start, end = 0, 0, 0
    number, temp, temp2, temp4 = [], [], [], []
    equation = list(equation)
    eq = equation[equation.index("=")::-1][::-1]
    output = equation[equation.index("=") + 1::]
    for i in range(len(eq)):
        temp.append(eq[i])  # all values of the loop
        for b in eq:  # remove all spaces
            if b == " ":
                eq.remove(" ")
        if (eq[i + 1] == "+" or eq[i + 1] == "-" or eq[i - 1] == "+" or eq[i - 1] == "-") and (
                eq[i + 1] != "*" and eq[i - 1] != "*") and is_number(eq[i]):  # the number with this conditions
            temp3 = []
            j = i
            if all(item.isdigit() or item == "." for item in temp):  # specific problem
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
        if i == len(eq) - 2:
            if len(eq) == 2:
                return ''.join(output)
            if len(eq) == 3 and eq[0] == "-":
                return eval(f"-{''.join(output)}")
            if eq[0] == "-":
                temp4.append("-")
            for c in eq:
                if is_number(c) or c == ".":
                    temp4.append(c)
            return eval(''.join(output)) / eval("".join(temp4))

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

    if len(eq) == 3:
        return eval(''.join(output))
    if len(eq) == 4 and eq[0] == "-":
        return eval(f"-{''.join(output)}")
    if len(eq) == 2:
        return eval(''.join(output))
    for d in eq:
        if d.isdigit() or d == "+" or d == "-" or d == "." and eq[eq.index(d) + 1] != "=":
            temp2.append(d)

    if len(temp2) == 2:
        temp2.append(1)

    if temp2[len(temp2) - 1] == "+" or temp2[len(temp2) - 1] == "-":
        temp2.pop()

    output = eval("".join(output))
    temp2 = eval("".join(temp2))
    return output / temp2


print(equation_solver("x-9.0=3.0"))
