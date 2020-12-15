from src.common.file_utils import get_path, read_integers


def part_one(nums: list) -> int:
    return play_game(nums, 2020)


def part_two(nums: list) -> int:
    return play_game(nums, 30000000)


def play_game(nums: list, turns: int) -> int:
    history = {}
    a = [0] * turns

    for i in range(turns - 1):
        if i < len(nums):
            a[i] = nums[i]
        else:
            if a[i] in history:
                a[i + 1] = i - history[a[i]]
        history[a[i]] = i

    return a[-1]


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one([7, 14, 0, 17, 11, 1, 2])
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two([7, 14, 0, 17, 11, 1, 2])
    print(part_two_res)
