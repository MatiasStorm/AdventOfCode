## Introduction
This is a solution to the 17th puzzle of the advent of code 2020.

The code is available at [github](https://github.com/MatiasStorm/AdventOfCode_2020)

## Solution

### Part 1
I have propably implemented the simplest solution, which also means its not very fast.
```python
def get_active(start):
    return [(0, y, x, 0) for y in range(len(start)) for x in range(len(start[0])) if start[y][x] == "#"]

def get_inactive(active, part2=False):
    inactive = []
    for cube in active:
        inactive += get_neighbours(cube, part2)
    return set(inactive)

def get_neighbours(cube, part2):
    neighbours  = []
    z, y, x, w = cube
    for zs in range(z - 1, z + 2):
        for ys in range(y - 1, y + 2):
            for xs in range(x - 1, x + 2):
                if part2:
                    for ws in range(w-1, w+2):
                        if not ( xs == x and ys == y and zs == z and ws == w ):
                            neighbours.append(( zs, ys, xs, ws ))
                elif not ( xs == x and ys == y and zs == z ):
                    neighbours.append(( zs, ys, xs, 0 ))
    return neighbours

def get_number_of_active(start, part2=False):
    active = get_active(start)
    for _ in range(6):
        new_active = active.copy()
        inactive = get_inactive(active, part2)
        for cube in active:
            count = len([i for i in get_neighbours(cube, part2) if i in active])
            if count not in (2,3) and cube in active:
                new_active.remove(cube)
        for cube in inactive:
            count = len([i for i in get_neighbours(cube, part2) if i in active])
            if count == 3 and cube not in active:
                new_active.append(cube)
        active = new_active
    return len(active)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        start = [l.strip() for l in f.readlines()]

    print("Part 1", get_number_of_active(start))
    print("Part 2", get_number_of_active(start, True))
```
The idea is to first look at all the active cubes and determine if they should stay active or
change state to inactive.

Afterwards all the active cubes neighbours are checked to see if they should be activated.

That was it for today, thanks for reading!
