from src.common.file_utils import get_path, read_integers


def part_one(filename: str) -> int:
    ints = read_integers(get_path(__file__, filename))
    return sum(ints)


def part_two(filename: str) -> int:
    ints = read_integers(get_path(__file__, filename))
    return max(ints)


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
