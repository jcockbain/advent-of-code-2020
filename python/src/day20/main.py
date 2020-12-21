from src.common.file_utils import get_path, read_raw
import itertools
from functools import reduce


class Tile():
    def __init__(self, id, vals, pic_width):
        self.id = id
        self.vals = vals
        self.versions = []
        self.version_index = 0

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


def flip_array(matrix):
    out = [[0 for j in range(0, len(matrix))] for i in range(0, len(matrix))]
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix)):
            new_row = row
            new_col = len(matrix)-1-col
            out[new_row][new_col] = matrix[row][col]
    return out


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


def check_all_tiles(tiles):
    length = len(tiles)
    width = int(length ** 0.5)

    tiles_set = set(tiles)
    placed_tiles = []
    found_solution = None

    def get_matching_idxs(idx):
        if idx == 0:
            return []
        if idx % width == 0:
            return [(idx - width, 1)]
        if idx // width == 0:
            return [(idx - 1, 0)]
        return [(idx - 1, 0), (idx - width, 1)]

    def get_sum_corners():
        tls = found_solution[:]
        print([t.id for t in tls])
        return multiply([t.id for t in [tls[0], tls[width - 1], tls[length - width], tls[-1]]])

    def backtrack():
        nonlocal found_solution

        if len(placed_tiles) == length:
            found_solution = placed_tiles[:]
            return

        matching_idxs = get_matching_idxs(len(placed_tiles))

        for tile in tiles_set:
            for i, t in enumerate(tile.versions):
                tile.version_index = i
                correct_perm = True
                for tile_idx, axis in matching_idxs:
                    paired_tile = placed_tiles[tile_idx]
                    if not matches_tile_behind(tile.versions[i], paired_tile.versions[paired_tile.version_index], axis):
                        correct_perm = False

                if correct_perm:
                    placed_tiles.append(tile)
                    tiles_set.remove(tile)
                    backtrack()
                    tile.version_index = 0
                    placed_tiles.pop()
                    tiles_set.add(tile)

    backtrack()

    return get_sum_corners() if found_solution else None


def part_one(filename: str) -> int:
    tiles = parse_input(filename)
    return check_all_tiles(tiles)


def parse_input(filename: str) -> dict:
    inp = read_raw(get_path(__file__, filename))
    splitted = inp.split("\n\n")
    tiles = []
    for tile in splitted:
        lines = tile.split("\n")
        id = int(lines[0].split(" ")[1].rstrip(":"))
        tile = Tile(id, [[x for x in l]
                         for l in lines[1:]], int(len(tiles) ** 0.5))
        tile.calc_versions()
        tiles.append(tile)
    return tiles


def part_two(filename: str) -> int:
    return None


def print_rows(tiles, width):
    if len(tiles) == 0:
        return

    print("<------------->")

    tile_strings = []
    for t in tiles:
        tile_string = []
        for row in t.vals:
            tile_string.append("".join(row))
        tile_strings.append(tile_string)

    for row in range((len(tiles) // width) + 1):
        for tile_row_idx in range(len(tiles[0].vals)):
            row_s = ""
            for tile in range(width):
                if (row * width) + tile < len(tiles):
                    row_s += tile_strings[(row * width) +
                                          tile][tile_row_idx] + " "
            if row_s != "":
                print(row_s)
        print("\n")


def path(filename: str):
    return get_path(__file__, filename)


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
