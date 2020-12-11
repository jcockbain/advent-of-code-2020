from src.common.file_utils import get_path, read_lines


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1),
                 (-1, 0), (-1, 1), (0, 1), (1, 1)]
    area = [[c for c in line] for line in lines]
    h, w = len(area), len(area[0])

    while True:
        new_area = [[area[r][c] for c in range(w)] for r in range(h)]
        for r in range(h):
            for c in range(w):

                occupied = 0
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < h and 0 <= nc < w and area[nr][nc] == "#":
                        occupied += 1

                if area[r][c] == "L" and occupied == 0:
                    new_area[r][c] = "#"

                elif area[r][c] == "#" and occupied >= 4:
                    new_area[r][c] = "L"

        if new_area == area:
            return sum([x.count("#") for x in area])
        area = new_area

    return -1


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1),
                 (-1, 0), (-1, 1), (0, 1), (1, 1)]
    area = [[c for c in line] for line in lines]
    h, w = len(area), len(area[0])

    while True:
        new_area = [[area[r][c] for c in range(w)] for r in range(h)]
        for r in range(h):
            for c in range(w):

                occupied = 0
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    while 0 <= nr < h and 0 <= nc < w and area[nr][nc] != "L":
                        if area[nr][nc] == "#":
                            occupied += 1
                            break
                        nr, nc = nr + dr, nc + dc

                if area[r][c] == "L" and occupied == 0:
                    new_area[r][c] = "#"

                elif area[r][c] == "#" and occupied >= 5:
                    new_area[r][c] = "L"

        if new_area == area:
            return sum([x.count("#") for x in area])
        area = new_area

    return -1


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
