from src.common.file_utils import get_path, read_integers


def part_one(filename: str) -> int:
    public_keys = read_integers(get_path(__file__, filename))
    pub_key1, pub_key2 = public_keys[0], public_keys[1]
    loop1, loop2 = get_loop_size(pub_key1), get_loop_size(pub_key2)
    encryption_key = transform(pub_key1, loop2)
    assert(encryption_key == transform(pub_key2, loop1))
    return encryption_key


def transform(public_key, loop):
    subject, value = public_key, 1
    for _ in range(loop):
        value = (value * subject) % 20201227
    return value


def get_loop_size(public_key):
    subject, value, size = 7, 1, 0
    while value != public_key:
        size += 1
        value = (value * subject) % 20201227
    return size


if __name__ == '__main__':

    print("---Part One---")
    part_one_res = part_one("input.txt")
    print(part_one_res)
