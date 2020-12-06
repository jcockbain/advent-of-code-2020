from src.common.file_utils import get_path, read_lines, read_raw


def part_one(filename: str) -> int:
    lines = read_raw(get_path(__file__, filename)).split("\n\n")
    total = 0
    for line in lines:
        line = line.replace("\n", "")
        total += len(list(set(line)))
    return total


def part_two(filename: str) -> int:
    lines = read_raw(get_path(__file__, filename)).split("\n\n")
    total = 0
    for line in lines:
        line = line.split("\n")
        seen = list(set([x for x in line[0]]))
        for p in line[1:]:
            seen = list(set(p) & set(seen))
        total += len(seen)
    return total


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
