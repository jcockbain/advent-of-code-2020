from src.common.file_utils import get_path, read_lines

# do some regex? 

def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    valid_passwords = []
    for word in lines:
        code, password = word.split(":")
        numbers, letter = code.split(" ")
        min_count, max_count = [int(x) for x in numbers.split("-")]
        if min_count <= password.count(letter) <= max_count:
            valid_passwords.append(password)
    return len(valid_passwords)


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    valid_passwords = []
    for word in lines:
        code, password = word.split(":")
        numbers, letter = code.split(" ")
        pos1, pos2 = [int(x) for x in numbers.split("-")]
        if (password[pos1] == letter) ^ (password[pos2] == letter):
            valid_passwords.append(password)
    return len(valid_passwords)


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
