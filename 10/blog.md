## Introduction
This is my solution to the advent of code puzzle december 10th 2020.

Code is available at [github](https://github.com/MatiasStorm/AdventOfCode_2020)

## Solution
```python
def read_input(file_name):
    with open(file_name, 'r') as f:
        return [int(l.strip()) for l in f.readlines()]


def get_jolts_differences(input):
    differences = {1: 0, 2: 0, 3:1} # 3 starts at 1 to account for the device's built in adapter.
    for i in range(len(input) - 1):
        difference = input[i+1] - input[i]
        differences[difference] += 1
    return differences

def get_number_of_arrangements(input):
    arrangements = {0: 1}
    total_arrangements = 1
    block_len = 0 # The length of the current block of concurrent numbers i.e: 5, 6, 7 --> 3
    for num in input:
        if block_len not in arrangements: # Add the number of permutations for a block of concurrent numbers with length 'block_len'
            arrangements[block_len] = 0
            for i in range(1,4): # Calculate the number of permutations for the new block length.
                if block_len - i in arrangements:
                    arrangements[block_len] += arrangements[block_len - i]
        if num + 1 in input:
            block_len += 1
        else:
            total_arrangements *= arrangements[block_len]
            block_len = 0
    return total_arrangements


if __name__ == '__main__':
    input = sorted(read_input("input.txt") + [0]) # Add 0 to account for the outlet
    differences = get_jolts_differences(input)
    print("Part 1: ", differences[1] * differences[3])
    print("Part 2: ", get_number_of_arrangements(input))
```
Part 1 was pretty easy, 
we just loop through the array of adapters and count the differences between each of them.

Part 2 was a bit more tricky. An important thing to realize is that 
the number of permutations in a group of contiguous adapters with length `n`,
is equal to the sum of permutations in the previous three, that is `n-1`, `n-2` and `n-3`.

**Example:**
- `0`, You have no adapters, permutations = 1
- `0, 1`, You only have one adapter, permutations = 1
- `0, 1, 2`, You have two adapters, permutations = 1 + 1 = 2
- `0, 1, 2, 3`, You have three adapters, permutations = 2 + 1 + 1 = 4
- `0, 1, 2, 3, 4`, You have four adapters, permutations = 4 + 2 + 1 = 7.

So for part 2, we just keep track of the number of permutations for each group of a given size.

Look through the adapters to find groups of adapters with contiguous jolts,
find the number permutations,
and multiply it with the running total.


Thanks for reading!

