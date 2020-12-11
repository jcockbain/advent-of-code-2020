from src.common.file_utils import get_path, read_lines

NEIGHBOURS = [(1, 0), (1, -1), (0, -1), (-1, -1),
              (-1, 0), (-1, 1), (0, 1), (1, 1)]

FILLED_SEAT = "L"
EMPTY_SEAT = "#"


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    area = [[c for c in line] for line in lines]
    h, w = len(area), len(area[0])

    while True:
        new_area = [[area[r][c] for c in range(w)] for r in range(h)]
        for r in range(h):
            for c in range(w):

                occupied = 0
                for dr, dc in NEIGHBOURS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < h and 0 <= nc < w and area[nr][nc] == EMPTY_SEAT:
                        occupied += 1

                if area[r][c] == FILLED_SEAT and occupied == 0:
                    new_area[r][c] = EMPTY_SEAT

                elif area[r][c] == EMPTY_SEAT and occupied >= 4:
                    new_area[r][c] = FILLED_SEAT

        if new_area == area:
            return sum([x.count(EMPTY_SEAT) for x in area])
        area = new_area

    return -1


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    area = [[c for c in line] for line in lines]
    h, w = len(area), len(area[0])

    while True:
        new_area = [[area[r][c] for c in range(w)] for r in range(h)]
        for r in range(h):
            for c in range(w):

                occupied = 0
                for dr, dc in NEIGHBOURS:
                    nr, nc = r + dr, c + dc
                    # keep moving in same direction till empty or filled seat
                    while 0 <= nr < h and 0 <= nc < w and area[nr][nc] != FILLED_SEAT:
                        if area[nr][nc] == EMPTY_SEAT:
                            occupied += 1
                            break
                        nr, nc = nr + dr, nc + dc

                if area[r][c] == FILLED_SEAT and occupied == 0:
                    new_area[r][c] = EMPTY_SEAT

                elif area[r][c] == EMPTY_SEAT and occupied >= 5:
                    new_area[r][c] = FILLED_SEAT

        if new_area == area:
            return sum([x.count(EMPTY_SEAT) for x in area])
        area = new_area

    return -1


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
