class Bag():
    def __init__(self, parent, child, amount):
        self.parent = parent
        self.child = child
        self.amount = amount

def read_input():
    input = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            input += parse_line_to_bags(l)
    return input

def parse_line_to_bags(line):
    arr = line.split(" ")
    bags = []
    parent = " ".join(arr[0:2])
    if arr[4] != "no":
        for i in range(5, len(arr), 4):
            child = " ".join(arr[i: i+2])
            amount = int(arr[i - 1])
            bags.append(Bag(parent, child, amount ))
    return bags

def get_parent_bags(input, search_bag):
    parents = []
    for bag in input:
        if bag.child == search_bag:
            parent = bag.parent
            parents.append(parent)
            parents += get_parent_bags(input, parent)
    return set(parents)

def get_number_of_bags_within(input, search_bag):
    result = 0
    for bag in input:
        if bag.parent == search_bag:
            result += bag.amount + bag.amount * get_number_of_bags_within(input, bag.child)
    return result

if __name__ == "__main__":
    input = read_input()
    print("Part one, number of surrounding bags: ", len(get_parent_bags(input, "shiny gold")))
    print("Part two, number of bags within: ", get_number_of_bags_within(input, "shiny gold"))
