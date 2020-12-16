from src.common.file_utils import get_path, read_lines, read_raw


class TicketReader():

    def __init__(self, filename):
        self.your_tickets, self.nearby_tickets, self.fields = self.process_input(
            filename)
        self.error_rate = self.get_error_rate()
        self.valid_tickets = self.get_valid_tickets()

    def is_valid(self, rule, v):
        for (lower, upper) in self.fields[rule]:
            if (lower <= v and v <= upper):
                return True
        return False

    def process_input(self, filename):
        lines = read_raw(get_path(__file__, filename))

        rules_string, your_ticket_string, nearby_ticket_string = lines.split(
            "\n\n")

        your_tickets = [[int(x) for x in t.split(",")]
                        for t in your_ticket_string.split("\n")[1:]]

        nearby_tickets = [[int(x) for x in t.split(",")]
                          for t in nearby_ticket_string.split("\n")[1:]]

        rules = {}
        for rule in rules_string.split("\n"):
            name, boundaries = rule.split(": ")
            rules[name] = []
            for val in boundaries.split("or"):
                val = val.strip()
                splitted = val.split("-")
                rules[name].append((int(splitted[0]), int(splitted[1])))

        return your_tickets[0], nearby_tickets, rules

    def get_error_rate(self):
        error = 0
        for ticket in self.nearby_tickets:
            for f in ticket:
                valid_field = False
                for _, rule in self.fields.items():
                    for (lower, upper) in rule:
                        if (lower <= f and f <= upper):
                            valid_field = True
                if not valid_field:
                    error += f
        return error

    def get_valid_tickets(self):
        valid_nearby_tickets = []
        for ticket in self.nearby_tickets:
            valid_ticket = True
            for f in ticket:
                valid_field = False
                for name, rule in self.fields.items():
                    for (lower, upper) in rule:
                        if (lower <= f and f <= upper):
                            valid_field = True
                if not valid_field:
                    valid_ticket = False
            if valid_ticket:
                valid_nearby_tickets.append(ticket)
        return [self.your_tickets] + valid_nearby_tickets


def part_one(filename: str) -> int:
    ticket_reader = TicketReader(filename)
    return ticket_reader.error_rate


def part_two(filename: str) -> int:

    ticket_reader = TicketReader(filename)
    possible_positions = {}

    tickets = ticket_reader.valid_tickets
    your_ticket = ticket_reader.your_tickets

    for rule in ticket_reader.fields:
        possible_positions[rule] = set(
            [x for x in range(len(your_ticket))])

    for ticket in tickets:
        for pos, v in enumerate(ticket):
            for rule in possible_positions:
                if pos in possible_positions[rule]:
                    if not ticket_reader.is_valid(rule, v):
                        possible_positions[rule].remove(pos)

    mapping = {}
    while len(possible_positions) > 0:
        pos_taken, remove = None, ""
        for rule, positions in possible_positions.items():
            if len(positions) == 1:
                v = list(positions)[0]
                mapping[rule] = v
                pos_taken = v
                remove = rule
                break

        for rule, positions in possible_positions.items():
            positions.remove(pos_taken)

        del possible_positions[remove]

    total = 1
    for rule, val in mapping.items():
        if "departure" in rule:
            total *= your_ticket[val]

    return total


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
