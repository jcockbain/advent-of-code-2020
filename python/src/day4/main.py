from src.common.file_utils import get_path, read_raw
import re


def part_one(filename: str) -> int:
    lines = read_raw(get_path(__file__, filename))
    pports = lines.split("\n\n")
    valid_pports = []
    for p in pports:
        valid_fields = 0
        for f in p.replace("\n", " ").split():
            k, v = f.split(":")
            valid_fields += k != "cid"
        if valid_fields >= 7:
            valid_pports.append(p)
    return len(valid_pports)


def part_two(filename: str) -> int:
    lines = read_raw(get_path(__file__, filename))
    pports = lines.split("\n\n")
    valid_pports = []
    for p in pports:
        valid_fields = 0
        for f in p.replace("\n", " ").split():
            k, v = f.split(":")
            valid_fields += checks[k](v)
        if valid_fields >= 7:
            valid_pports.append(p)
    return len(valid_pports)


def check_byr(s):
    return s.isdigit() and 1920 <= int(s) <= 2002


def check_iyr(s):
    return s.isdigit() and 2010 <= int(s) <= 2020


def check_eyr(s):
    return s.isdigit() and 2020 <= int(s) <= 2030


def check_hgt(s):
    try:
        val, unit = re.search(r'(\d+)([a-z]{2})', s).groups()
    except AttributeError:
        return False
    if unit not in ["in", "cm"]:
        return False
    return 59 <= int(val) <= 76 if unit == "in" else 150 <= int(val) <= 193


def check_hcl(s):
    return re.search(r'#[a-f\d]{6}', s) is not None


def check_ecl(s):
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(s):
    return len(s) == 9 and s.isdigit()


def check_cid(_):
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
