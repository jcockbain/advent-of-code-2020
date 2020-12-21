from src.common.file_utils import get_path, read_raw


class Solver():
    def __init__(self, filename):
        self.rules, self.messages = self.parse_input(filename)
        self.possibles = {}

    def parse_input(self, filename):
        lines = read_raw(filename)
        splitted = lines.split("\n\n")
        messages = splitted[1].split("\n")
        rules = {}
        for rule in splitted[0].split("\n"):
            key, r = rule.split(":")
            val = str(r).replace('"', "").strip()
            if val.isalpha():
                rules[int(key)] = (0, [val])
            else:
                rules[int(key)] = (1, [x.strip() for x in r.split("|")])
        return rules, messages

    def get_possible_messages(self, rule_idx):
        if rule_idx not in self.possibles:
            rule = self.rules[rule_idx]
            if rule[0] == 0:
                self.possibles[rule_idx] = rule[1]
            else:
                possibles = []
                for single_rule in rule[1]:
                    vals = [int(v) for v in single_rule.split(" ")]
                    res = self.get_possible_messages(vals[0])
                    for val in vals[1:]:
                        messages = self.get_possible_messages(val)
                        res = [r + m for r in res for m in messages]
                    possibles += res
                self.possibles[rule_idx] = possibles
        return self.possibles[rule_idx]


def matches_rule8(prefixes, suffixes, message):
    for p in prefixes:
        if len(message) < len(p):
            return False
        if message.startswith(p):
            if matches_rule11(prefixes, suffixes, message[len(p):]):
                return True
            elif matches_rule8(prefixes, suffixes, message[len(p):]):
                return True
    return False


def matches_rule11(prefixes, suffixes, message):
    for p in prefixes:
        for s in suffixes:
            if len(message) < len(p) + len(s):
                return False
            if message.startswith(p) and message.endswith(s):
                if len(message) == len(p) + len(s):
                    return True
                elif matches_rule11(prefixes, suffixes, message[len(p):len(message)-len(s)]):
                    return True
    return False


def part_one(filename: str) -> int:
    solver = Solver(get_path(__file__, filename))
    possibles = solver.get_possible_messages(0)
    return sum([x in possibles for x in solver.messages])


def part_two(filename: str) -> int:
    solver = Solver(get_path(__file__, filename))
    prefixes = solver.get_possible_messages(42)
    suffixes = solver.get_possible_messages(31)
    return sum([1 for m in solver.messages if matches_rule8(prefixes, suffixes, m)])


def path(filename: str):
    return get_path(__file__, filename)


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
