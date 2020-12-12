## Introduction

My solution to the 9th advent of code puzzle.

The code i available on [github](https://github.com/MatiasStorm/AdventOfCode_2020)

## The puzzle

Today we need to break the XMAS encryption, to figure out how it works
read the whole puzzle at [Advent of Code](https://adventofcode.com/2020/day/9)

**Part 1:** Find the first number that doesn't follow the XMAS encryption scheme.

**Part 2:** Find a contigous set of numbers which sum to the previously found number.

## Solution

### Part 1

First we read in the input file:
``` python
def read_input(file_name):
    with open(file_name, "r") as f:
        return [int(l.strip()) for l in f.readlines()]
```

Then we define the following two methods:
```python
def is_number_correct(input, s):
    while len(input) >= 2:
        if input[0] + input[-1] > s:
            input = input[0:-1]
        elif input[0] + input[-1] < s:
            input = input[1:len(input)]
        else:
            return True
    return False

def get_first_wrong_number(input, pream_len):
    for i in range(len(input) - pream_len):
        if not is_number_correct(sorted(input[i: i + pream_len ]), input[i + pream_len]):
            return input[i + pream_len]
```
`is_number_correct` checks if two numbers sum to to the `s`-value.

`get_first_wrong_number` finds the first number in `input`
where no two numbers in the previous `pream_len` numbers sum to it.

That was part one now we can test the solution:
```python
input = read_input("input.txt")
num = get_first_wrong_number(input, 25)
print("Part one: ", num)
```

### Part 2

For part two we define a single new method:
```python
def find_contiguous_range(input, num):
    start_index = 0
    end_index = 1
    contiguous_range = input[0:2]
    contiguous_sum = sum(contiguous_range)
    while contiguous_sum != num:
        if contiguous_sum < num:
            end_index += 1
            contiguous_range.append(input[end_index])
        elif contiguous_sum > num:
            start_index += 1
            end_index = start_index + 1
            contiguous_range = input[start_index: end_index + 1]
        contiguous_sum = sum(contiguous_range)
    return contiguous_range
```
This method starts at the top of the list, increases the contiguous range, 
until its sum is either larger than or equal to `num`.

If the sum gets larger than `num` `start_index` is incremented and the search is
restarted from that index and up.

If it equals `num` the range is returned.

Now we can test the code:
```python
contigous_range = find_contiguous_range(input, num)
print("Part two: ", contigous_range[0] + contigous_range[-1])
```

Thanks for reading!

