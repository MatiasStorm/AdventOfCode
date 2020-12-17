def get_active(start):
    return [(0,y,x) for y in range(len(start)) for x in range(len(start[0])) if start[y][x] == "#"]

def get_active4d(start):
    return [(0,y,x,0) for y in range(len(start)) for x in range(len(start[0])) if start[y][x] == "#"]

def get_neighbours(z, y, x):
    neighbours  = []
    for zs in range(z - 1, z + 2):
        for ys in range(y - 1, y + 2):
            for xs in range(x - 1, x + 2):
                if not ( xs == x and ys == y and zs == z ):
                    neighbours.append(( zs, ys, xs ))
    return neighbours

def get_neighbours4d(z, y, x, w):
    neighbours  = []
    for zs in range(z - 1, z + 2):
        for ys in range(y - 1, y + 2):
            for xs in range(x - 1, x + 2):
                for ws in range(w-1, w+2):
                    if not ( xs == x and ys == y and zs == z and ws == w ):
                        neighbours.append(( zs, ys, xs, ws ))
    return neighbours

def get_ranges(active):
    zs = [a[0] for a in active]
    ys = [a[1] for a in active]
    xs = [a[2] for a in active]
    return (range(min(zs) - 1, max(zs) + 2), range(min(ys) - 1, max(ys) + 2), range(min(xs) - 1, max(xs) + 2))

def get_ranges4d(active):
    zs = [a[0] for a in active]
    ys = [a[1] for a in active]
    xs = [a[2] for a in active]
    ws = [a[3] for a in active]
    return (range(min(zs) - 1, max(zs) + 2)
            , range(min(ys) - 1, max(ys) + 2)
            , range(min(xs) - 1, max(xs) + 2)
            , range(min(ws) - 1, max(ws) + 2)
            )

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        start = [l.strip() for l in f.readlines()]
    active = get_active(start)

    for _ in range(6):
        ranges = get_ranges(active)
        new_active = active.copy()
        for z in ranges[0]:
            for y in ranges[1]:
                for x in ranges[2]:
                    cube = (z,y,x)
                    count = len([i for i in get_neighbours(z, y, x) if i in active])
                    if count not in (2,3) and cube in active:
                        new_active.remove(cube)
                    elif count == 3 and cube not in active:
                        new_active.append(cube)
        active = new_active
    print(len(active))
                         
    active = get_active4d(start)
    for _ in range(6):
        print(len(active))
        ranges = get_ranges4d(active)
        new_active = active.copy()
        for z in ranges[0]:
            for y in ranges[1]:
                for x in ranges[2]:
                    for w in ranges[3]:
                        cube = (z,y,x, w)
                        count = len([i for i in get_neighbours4d(z, y, x, w) if i in active])
                        if count not in (2,3) and cube in active:
                            new_active.remove(cube)
                        elif count == 3 and cube not in active:
                            new_active.append(cube)
        active = new_active
    print(len(active))

    
