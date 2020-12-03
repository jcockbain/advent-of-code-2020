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


def get_trees(down, right, lines):
    x, y, trees, width = 0, 0, 0, len(lines[0])
    while y < len(lines):
        trees += lines[y][x % width] == "#"
        x += right
        y += down
    return trees


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
