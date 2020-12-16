## Introduction
This is a solution to the 12th puzzle of the advent of code 2020.

The code is available at [github](https://github.com/MatiasStorm/AdventOfCode_2020)

## Solution

### Part 1

First we read in the input, as a list of tuples containing the operation and value:
```python
def read_input(file_name):
    with open(file_name, "r") as f:
        return [(l[0], int(l[1:])) for l in f.readlines()]
```

Then we can define the method for finding the Manhattan distance travled:
```python
def get_dist_part1(directions):
    degree = 90
    dist = 0
    for d in directions:
        direction = d[0]
        amount = -d[1] if d[0] in ["N", "W", "L"] else d[1]
        if direction in ["N", "S", "E", "W"]:
            dist += amount
        elif direction in [ "L", "R" ]:
            degree = ( degree + amount ) % 360
        elif direction == "F":
            if degree == 90 or degree == 180:
                dist += amount
            else:
                dist -= amount
    return dist
```

Finally we can test the method:
```python
directions = read_input("input.txt")
print(get_dist_part1(directions))
```

### Part 2
Firstly we read in the input the same was as part 1.

Then we just need to create the following method to find the distance with the new rules:
```python
def get_dist_part2(directions):
    ship = {"E": 0, "S": 0}
    way_point = {"E": 10, "S": -1}
    for d in directions:
        direction = d[0]
        amount = -d[1] if d[0] in ["N", "W", "L"] else d[1]

        if direction == "N" or direction == "S":
            way_point["S"] += amount

        elif direction == "W" or direction == "E":
            way_point["E"] += amount

        elif direction == "L" or direction == "R":
            a = way_point["E"]
            b = way_point["S"]
            x = ship["E"]
            y = ship["S"]
            if amount == 90 or amount == -270:
                way_point["E"] = -(b-y) + x 
                way_point["S"] = (a-x) + y
            elif amount == -90 or amount == 270:
                way_point["E"] = b - y + x
                way_point["S"] = -(a - x) + y
            else:
                way_point["E"] = -(a-x) + x
                way_point["S"] = -(b - y) + y
        elif direction == "F":
            for k in ship:
                dist = amount * ( way_point[k] - ship[k] )
                ship[k] += dist
                way_point[k] += dist
    return ship["E"] + ship["S"]
```
With the new rules for part 2 we now primaryly move the way point instead of the ship.

The trickiest part was to figure out how to rotate the way point around the ship.
If you find the formulas difficult to understand, try to derive them yourself on a piece of paper,
or google how to rotate a point around another point.

When that is done it's almost the same as in part 1.

Now part 2 can be tested with:
```python
directions = read_input("input.txt")
print(get_dist_part2(directions))
```


Thanks for reading!
