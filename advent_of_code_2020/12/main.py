def read_input(file_name):
    with open(file_name, "r") as f:
        return [(l[0], int(l[1:])) for l in f.readlines()]


def get_dist_part1(directions):
    degree = 90
    dist = 0
    for d in directions:
        direction = d[0]
        amount = -d[1] if d[0] in ["N", "W", "L"] else d[1]
        if direction in ["N", "S", "E", "W"]:
            dist += amount
        elif direction in [ "L", "R" ]:
            degree = ( degree + amount ) % 360
        elif direction == "F":
            if degree == 90 or degree == 180:
                dist += amount
            else:
                dist -= amount
    return dist

def get_dist_part2(directions):
    ship = {"E": 0, "S": 0}
    way_point = {"E": 10, "S": -1}
    for d in directions:
        direction = d[0]
        amount = -d[1] if d[0] in ["N", "W", "L"] else d[1]

        if direction == "N" or direction == "S":
            way_point["S"] += amount

        elif direction == "W" or direction == "E":
            way_point["E"] += amount

        elif direction == "L" or direction == "R":
            a = way_point["E"]
            b = way_point["S"]
            x = ship["E"]
            y = ship["S"]
            if amount == 90 or amount == -270:
                way_point["E"] = -(b-y) + x 
                way_point["S"] = (a-x) + y
            elif amount == -90 or amount == 270:
                way_point["E"] = b - y + x
                way_point["S"] = -(a - x) + y
            else:
                way_point["E"] = -(a-x) + x
                way_point["S"] = -(b - y) + y
        elif direction == "F":
            for k in ship:
                dist = amount * ( way_point[k] - ship[k] )
                ship[k] += dist
                way_point[k] += dist
    return ship["E"] + ship["S"]
        



if __name__ == "__main__":
    directions = read_input("input.txt")
    print(get_dist_part1(directions))
    print(get_dist_part2(directions))
