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


# top-down recursion
def part_two_1(filename: str) -> int:
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


# bottom-up recursion
def part_two_2(filename: str) -> int:
    ints = read_integers(get_path(__file__, filename))
    ints_set = set(ints)
    ints.sort()
    ways = [0] * (max(ints) + 1)
    
    for x in [1, 2, 3]:
        ways[x] = int(x in ints)

    for i in range(2, max(ints) + 1):
        if i in ints_set:
            ways[i] += ways[i - 1] + ways[i - 2] + ways[i - 3]

    return ways[-1]


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two_1("input.txt")
    print(part_two_res)
