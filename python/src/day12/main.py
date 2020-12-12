from src.common.file_utils import get_path, read_lines
import math


def part_one(filename: str) -> int:
    direction = 90
    x, y = 0, 0
    lines = read_lines(get_path(__file__, filename))
    for l in lines:
        d, v = l[0], int(l[1:])

        if d == "R":
            direction = (direction + v) % 360

        if d == "L":
            direction = (direction - v) % 360

        if d == "N":
            y += v

        if d == "E":
            x += v

        if d == "S":
            y -= v

        if d == "W":
            x -= v

        if d == "F":
            y += math.cos(math.radians(direction)) * v
            x += math.sin(math.radians(direction)) * v

    return abs(x) + abs(y)


def part_two(filename: str) -> int:
    wx, wy = 10, 1
    sx, sy = 0, 0
    lines = read_lines(get_path(__file__, filename))
    for l in lines:
        d, v = l[0], int(l[1:])

        if d == "R":
            wx, wy = rotate_coords(wx, wy, v)

        if d == "L":
            wx, wy = rotate_coords(wx, wy, 360 - v)

        if d == "N":
            wy += v

        if d == "E":
            wx += v

        if d == "S":
            wy -= v

        if d == "W":
            wx -= v

        if d == "F":
            sx += wx * v
            sy += wy * v

    return abs(sx) + abs(sy)


def rotate_coords(wx, wy, v):
    if v == 90:
        return wy, -wx
    elif v == 180:
        return -wx, -wy
    if v == 270:
        return -wy, wx
    return wx, wy


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
