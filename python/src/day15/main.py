from src.common.file_utils import get_path, read_integers


def part_one(nums: list) -> int:
    return play_game(nums, 2020)


def part_two(nums: list) -> int:
    return play_game(nums, 30000000)


def play_game(nums: list, turns: int) -> int:
    history = {}
    last_number, spoken = None, None

    for i in range(turns):
        if i < len(nums):
            spoken = nums[i]
        else:
            if last_number not in history:
                spoken = 0
            else:
                spoken = i - 1 - history[last_number]

        history[last_number] = i - 1
        last_number = spoken

    return last_number


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one([7, 14, 0, 17, 11, 1, 2])
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two([7, 14, 0, 17, 11, 1, 2])
    print(part_two_res)
