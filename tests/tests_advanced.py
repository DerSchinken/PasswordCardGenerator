from PasswordCardGenerator import PasswordCard
from os import system

if __name__ == "__main__":
    keyword = "Keyword"

    card1 = PasswordCard(len(keyword), seed=10)
    card2 = PasswordCard(len(keyword), seed=10)
    if str(card1) != str(card2):
        raise Exception("'Seed' doesn't work!")
    else:
        print("'Seed' works!")

    if card1 == card2:
        print("'__eq__' works!")
    else:
        raise Exception("'__eq__' doesn't work!")

    # Trying __getitem__
    try:
        card1[1, 2, 3]
    except TypeError:
        pass
    else:
        raise Exception("'__getitem__' doesn't work!")

    try:
        x = card1[1, 2]
        x = card1[".", 4], x
        x = card1[1], x
    except Exception as e:
        print(e)
        raise Exception("'__getitem__' doesn't work")

    print("'__getitem__' works!")

    # Trying __repr__
    expected = f"PasswordCard(keyword_length={len(keyword)}, segment_length=3, seed=10)"
    if repr(card1) == expected and repr(card2) == expected:
        print("__repr__ works!")
    else:
        raise Exception("'__repr__' doesn't work!")

    # Trying __main__
    ## trying python
    exit_code = system("python -m PasswordCardGenerator -t -p -s 100 --pwd !generate")
    if exit_code:
        ## if python failed use python3
        exit_code = system("python3 -m PasswordCardGenerator -t -p -s 100 --pwd !generate")
        if exit_code:
            raise Exception("'-t -p -s 100 --pwd !generate' failed")
