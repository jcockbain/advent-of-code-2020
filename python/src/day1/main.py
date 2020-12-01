from src.common.file_utils import get_path, read_integers


def part_one(filename: str) -> int:
    ints = read_integers(get_path(__file__, filename))
    return two_sum(ints, 2020)


def part_two(filename: str) -> int:
    ints = read_integers(get_path(__file__, filename))
    # use twosum solution from p1 to reduce time complexity from
    # O(n^3) to O(n^2)
    for i, n in enumerate(ints):
        multiplier = two_sum(ints[i + 1:], 2020 - n)
        if multiplier != -1:
            return n * multiplier
    return -1


def two_sum(ints: list, target: int) -> int:
    seen = set()
    for i in ints:
        if target - i in seen:
            return i * (target - i)
        seen.add(i)
    return -1


if __name__ == '__main__':
    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
