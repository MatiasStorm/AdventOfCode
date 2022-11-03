## Introduction
This is a solution to the 13th puzzle of the advent of code 2020.

The code is available at [github](https://github.com/MatiasStorm/AdventOfCode_2020)

## Solution

### Part 1
Part 1 was pretty straight forward. 
We just divide the bus id with the arrival time,
round it up and multiply it with the same bus id to get the ealist time we could take that bus.

```python
def get_earliest_bus(file_name):
    with open(file_name, "r") as f:
        arrival = int(f.readline().strip())
        busses = [int(i) for i in f.readline().strip().split(",") if i != "x"]

    earliest = arrival + max(busses)
    bus_id = 0
    for b in busses:
        timestamp = math.ceil(arrival / b) * b
        if timestamp < earliest:
            earliest = timestamp
            bus_id = b
    return ( earliest - arrival ) * bus_id
    
print("Part 1:", get_earliest_bus("input.txt"))
```

### Part 2
Part 2 was a bit more tricky, i tried to explain it as well as i could in the comments:
```python
def earliest_timestamp(file_name):
    busses = {}
    with open(file_name, "r") as f:
        f.readline()
        bs = [int(i) if i != "x" else -1 for i in f.readline().strip().split(",") ]
        for i, b in enumerate(bs):
            if b != -1:
                busses[b] = i # Dict with {bus_id : offset}

    time_stamp = list(busses)[0]
    cm = time_stamp # common multiple, starts at the first bus's timestamp.
    for b in list( busses )[1:]: # Loop through all the busses except the first one (We have found its lcm)
        while (time_stamp + busses[b]) % b != 0: # find the LCM of time_stamp + offset and the current bus id.
            time_stamp += cm
        cm *= b # Get the new common multiple of all previous numbers
    return time_stamp

print("Part 2:", earliest_timestamp("input.txt"))
```

Thanks for reading!
