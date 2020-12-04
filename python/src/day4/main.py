from src.common.file_utils import get_path, read_raw
import re


def part_one(filename: str) -> int:
    lines = read_raw(get_path(__file__, filename))
    pports = lines.split("\n\n")
    valid = []
    for p in pports:
        valid_f = 0
        p = p.replace("\n", " ")
        fields = p.split()
        for f in fields:
            k, v = f.split(":")
            if k != "cid":
                valid_f += 1
        if valid_f >= 7:
            valid.append(p)
    return len(valid)


def part_two(filename: str) -> int:
    lines = read_raw(get_path(__file__, filename))
    pports = lines.split("\n\n")
    valid = []
    for p in pports:
        valid_f = 0
        p = p.replace("\n", " ")
        fields = p.split()
        for f in fields:
            k, v = f.split(":")
            if k in checks:
                if checks[k](v):
                    valid_f += checks[k](v)
        if valid_f >= 7:
            valid.append(p)
    return len(valid)


def check_byr(s):
    if not s.isdigit():
        return False
    if len(s) != 4:
        return False
    return 1920 <= int(s) <= 2002


def check_iyr(s):
    if not s.isdigit():
        return False
    if len(s) != 4:
        return False
    return 2010 <= int(s) <= 2020


def check_eyr(s):
    if not s.isdigit():
        return False
    if len(s) != 4:
        return False
    return 2020 <= int(s) <= 2030


def check_hgt(s):
    # units = [c for c in s if c.isalpha()]
    r = re.search(r'(\d+)([a-z]{2})', s)
    if not r:
        return False
    n, u = "", ""
    if r:
        n, u = r.groups()
    if u == "in":
        return 59 <= int(n) <= 76
    if u == "cm":
        return 150 <= int(n) <= 193
    return False


def check_hcl(s):
    if s[0] != "#":
        return False
    rest = s[1:]
    if len(rest) != 6:
        return False
    for c in rest:
        if not c.isdigit() and (ord("a") > ord(c) or ord("f") < ord(c)):
            return False
    return True


def check_ecl(s):
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(s):
    return len(s) == 9 and s.isdigit()


def check_cid(s):
    return False


checks = {
    "byr": check_byr,
    "iyr": check_iyr,
    "eyr": check_eyr,
    "hgt": check_hgt,
    "hcl": check_hcl,
    "ecl": check_ecl,
    "pid": check_pid,
    "cid": check_cid,
}

if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
