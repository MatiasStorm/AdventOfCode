## Introduction
This is a solution to the 17th puzzle of the advent of code 2020.

The code is available at [github](https://github.com/MatiasStorm/AdventOfCode_2020)

## Solution
First of we define a method for reading the input file:
```python
def read_input(file_name):
    with open(file_name, "r") as f:
        return [l.strip().replace(" ", "") for l in f.readlines()]
        
expressions = read_input("input.txt")
```

### Part 1
```python
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
    
    
print("Part 1:", sum([evaluate(e) for e in expressions]))
```


### Part 2
```python
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
    
print("Part 2:", sum([evaluate2(e) for e in expressions]))
```

The only difference between part 1 and 2 is that in part 2 we do all the + operations
and if the encounter a * operation the current result is added to an array.  
In the end we take the product of that array


Thanks for reading!
