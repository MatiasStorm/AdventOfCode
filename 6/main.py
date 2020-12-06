def sum_all_groups_part_1():
    group = ""
    result = 0
    with open("input.txt", "r") as f:
        for l in f.readlines():
            if l == "\n":
                result +=len(set([i for i in group]))
                group = ""
            else:
                group += l.strip()
    return result


def intersection(list_of_sets):
    intersection = set(list_of_sets[0])
    for i in list_of_sets[1:]:
        intersection &= i
    return intersection


def sum_all_groups_part_2():
    group_str = ""
    result = 0
    with open("input.txt", "r") as f:
        for l in f.readlines():
            if l == "\n":
                group = [set(i) for i in group_str.split(":")]
                result += len(intersection(group))
                group_str = ""
            else:
                group_str += l.strip() if group_str == "" else ":" + l.strip()
    return result


if __name__ == '__main__':
    print("Sum of all groups, Part 1: ", sum_all_groups_part_1())
    print("Sum of all groups, Part 2: ", sum_all_groups_part_2())

