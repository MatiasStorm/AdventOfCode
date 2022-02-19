class Tile:
    def __init__(self, tile, id):
        self.tile = tile
        self.id = id
        self.up = tile[0]
        self.right = "".join([i[-1] for i in tile])
        self.down = tile[-1]
        self.left = "".join([i[0] for i in tile])

    def match(self, tile):
        for d in [self.up, self.right, self.down, self.left]:
            rev_d = d[::-1]
            if d == tile.up or d == tile.down or d == tile.left or d == tile.right:
                return True
            elif rev_d == tile.up or rev_d == tile.down or rev_d == tile.left or rev_d == tile.right:
                return True
        return False

    def __repr__(self):
        return self.id
        # return "\n".join(self.tile)

def read_input(file_name):
    tiles = {}
    with open(file_name, "r") as f:
        tile = []
        id = None
        for l in f.readlines():
            l = l.strip()
            if id == None:
                id = l.split(" ")[1][0:-1]
                tile = []
            elif l == "":
                tiles[id] = Tile(tile, id)
                id = None
            else:
                tile.append(l)
    return tiles

def get_corners(tiles):
    s = 1
    for t1 in tiles:
        tile1 = tiles[t1]
        count = 0
        for t2 in tiles:
            tile2 = tiles[t2]
            if t1 == t2:
                continue
            elif tile1.match(tile2):
                count += 1
        print(count)
        if count == 2:
            s *= int(t1)
    return s


if __name__ == "__main__":
    tiles = read_input("input.txt")
    print(get_corners(tiles))





