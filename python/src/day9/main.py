from collections import deque

from src.common.file_utils import get_path, read_integers


def part_one(filename: str, preamble: int) -> int:
    ints = read_integers(get_path(__file__, filename))
    queue = deque(ints[:preamble])
    for i, n in enumerate(ints[preamble:]):
        if not can_sum(n, queue):
            return n
        queue.append(n)
        queue.popleft()
    return -1


def part_two(filename: str, preamble: int) -> int:
    ints = read_integers(get_path(__file__, filename))
    n = part_one(filename, preamble)
    for i in range(len(ints)):
        for j in range(i + 1, len(ints)):
            if sum(ints[i: j]) == n:
                return min(ints[i:j]) + max(ints[i:j])
    return -1


def can_sum(target, nums):
    seen = set()
    for n in nums:
        if target - n in seen:
            return True
        seen.add(n)
    return False

if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt", 25)
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt", 25)
    print(part_two_res)
