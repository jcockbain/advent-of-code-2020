from src.common.file_utils import get_path, read_raw
import itertools
from functools import reduce

sea_monster = [
    (0, 18),
    (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
    (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)
]


class Tile():
    def __init__(self, id, vals):
        self.id = id
        self.vals = vals
        self.versions = []
        self.version_index = None

    def calc_versions(self):
        self.versions = []
        self.versions.append(rotate_array(self.vals))
        self.versions.append(rotate_array(self.versions[-1]))
        self.versions.append(rotate_array(self.versions[-1]))
        self.versions.append(rotate_array(self.versions[-1]))

        self.versions.append(flip_array(self.vals))
        self.versions.append(rotate_array(self.versions[-1]))
        self.versions.append(rotate_array(self.versions[-1]))
        self.versions.append(rotate_array(self.versions[-1]))


def rotate_array(m):
    n = len(m)
    res = [[0] * n] * n
    for y in range(n):
        for x in range(n):
            res[y][x] = m[x][y]
        res[y] = res[y][::-1]
    return res


def flip_array(m):
    out = [[0 for j in range(0, len(m))] for i in range(0, len(m))]
    for row in range(0, len(m)):
        for col in range(0, len(m)):
            new_row = row
            new_col = len(m)-1-col
            out[new_row][new_col] = m[row][col]
    return out


def check_top(bottom, top):
    bottom_vals = bottom.versions[bottom.version_index]
    top_vals = top.versions[top.version_index]
    return bottom_vals[0] == top_vals[-1]


def check_left(right, left):
    left_vals = left.versions[left.version_index]
    right_vals = right.versions[right.version_index]
    return get_col(0, right_vals) == get_col(len(left_vals) - 1, left_vals)


def matches_tile_behind(tile1, tile2, axis):
    if axis == 1:
        return tile1[0] == tile2[-1]
    return get_col(0, tile1) == get_col(len(tile2) - 1, tile2)


def get_col(x, arr):
    res = [0] * len(arr)
    for i, c in enumerate(arr):
        res[i] = c[x]
    return res


def multiply(l):
    return reduce(lambda x, y: x * y, l)


def backtrack(tiles_set, row, col, side):
    if row >= side or col >= side:
        return True

    for tile in tiles_set:
        placed_tiles[row][col] = tile
        tiles_set.remove(tile)
        for i, t in enumerate(tile.versions):
            tile.version_index = i
            left = True
            top = True
            if col > 0:
                left = check_left(
                    placed_tiles[row][col], placed_tiles[row][col-1])
            if row > 0:
                top = check_top(placed_tiles[row]
                                [col], placed_tiles[row-1][col])

            if left and top:
                c = (col + 1) % side
                r = (side*row + col + 1) // side
                if backtrack(tiles_set, r, c, side):
                    tile.version_index = i
                    return True
                tile.version_index = None
        placed_tiles[row][col] = None
        tiles_set.add(tile)

    return False


def parse_input(filename: str) -> dict:
    inp = read_raw(get_path(__file__, filename))
    splitted = inp.split("\n\n")
    tiles = []
    for tile in splitted:
        lines = tile.split("\n")
        id = int(lines[0].split(" ")[1].rstrip(":"))
        tile = Tile(id, [[x for x in l]
                         for l in lines[1:]])
        tile.calc_versions()
        tiles.append(tile)
    return tiles


def print_rows(tiles, width):
    if len(tiles) == 0:
        return

    print("<------------->")

    tile_strings = []
    for row in tiles:
        for tile in row:
            tile_string = []
            for row in tile.versions[tile.version_index]:
                tile_string.append("".join(row))
            tile_strings.append(tile_string)

    for row in range(len(tiles)):
        for tile_row_idx in range(len(tiles[0][0].vals)):
            row_s = ""
            for tile in range(width):
                if (row * width) + tile < len(tiles):
                    row_s += tile_strings[(row * width) +
                                          tile][tile_row_idx] + " "
            if row_s != "":
                print(row_s)
        print("\n")


def part_one(filename: str) -> int:
    global placed_tiles

    tiles = parse_input(filename)
    tiles_set = set(tiles)
    side = int(len(tiles) ** 0.5)
    placed_tiles = [[None for j in range(side)] for i in range(side)]

    backtrack(tiles_set, 0, 0, side)

    return multiply([t.id for t in [placed_tiles[0][0], placed_tiles[0][-1], placed_tiles[-1][0], placed_tiles[-1][-1]]])


def part_two(input):
    global placed_tiles

    image = remove_boundaries(placed_tiles)
    monsters, rotations = 0, 0
    while not monsters:
        monsters = mark_sea_monsters(image)
        if not monsters:
            if rotations < 4:
                image = rotate_array(image)
                rotations += 1
            else:
                image = flip_array(image)
                rotations = 0
        else:
            return sum([l.count('#') for l in image])

    return -1


def remove_boundaries(tiles):
    tiles_len = len(tiles)
    img_width = tiles_len * (len(placed_tiles[0][0].vals) - 2)
    image = [[None for j in range(0, img_width)] for i in range(0, img_width)]

    for ri, row in enumerate(placed_tiles):
        for ci, tile in enumerate(row):
            t = tile.versions[tile.version_index]
            plen = len(t) - 2
            for pri in range(1, len(t)-1):
                for pci in range(1, len(t)-1):
                    px = t[pri][pci]
                    dest_row = ri * plen + pri - 1
                    dest_col = ci * plen + pci - 1
                    image[dest_row][dest_col] = px

    return image


def mark_sea_monsters(image):
    monsters = 0
    for r in range(0, len(image)):
        for c in range(0, len(image[r])):
            found = True
            for coords in sea_monster:
                offset_r, offset_c = r + coords[0], c + coords[1]
                if offset_r >= len(image) or offset_c >= len(image[r]) or image[offset_r][offset_c] != '#':
                    found = False
                    break
            if found:
                monsters += 1
                for coords in sea_monster:
                    image[r + coords[0]][c + coords[1]] = 'O'
    return monsters


def path(filename: str):
    return get_path(__file__, filename)


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
