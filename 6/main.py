def get_input():
    input = []
    group = ""
    with open("input.txt", "r") as f:
        for l in f.readlines():
            if l == "\n":
                input.append([set(i) for i in group.split(":")])
                group = ""
            else:
                group += l.strip() if group == "" else ":" + l.strip()
    return input

def union(list_of_sets):
    union = set(list_of_sets[0])
    for i in list_of_sets[1:]:
        union |= i
    return union

def intersection(list_of_sets):
    intersection = set(list_of_sets[0])
    for i in list_of_sets[1:]:
        intersection &= i
    return intersection

if __name__ == '__main__':
    input = get_input()
    print("Sum of all groups, Part 1: ", sum([ len(union(g)) for g in input ]))
    print("Sum of all groups, Part 2: ", sum([ len(intersection(g)) for g in input ]))

