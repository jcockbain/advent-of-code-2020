from src.common.file_utils import get_path, read_lines


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    earliest = int(lines[0])
    bus_ids = []
    for i in lines[1].split(","):
        if i != "x":
            bus_ids.append(int(i))

    shortest_wait, bus_id = float('inf'), None

    for b in bus_ids:
        wait = (((earliest // b) * b) + b) - earliest
        if wait < shortest_wait:
            shortest_wait = wait
            bus_id = b

    return shortest_wait * bus_id if shortest_wait else -1


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))

    running_product, earliest_bus = 1, 0
    
    # uses chinese remainder theorem
    for (index, bus) in enumerate(lines[1].split(",")):
        if bus == "x":
            continue

        bus_id = int(bus)
        while ((earliest_bus + index) % bus_id) != 0:
            earliest_bus += running_product
        running_product *= bus_id
    return earliest_bus


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
