def read_input(file_name):
    with open(file_name, "r") as f:
        return [int(l.strip()) for l in f.readlines()]


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





if __name__ == '__main__':
    input = read_input("input.txt")
    num = get_first_wrong_number(input, 25)
    print("Part one: ", num)

    contigous_range = find_contiguous_range(input, num)
    print("Part two: ", contigous_range[0] + contigous_range[-1])


