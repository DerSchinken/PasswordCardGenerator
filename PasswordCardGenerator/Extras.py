from random import randint
from os import path


def filename_generator(name: str, suffix: str):
    # in case you need a filename generator:
    filename = name + f"_{randint(1000, 100000000)}." + "suffix"
    while path.exists(filename):
        filename = name + f"_{randint(1000, 100000000)}." + "suffix"

    return filename
