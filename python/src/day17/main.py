
from src.common.file_utils import get_path, read_lines
from collections import defaultdict


ALIVE = "#"
DEAD = "."


class Board():
    def __init__(self, input_board):
        self.cells = self.init_cells(input_board)

    def init_cells(self, board):
        cells = {}
        h = len(board)
        w = len(board[0])
        for r in range(h):
            for c in range(w):
                cells[(c, r, 0)] = board[r][c]

        return cells

    def print(self):
        max_z, min_z, max_y, max_x = 0, 0, 0, 0

        for (x, y, z) in self.cells:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            max_z = max(max_z, z)
            min_z = min(min_z, z)

        s = ""
        for z in range(min_z, max_z + 1):
            s += "Z = {}\n".format(z)
            for y in range(0, max_y + 1):
                for x in range(0, max_x + 1):
                    s += self.cells.get((x, y, z), DEAD)
                s += "\n"
            s += "\n"
        print(s)

    def cycle(self):

        new_neighbours = defaultdict(int)
        for cell, val in self.cells.items():
            if val is ALIVE:
                neighbours = get_neighbours_array_1(cell)
                for n in neighbours:
                    new_neighbours[n] += 1

        new_cells = {}
        for cell, count in new_neighbours.items():
            if (cell in self.cells and self.cells[cell] == ALIVE) and (2 <= count <= 3):
                new_cells[cell] = ALIVE

            elif (cell not in self.cells or self.cells[cell] == DEAD) and (count == 3):
                new_cells[cell] = ALIVE

        self.cells = new_cells

    def count_neighbours(self, loc):
        n = 0
        for neighbour in get_neighbours_array_1(loc):
            if self.cells.get(neighbour, DEAD) == ALIVE:
                n += 1
        return n

    def count_alive(self):
        alive = 0
        for state in self.cells.values():
            if state == ALIVE:
                alive += 1
        return alive

def get_neighbours_array_1(loc):
    n = []
    x, y, z = loc
    for dz in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if [dx, dy, dz] != [0, 0, 0]:
                    n.append((x + dx, y + dy, z + dz))
    return n

# TODO: Remove big duplication between 1 and 2


class Board_2():
    def __init__(self, input_board):
        self.cells = self.init_cells(input_board)

    def init_cells(self, board):
        cells = {}
        h = len(board)
        w = len(board[0])
        for r in range(h):
            for c in range(w):
                cells[(c, r, 0, 0)] = board[r][c]

        return cells

    def cycle(self):

        new_neighbours = defaultdict(int)
        for cell, val in self.cells.items():
            if val is ALIVE:
                neighbours = get_neighbours_array_2(cell)
                for n in neighbours:
                    new_neighbours[n] += 1

        new_cells = {}
        for cell, count in new_neighbours.items():
            if (cell in self.cells and self.cells[cell] == ALIVE) and (2 <= count <= 3):
                new_cells[cell] = ALIVE

            elif (cell not in self.cells or self.cells[cell] == DEAD) and (count == 3):
                new_cells[cell] = ALIVE

        self.cells = new_cells

    def count_neighbours(self, loc):
        n = 0
        for neighbour in get_neighbours_array_2(loc):
            if self.cells.get(neighbour, DEAD) == ALIVE:
                n += 1
        return n

    def count_alive(self):
        alive = 0
        for state in self.cells.values():
            if state == ALIVE:
                alive += 1
        return alive


def get_neighbours_array_2(loc):
    n = []
    x, y, z, w = loc
    for dw in [-1, 0, 1]:
        for dz in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if [dx, dy, dz, dw] != [0, 0, 0, 0]:
                        n.append((x + dx, y + dy, z + dz, w + dw))
    return n


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))

    board = Board(lines)

    for i in range(6):

        # print("ROUND: {}".format(i))
        board.cycle()
        # board.print()

    return board.count_alive()


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))

    board = Board_2(lines)

    for i in range(6):

        # print("ROUND: {}".format(i))
        board.cycle()
        # board.print()

    return board.count_alive()


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
