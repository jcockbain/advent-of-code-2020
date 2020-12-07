from src.common.file_utils import get_path, read_lines
import re


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    bags = {}
    for line in lines:
        outer, rest = line.split("contain")
        outer = outer.strip().rstrip("s")

        if rest == " no other bags.":
            bags[outer] = []

        else:
            bags[outer] = []
            contains = rest.split(",")
            for c in contains:
                c = c.strip().replace(".", "")
                r = re.search(r'(\d+) (\S+.*)', c)
                if r:
                    num, i = r.groups()
                    bags[outer].append(i.rstrip("s"))

    def check_bags(bag):
        if bag == "shiny gold bag":
            return True
        if bag in bags:
            return any([check_bags(b) for b in bags[bag]])
        return False

    total_gold = 0
    for b in bags:
        if check_bags(b):
            total_gold += 1

    return total_gold - 1


def part_two(filename: str) -> int:

    lines = read_lines(get_path(__file__, filename))
    bags = {}
    for line in lines:
        outer, rest = line.split("contain")
        outer = outer.strip().rstrip("s")

        if rest == " no other bags.":
            bags[outer] = []

        else:
            bags[outer] = []
            contains = rest.split(",")
            for c in contains:
                c = c.strip().replace(".", "")
                r = re.search(r'(\d+) (\S+.*)', c)
                if r:
                    num, i = r.groups()
                    bags[outer].append((int(num), i.rstrip("s")))

    def count_bags(bag):
        if bag not in bags or bags[bag] == []:
            return 0

        s = 0
        for b in bags[bag]:
            s += b[0] + (b[0] * count_bags(b[1]))
        return s

    return count_bags("shiny gold bag")


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
