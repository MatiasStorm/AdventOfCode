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


if __name__ == "__main__":
    program = read_input("input.txt")
    print("Part 1:", find_mem_sum(program))
    print("Part 2:", find_mem_sum2(program))
