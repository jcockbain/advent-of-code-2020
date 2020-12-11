from src.common.file_utils import get_path, read_lines

NEIGHBOURS = [(1, 0), (1, -1), (0, -1), (-1, -1),
              (-1, 0), (-1, 1), (0, 1), (1, 1)]

EMPTY_SEAT = "L"
FILLED_SEAT = "#"
PATH = "."


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    area = [[c for c in line] for line in lines]
    h, w = len(area), len(area[0])
    old_area = None

    while area != old_area:
        old_area = [[area[r][c] for c in range(w)] for r in range(h)]
        for r in range(h):
            for c in range(w):
                if old_area[r][c] != PATH:
                    
                    occupied = 0
                    for dr, dc in NEIGHBOURS:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w and old_area[nr][nc] == FILLED_SEAT:
                            occupied += 1
                    if occupied == 0:
                        area[r][c] = FILLED_SEAT
                    elif occupied >= 4:
                        area[r][c] = EMPTY_SEAT

    return sum([x.count(FILLED_SEAT) for x in area])


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    area = [[c for c in line] for line in lines]
    h, w = len(area), len(area[0])
    old_area = None

    while area != old_area:
        old_area = [[area[r][c] for c in range(w)] for r in range(h)]
        for r in range(h):
            for c in range(w):
                if area[r][c] != PATH:
                    
                    occupied = 0
                    for dr, dc in NEIGHBOURS:
                        nr, nc = r + dr, c + dc
                        # keep moving in same direction till empty or filled seat
                        while 0 <= nr < h and 0 <= nc < w and old_area[nr][nc] != EMPTY_SEAT:
                            if old_area[nr][nc] == FILLED_SEAT:
                                occupied += 1
                                break
                            nr, nc = nr + dr, nc + dc

                    if occupied == 0:
                        area[r][c] = FILLED_SEAT
                    elif occupied >= 5:
                        area[r][c] = EMPTY_SEAT
    
    return sum([x.count(FILLED_SEAT) for x in area])


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
