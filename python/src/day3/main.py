from src.common.file_utils import get_path, read_lines
from functools import reduce


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    return get_trees(1, 3, lines)


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    trees = [
        get_trees(1, 1, lines),
        get_trees(1, 3, lines),
        get_trees(1, 5, lines),
        get_trees(1, 7, lines),
        get_trees(2, 1, lines)
    ]
    return reduce((lambda x, y: x * y), trees)


def get_trees(dy, dx, lines):
    h, w = len(lines), len(lines[0])
    return sum([lines[i * dy][(i * dx) % w] == "#" for i in range(0, h // dy)])


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
