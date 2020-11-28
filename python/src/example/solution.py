def _get_inputs_int(filename):
    with open(filename) as file:
        return list(map(int, file))

def part_one(filename: str):
    return _get_inputs_int(filename)