import os


def read_integers(file: str) -> list:
    with open(file) as f:
        return [int(x) for x in f.readlines()]


def read_lines(file: str) -> list:
    with open(file) as f:
        return [line.rstrip() for line in f.readlines()]


def read_list(file: str) -> list:
    with open(file) as f:
        return f.read().split(",")


def read_raw(file: str) -> str:
    with open(file) as f:
        return f.read()


def get_path(dir_name: str, filename: str) -> str:
    return os.path.join(os.path.dirname(dir_name), filename)
