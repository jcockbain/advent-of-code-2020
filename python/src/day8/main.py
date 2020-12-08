from src.common.file_utils import get_path, read_lines


def part_one(filename: str) -> int:
    return run_code(read_lines(get_path(__file__, filename)))[1]


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))

    for i, line in enumerate(lines):
        code, value = line.split(" ")

        if code == "nop":
            line_copy = lines[:]
            line_copy[i] = "{} {}".format("jmp", value)
            completed, acc = run_code(line_copy)
            if completed:
                return acc

        elif code == "jmp":
            line_copy = lines[:]
            line_copy[i] = "{} {}".format("nop", value)
            completed, acc = run_code(line_copy)
            if completed:
                return acc

    return -1


def run_code(lines) -> (bool, int):
    acc, idx = 0, 0
    visited = set()

    while idx < len(lines) and idx not in visited:
        visited.add(idx)
        line = lines[idx]
        code, value = line.split(" ")

        if code == "acc":
            acc = acc + \
                int(value[1:]) if value[0] == "+" else acc - int(value[1:])
            idx += 1

        elif code == "jmp":
            idx = idx + \
                int(value[1:]) if value[0] == "+" else idx - int(value[1:])

        elif code == "nop":
            idx += 1

    return (idx not in visited, acc)


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
