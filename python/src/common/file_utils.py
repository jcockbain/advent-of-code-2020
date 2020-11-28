import os


def get_path(dir_name: str, filename: str) -> str:
    return os.path.join(os.path.dirname(dir_name), filename)