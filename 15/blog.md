## Introduction
This is a solution to the 15th puzzle of the advent of code 2020.

The code is available at [github](https://github.com/MatiasStorm/AdventOfCode_2020)

## Solution
Today's puzzle was one of the easier ones:
```python
def play_game(numbers, iterations=2020):
    spoken = {n : [i + 1, i + 1] for i,n in enumerate(numbers)}
    last_spoken = numbers[-1]
    for i in range(len(numbers), iterations):
        if last_spoken in spoken:
            spoken[last_spoken][0] = spoken[last_spoken][1]
            spoken[last_spoken][1] = i
            last_spoken = spoken[last_spoken][1] - spoken[last_spoken][0]
        else:
            spoken[last_spoken] = [i, i]
            last_spoken = 0
    return last_spoken

if __name__ == "__main__":
    print("Part 1: ", play_game([ 6,13,1,15,2,0 ]))
    print("Part 2: ", play_game([ 6,13,1,15,2,0 ], iterations=30000000))
```
In `play_game` we keep track of the numbers that have been said, and when they have been said
in the `spoken` dicitonary.

Then we loop for the specified number of iterations, applying the rules, and return the last 
spoken number in that game.

Thanks for reading!
