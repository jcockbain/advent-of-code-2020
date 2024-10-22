from src.common.file_utils import get_path, read_lines


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    earliest, shortest_wait, bus_id = int(lines[0]), float('inf'), None

    for b in [int(x) for x in lines[1].split(',') if x.isnumeric()]:
        wait = (((earliest // b) * b) + b) - earliest
        if wait < shortest_wait:
            shortest_wait, bus_id = wait, b
    
    return shortest_wait * bus_id if shortest_wait else -1


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    running_product, earliest_bus = 1, 0

    # uses chinese remainder theorem
    for (index, bus) in enumerate(lines[1].split(",")):
        if bus != "x":
            while ((earliest_bus + index) % int(bus)) != 0:
                earliest_bus += running_product
            running_product *= int(bus)
    
    return earliest_bus


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
