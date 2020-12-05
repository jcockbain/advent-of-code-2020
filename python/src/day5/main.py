from src.common.file_utils import get_path, read_lines


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    return max([get_seat_id(line) for line in lines])


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    seat_ids = [get_seat_id(line) for line in lines]
    seat_ids.sort()
    missing = seat_ids[0]
    for s in seat_ids:
        missing ^= s
    return missing


def get_seat_id(line):
    rows, cols = line[0:7], line[7:10]

    row, mask = 0, 64
    for r in rows:
        if r == "B":
            row += mask
        mask >>= 1

    col, mask = 0, 4
    for c in cols:
        if c == "R":
            col += mask
        mask >>= 1

    return (row * 8) + col


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
