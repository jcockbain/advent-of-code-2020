from src.common.file_utils import get_path, read_lines, read_raw


def part_one(filename: str) -> int:
    lines = read_raw(get_path(__file__, filename)).split("\n\n")
    return sum([len(set(line.replace("\n", ""))) for line in lines])


def part_two(filename: str) -> int:
    lines = read_raw(get_path(__file__, filename)).split("\n\n")
    return sum([common_letters(l) for l in lines])


def common_letters(line: str) -> int:
    split_lines = line.split("\n")
    seen = list(set(split_lines[0]))
    for p in split_lines[1:]:
        seen = list(set(p) & set(seen))
    return len(seen)



if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
