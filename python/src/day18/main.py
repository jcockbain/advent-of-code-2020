from src.common.file_utils import get_path, read_lines


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    return sum([evaluate(l, evaluate_exp1) for l in lines])


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    return sum([evaluate(l, evaluate_exp2) for l in lines])


def evaluate(exp, evaluate_exp_func):
    exp = [c for c in exp.replace(" ", "")]
    i, start = 0, None

    while i < len(exp):
        if exp[i] == "(":
            start = i

        elif exp[i] == ")":
            exp = exp[:start] + [evaluate_exp_func(exp[start+1:i])] + exp[i+1:]
            i, start = 0, None
            continue
        i += 1

    return evaluate_exp_func(exp)


def evaluate_exp1(exp):
    n = 0
    current_op = "+"
    for i in range(len(exp)):
        
        c = str(exp[i])
        if c in ["+", "*"]:
            current_op = c

        elif c.isdigit():
            n = operate(current_op)(n, int(c))

    return n


def evaluate_exp2(exp):
    while len(exp) > 1:
        for op in ["+", "*"]:
            while op in exp:
                idx = exp.index(op)
                val = operate(op)(int(exp[idx-1]), int(exp[idx+1]))
                exp = exp[:idx - 1] + [val] + exp[idx+2:]
    return exp[-1]


def operate(op):
    if op == "+":
        return lambda a, b: a + b
    if op == "*":
        return lambda a, b: a * b


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
