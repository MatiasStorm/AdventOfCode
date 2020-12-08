def read_input(file_name):
    with open(file_name, "r") as f:
        return [parse_line(l) for l in f.readlines()]

def parse_line(line):
    line_arr = line.split(" ")
    op = line_arr[0]
    val = int( line_arr[1][1:] )
    if line_arr[1][0] == '-':
        val = -val
    return [ op, val ]

def do_operation(operation, index, acc):
    op, val = operation
    if op == "nop":
        index += 1
    elif op == "acc":
        acc += val
        index += 1
    elif op == "jmp":
        index += val
    return index, acc


def get_acc_val(input):
    index = 0
    visited_indexes = []
    acc = 0
    while index < len(input):
        if index in visited_indexes:
            return acc
        visited_indexes.append(index)
        index, acc = do_operation(input[index], index, acc)
    return acc

def does_loop(input, index, visited_indexes):
    while index < len(input):
        if index in visited_indexes:
            return True
        visited_indexes.append(index)
        index = do_operation(input[index], index, 0)[0]
    return False

def fix_corrupt_opertion(input):
    index = 0
    visited_indexes = []
    while index < len(input):
        if index in visited_indexes:
            return None
        operation = input[index]
        op = operation[0]

        if op == "nop" or op == "jmp":
            operation[0] = "jmp" if op == "nop" else "nop"
            if not does_loop(input, index, visited_indexes.copy()):
                return input
        operation[0] = op

        visited_indexes.append(index)
        index = do_operation(operation, index, 0)[0]
    return None
    

if __name__ == "__main__":
    input = read_input("input.txt")
    print("Acc value, just before the loop: ", get_acc_val(input))
    print("Acc value after fix: ", get_acc_val(fix_corrupt_opertion(input)))
