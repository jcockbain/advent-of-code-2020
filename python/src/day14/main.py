from src.common.file_utils import get_path, read_lines
import re

BITS = 36


def part_one(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    memory = {}

    for line in lines:
        splitted = line.split("=")
        key, val = splitted[0].strip(), splitted[1].strip()
        
        if key == "mask":
            mask = val
        else:
            address = int(re.search(r'mem\[(\d+)]', key).groups()[0])
            val = list('{:036b}'.format(int(val)))
            for idx, c in enumerate(mask):
                if c != "X" and c != val[idx]:
                    val[idx] = c
            memory[address] = int("".join(val), 2)
    
    return sum(memory.values())


def part_two(filename: str) -> int:
    lines = read_lines(get_path(__file__, filename))
    memory = {}
    
    for line in lines:
        splitted = line.split("=")
        key, val = splitted[0].strip(), splitted[1].strip()
       
        if key == "mask":
            mask = val.strip()
        else:
            address = int(re.search(r'mem\[(\d+)]', key).groups()[0])
            n = list('{:036b}'.format(address))
            floating = 0
            
            # replace with 1's, mark x's
            for i in range(BITS):
                if mask[i] == "X":
                    floating += 1
                    n[i] = "{}"
                elif mask[i] == "1":
                    n[i] = "1"
            n = "".join(n)
            
            if floating > 0:
                bin_format = "0{}b".format(floating)
                # insert each binary number up to 2**floating into positions of X's
                for i in range(2 ** floating):
                    replace_bin = format(i, bin_format)
                    mem_address = n.format(*replace_bin)
                    memory[int(mem_address, 2)] = int(val)
            else:
                memory[int("".join(n), 2)] = int(val)

    return sum(memory.values())


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)

    print("---Part Two---")
    part_two_res = part_two("input.txt")
    print(part_two_res)
