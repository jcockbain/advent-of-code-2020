from src.common.file_utils import get_path, read_integers


def part_one(filename: str) -> int:
    ints = read_integers(get_path(__file__, filename))

    # max_adapter = max(ints) + 3

    ints.sort()

    ones, threes = 0, 0
    v = 0

    for i, x in enumerate(ints):

        if x - v == 3:
            threes += 1

        if x - v == 1:
            ones += 1

        v = x

    return ones * (threes + 1)


def part_two(filename: str) -> int:
    ints = read_integers(get_path(__file__, filename))
    ints.sort()
    max_ints = max(ints)
    cache = [-1] * max_ints

    def number_ways(v):
        if v == max_ints:
            return 1

        if cache[v] == -1:
            s = 0

            if v + 1 in ints:
                s += number_ways(v + 1)

            if v + 2 in ints:
                s += number_ways(v + 2)

            if v + 3 in ints:
                s += number_ways(v + 3)

            cache[v] = s

        return cache[v]

    return number_ways(0)


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
