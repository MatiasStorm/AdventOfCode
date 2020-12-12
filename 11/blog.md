## Introduction
This is my solution to the advent of code puzzle on december 11th 2020.

Code is available at [github](https://github.com/MatiasStorm/AdventOfCode_2020)

## Solution
First we create a simple method to read the input data:
```python
def read_input(file_name):
    with open(file_name, "r") as f:
        return [[i for i in l.strip()] for l in f.readlines()]
```

Next we define a method for creating a dictionary of all the seats:
```pyhton
def get_seats(plan, adj_alg):
    seats = {}
    for r in range(len(plan)):
        for c in range(len(plan[0])):
            if plan[r][c] == "L":
                seats[(r, c)] = ["L"]
    return adj_alg(seats)
```
`plan` is the input data returned from `read_input`

`adj_alg` is the algorithm use to determine the position of the adjacent seats.

The method returns a dictionary containing the row and column position of the seat
as the key, and an array, where the first index is the status (`'L' || '#'`) and the second
index is an array of adjacent seats, as the value.

Now we can define the first adjacent seat finding algrithm:
```python
def adjacent(seats):
    for seat in seats:
        row, col = seat
        adj_seats = []
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (r, c) in seats and (r, c) != seat:
                    adj_seats.append((r, c))
        seats[seat].append(adj_seats)
    return seats
```
This just add the immediately adjacent seats to the adjacent seat array of each seat.

Finnally we need to define a method for running the seat simulation:
```python
def do_sim(seats, n_occ):
    changes = {-1:-1}
    while len(changes) > 0:
        changes = {}
        for seat in seats:
            occ = 0
            for sur_seat in seats[seat][1]:
                if seats[sur_seat][0] == "#":
                    occ += 1
            if occ == 0 and seats[seat][0] == "L":
                changes[seat] = "#"
            if occ >= n_occ and seats[seat][0] == "#":
                changes[seat] = "L"
        for c in changes:
            seats[c][0] = changes[c]
    return len([i for i in seats if seats[i][0] == "#"])
```
`seats` are the dictionary of seats, with status and adjacent seats.

`n_occ` is the minimum number of occupied adajcent seats a seat can have before it becomes empty.

That was part 1, which can be tested with:
```python
plan = read_input("input.txt")
seats = get_seats(plan, adjacent)
print("Part 1: ", do_sim(seats, 4))
```

For part 2 we just need to define a new algorithm for finding adjacent seats:
```python
def check_direction(seats, start_row, inc_row, start_col, inc_col):
    r = start_row
    c = start_col
    while 0 <= r < len(plan) and 0 <= c < len(plan[0]):
        if (r, c) in seats:
            return (r,c)
        r += inc_row
        c += inc_col
    return None

def visible(seats):
    for seat in seats:
        adj_seats = []
        row, col = seat
        for i in range(-1 , 2):
            for j in range(-1, 2):
                if 0 == j == i:
                    continue
                s = check_direction(seats, row + i, i, col + j, j)
                if s:
                    adj_seats.append(s)
        seats[seat].append(adj_seats)
    return seats
```
`check_direction` returns the position of the first seat in the given directon

`visible` adds the adajcent seats to the seat dictionary, using `check_direction`.

Part 2 can be tested with:
```python
plan = read_input("input.txt")
seats = get_seats(plan, visible)
print("Part 2: ", do_sim(seats, 5))
```

That was it, thanks for reading!
