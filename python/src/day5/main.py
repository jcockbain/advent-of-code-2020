from src.common.file_utils import get_path, read_lines


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    highest_id = 0
    for line in lines:
        highest_id = max(highest_id, get_seat_id(line))
    return highest_id


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    seat_ids = []
    for line in lines:
        seat_ids.append(get_seat_id(line))
    
    seat_ids.sort()
    missing = seat_ids[0]
    for s in seat_ids:
        missing ^= s
    return missing


def get_seat_id(line):
    rows = line[0:7]
    cols = line[7:10]

    row, mask = 0, 64 
    for i in range((len(rows))):
        if rows[i] == "B":
            row += mask
        mask >>= 1

    col, mask = 0, 4
    for j in range((len(cols))):
        if cols[j] == "R":
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
