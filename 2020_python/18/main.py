import math

def read_input(file_name):
    with open(file_name, "r") as f:
        return [l.strip().replace(" ", "") for l in f.readlines()]

def evaluate(expression, i=0):
    result = None
    op = None
    while i < len(expression):
        c = expression[i]
        if c in "+*":
            op = c
        elif c == "(":
            num, i = evaluate(expression, i+1)
            if result == None:
                result = num
            else:
                result = result * num if op == "*" else result + num
        elif c == ")":
            return result, i
        else:
            if result == None:
                result = int(c)
            else:
                num = int(c)
                result = result * num if op == "*" else result + num
        i += 1
    return result

def evaluate2(expression, i=0):
    result = None
    op = None
    numbers = []
    while i < len(expression):
        c = expression[i]
        if c == "+":
            op = c
        elif c == "*":
            numbers.append(result)
            result = None
            op = None
        elif c == "(":
            num, i = evaluate2(expression, i+1)
            if result == None:
                result = num
            if op == "+":
                result += num
            elif op == "*":
                numbers.append(num)
                numbers.append(result)
                result = None
                op = None
        elif c == ")":
            return math.prod(numbers) * result, i
        else:
            if result == None:
                result = int(c)
            else:
                num = int(c)
                result += num
        i += 1
    return math.prod(numbers) * result

if __name__ == "__main__":
    expressions = read_input("input.txt")

    print("Part 1:", sum([evaluate(e) for e in expressions]))
    print("Part 2:", sum([evaluate2(e) for e in expressions]))

