from src.common.file_utils import get_path, read_lines
import re


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    valid_passwords = []
    for word in lines:
        min_count, max_count, letter, password = re.search(
            r'(\d+)-(\d+) ([a-z]): ([a-z]+)', word).groups()
        if int(min_count) <= password.count(letter) <= int(max_count):
            valid_passwords.append(password)
    return len(valid_passwords)


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    valid_passwords = []
    for word in lines:
        pos1, pos2, letter, password = re.search(
            r'(\d+)-(\d+) ([a-z]): ([a-z]+)', word).groups()
        if (password[int(pos1) - 1] == letter) ^ (password[int(pos2) - 1] == letter):
            valid_passwords.append(password)
    return len(valid_passwords)


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
