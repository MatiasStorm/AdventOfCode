## Introduction
This is a solution to the 14th puzzle of the advent of code 2020.

The code is available at [github](https://github.com/MatiasStorm/AdventOfCode_2020)

## Solution

To start off we define two helper methods for converting between binary and decimal, and back:
```python
def convert_to_binary(number):
    binary = ""
    for i in range(35, -1, -1):
        if number - 2**i >= 0:
            binary += "1"
            number -= 2**i
        else:
            binary += "0"
    return binary

def convert_to_decimal(binary):
    number = 0
    for i, b in enumerate(reversed(list(binary))):
        if b == "1":
            number += 2**i
    return number
```

Then we define a method for reading the input, which will be used in both parts:
```python
def read_input(file_name):
    program = []
    mask = None
    with open(file_name, "r") as f:
        for l in f.readlines():
            l = l.strip()
            if "mask" in l:
                if mask:
                    program.append((mask, mem))
                mask = l.split(" ")[2]
                mem = []
            elif "mem" in l:
                addr = convert_to_binary(int(l.split(" ")[0][4:-1]))
                val = int(l.split(" ")[2])
                mem.append((addr, val))
        mem.append((addr, val))
        program.append((mask, mem))
    return program
```
This returns a list of memory operations and the mask that will be applied to them.

In this format: `[(mask1, [(mem1, val1), (mem2, val2)]), (mask2, ...)]`

### Part 1
To solve part 1, we define the following two methods:
```python
def apply_mask(number, mask):
    binary = list(convert_to_binary(number))
    for i in range(len(mask)):
        if mask[i] != "X":
            binary[i] = mask[i]
    return convert_to_decimal("".join(binary))

def find_mem_sum(program):
    memory = {}
    for p in program:
        mask = p[0]
        for mem in p[1]:
            addr = mem[0]
            val = mem[1]
            memory[addr] = apply_mask(val, mask)
    return sum(memory.values())


print("Part 1:", find_mem_sum(program))
```
`apply_mask` applies the mask to the number which is to be saved in memory.

`find_mem_sum` runs through the program, saves all the values in the memory dictionary
and finally sums the values.

### Part 2
```python
def apply_mask_to_address(address, mask):
    addresses = [address]
    for i in range(len(mask)):
        if mask[i] == "1":
            for j in range(len(addresses)):
                addr = addresses[j]
                addresses[j] = addr[0:i] + "1" + addr[i+1:]
        elif mask[i] == "X":
            for addr in addresses.copy():
                addr = list(addr)
                addr[i] = "1" if addr[i] == "0" else "0"
                addresses.append("".join(addr))
    return addresses

def find_mem_sum2(program):
    memory = {}
    for p in program:
        mask = p[0]
        for mem in p[1]:
            address = mem[0]
            val = mem[1]
            for addr in apply_mask_to_address(address, mask):
                memory[addr] = val
    return sum(memory.values())


print("Part 2:", find_mem_sum2(program))
```
`apply_mask_to_address` finds all the addresses which the number is to be saved in.

`find_mem_sum2` loops through the program, gets the addresses from `apply_mask_to_address`,
saves the values in the `memory` dictionary and finally sums all the values.


Thanks for reading!
