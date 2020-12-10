from src.common.file_utils import get_path, read_integers


def part_one(filename: str) -> int:
    ints = read_integers(get_path(__file__, filename))
    ints.sort()
    ones, threes, v = 0, 0, 0

    for x in ints:
        threes += (x - v == 3)
        ones += (x - v == 1)
        v = x

    return ones * (threes + 1)


def part_two(filename: str) -> int:
    ints = read_integers(get_path(__file__, filename))
    ints_set = set(ints)
    cache = [-1] * max(ints)

    def number_ways(v):
        if v not in ints_set:
            return 0
        if v == max(ints):
            return 1

        if cache[v] == -1:
            cache[v] = sum([number_ways(v + x) for x in range(1, 4)])

        return cache[v]

    return sum([number_ways(x) for x in range(1, 4)])


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
