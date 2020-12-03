def get_input():
    input = []
    with open('input.txt', 'r') as f:
        input = [l.strip() for l in f.readlines()]
    return input

def count_trees(down, left, tree_char, field):
    width = len(field[0])
    trees = 0
    r = 0
    c = 0
    while r < len(field):
        if field[r][c] == tree_char:
            trees += 1
        r += down
        c = ( c + left ) % width
    return trees

if __name__ == "__main__":
    input = get_input()
    print("Number of trees - 1 down, 3 left: ", count_trees(1, 3, "#", input))
    r1_d1 = count_trees(1, 1, "#", input)
    r3_d1 = count_trees(1, 3, "#", input)
    r5_d1 = count_trees(1, 5, "#", input)
    r7_d1 = count_trees(1, 7, "#", input)
    r1_d2 = count_trees(2, 1, "#", input)
    print("All slopes: ", r1_d1, r3_d1, r5_d1, r7_d1, r1_d2)
    print("Product: ", r1_d1 * r3_d1 * r5_d1 * r7_d1 * r1_d2)

