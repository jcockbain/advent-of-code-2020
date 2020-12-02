from src.common.file_utils import get_path, read_lines
import re


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    return sum([int(min_c) <= p.count(l) <= int(max_c) for w in lines for min_c, max_c, l, p in (re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', w).groups(),)])


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    return sum([(p[int(pos1) - 1] == l) ^ (p[int(pos2) - 1] == l) for w in lines for pos1, pos2, l, p in (re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', w).groups(),)])


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
