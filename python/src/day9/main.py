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


def can_sum(target, nums):
    seen = set()
    for n in nums:
        if target - n in seen:
            return True
        seen.add(n)
    return False


def part_two(filename: str, preamble: int) -> int:
    ints = read_integers(get_path(__file__, filename))
    n = part_one(filename, preamble)
    return sub_array_sum(n, ints)


# O(N) using sliding window
def sub_array_sum(target, ints):
    curr_sum = 0
    start = 0

    for end, val in enumerate(ints):
        curr_sum += val
        while curr_sum > target:
            curr_sum -= ints[start]
            start += 1
        if curr_sum == target:
            return min(ints[start:end+1]) + max(ints[start:end+1])

    return -1


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt", 25)
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt", 25)
    print(part_two_res)
