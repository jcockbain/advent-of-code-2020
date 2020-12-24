from src.common.file_utils import get_path, read_lines
from collections import defaultdict


dirs = {
    "e": (1, 1, 0),
    "w": (-1, -1, 0),
    "ne": (0, 1, 1),
    "nw": (-1, 0, 1),
    "se": (1, 0, -1),
    "sw": (0, -1, -1),
}


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    black = get_tiles(lines)
    return len(black)


def get_tiles(lines):
    black = set()
    for line in lines:
        pos = process_line(line)
        if pos in black:
            black.remove(pos)
        else:
            black.add(pos)
    return black


def process_line(line):
    pos = (0, 0, 0)
    idx = 0

    while idx < len(line):
        if line[idx] == "s" or line[idx] == "n":
            d = line[idx] + line[idx + 1]
            idx += 2
        else:
            d = line[idx]
            idx += 1
        travel = dirs[d]
        pos = pos[0] + travel[0], pos[1] + travel[1], pos[2] + travel[2]

    return pos


def game_of_life(black, turns):

    for _ in range(turns):

        neighbour_counter = defaultdict(int)

        for pos in black:
            for travel in dirs.values():
                newpos = pos[0] + travel[0], pos[1] + \
                    travel[1], pos[2] + travel[2]
                neighbour_counter[newpos] += 1

        new_black = set()

        for pos, nbours in neighbour_counter.items():
            if pos in black:
                if not (nbours == 0 or nbours > 2):
                    new_black.add(pos)
            elif pos not in black and nbours == 2:
                new_black.add(pos)

        black = new_black

    return new_black


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    black = get_tiles(lines)
    black = game_of_life(black, 100)
    return len(black)


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
