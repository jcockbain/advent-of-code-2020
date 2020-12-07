from src.common.file_utils import get_path, read_lines
import re


def part_one(filename: str) -> int:
    bags = process_bags(filename)

    # store previous results to save rechecking paths
    cache = {}

    def check_bags(bag):
        if bag not in cache:
            can_reach_gold = False
            if bag == "shiny gold bag":
                can_reach_gold = True
            elif bag in bags:
                can_reach_gold = any([check_bags(b[1]) for b in bags[bag]])
            cache[bag] = can_reach_gold
        return cache[bag]

    # subtract one for original bag (for gold on outside)
    return sum([check_bags(b) for b in bags]) - 1


def part_two(filename: str) -> int:
    bags = process_bags(filename)

    cache = {}

    def count_bags(bag):
        if bag not in bags or bags[bag] == []:
            return 0
        if bag not in cache:
            cache[bag] = sum([b[0] + b[0] * count_bags(b[1]) for b in bags[bag]])
        return cache[bag]

    return count_bags("shiny gold bag")


# get a dict of bags to contents (as tuples)
def process_bags(filename) -> dict:
    lines = read_lines(get_path(__file__, filename))
    bags = {}
    for line in lines:
        outer_bag, inner_bags = line.split("contain")
        outer_bag = outer_bag.strip().rstrip("s")
        bags[outer_bag] = []
        if inner_bags != " no other bags.":
            for bag in inner_bags.split(","):
                r = re.search(r'(\d+) (\S+.*)', bag.replace(".", ""))
                if r:
                    num, bag_name = r.groups()
                    bags[outer_bag].append((int(num), bag_name.rstrip("s")))
    return bags


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
