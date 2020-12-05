def get_seat_row_col(seat):
    r = 128
    c = 8
    for i in range(len(seat)):
        if i < 7: # Getting row
            if seat[i] == "F":
                r -= int (128 / (2 ** (i + 1)))

        else: # Getting col
            if seat[i] == "L":
                c -= int( 8 / (2 ** (i - 6)) )
    return (r - 1, c - 1)



def read_seat_plan():
    plan = [[0 for j in range(8)] for i in range(128)]
    with open("input.txt", "r") as f:
        for line in f.readlines():
            r, c = get_seat_row_col(line.strip())
            plan[r][c] = 1
    return plan

def get_highest_seat_id(plan):
    for r in range(len(plan) - 1, -1, -1):
        if sum(plan[r]) > 0:
            for c in range(len(plan[r]) - 1, -1, -1):
                if plan[r][c] == 1:
                    return r * 8 + c

def get_your_seat_id(plan):
    for r in range(len(plan)):
        if 0 < sum(plan[r]) < 8:
            for c in range(len(plan[r])):
                if plan[r][c] == 0:
                    return r * 8 + c

if __name__ == "__main__":
    plan = read_seat_plan()
    print(get_highest_seat_id(plan))
    print(get_your_seat_id(plan))
