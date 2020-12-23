from src.common.file_utils import get_path, read_raw


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def part_one(filename: str) -> int:
    n = read_raw(get_path(__file__, filename))
    return calc_one(n.strip("\n"), 100)


def part_two(filename: str) -> int:
    n = read_raw(get_path(__file__, filename))
    return calc_two(n.strip("\n"), 10000000)


def calc_one(n, moves):
    ordering = [int(x) for x in n]
    highest = max(ordering)
    lowest = min(ordering)

    head, d = create_ll(ordering)

    for _ in range(moves):
        head = move(d, head, lowest, highest)

    res = []
    curr_node = d[1].next
    while curr_node.val != 1:
        res.append(curr_node.val)
        curr_node = curr_node.next

    return "".join([str(x) for x in res])


def calc_two(n, moves):
    ordering = [int(x) for x in n]
    highest = max(ordering)
    lowest = min(ordering)
    for i in range(highest + 1, 1000001):
        ordering.append(i)
    highest = 1000000

    head, d = create_ll(ordering)

    for _ in range(moves):
        head = move(d, head, lowest, highest)

    return d[1].next.val * d[1].next.next.val


def create_ll(ordering):
    head = Node(ordering[0])
    node = head

    d = {}
    for v in ordering[1:]:
        new_node = Node(v)
        node.next = new_node
        d[node.val] = node
        node = new_node

    node.next = head
    d[node.val] = node
    return head, d


def move(d, current, lowest, highest):

    start = d[current.val]
    removed = start.next
    removed_end = start.next.next.next
    removed_vals = [start.next.val,
                    start.next.next.val, start.next.next.next.val]
    three_ahead = start.next.next.next.next
    start.next = three_ahead

    destination = current.val - 1

    while destination < lowest or destination in removed_vals:
        destination -= 1
        if destination < lowest:
            destination = highest

    destination_node = d[destination]
    destination_next = destination_node.next
    destination_node.next = removed
    removed_end.next = destination_next

    return current.next


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
