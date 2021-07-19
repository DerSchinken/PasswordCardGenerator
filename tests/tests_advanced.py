from PasswordCardGenerator import PasswordCard
from os import system

if __name__ == "__main__":
    keyword = "Keyword"

    card1 = PasswordCard(len(keyword), seed=10)
    card2 = PasswordCard(len(keyword), seed=10)
    if str(card1) != str(card2):
        raise Exception("Seed does not work!")
    else:
        print("Seed works!")

    # Trying __main__
    ## trying python
    exit_code = system("python -m PasswordCardGenerator -t -p -s 100 --pwd !generate")
    if exit_code:
        ## if python failed use python3
        exit_code = system("python3 -m PasswordCardGenerator -t -p -s 100 --pwd !generate")
        if exit_code:
            raise Exception("'-t -p -s 100 --pwd !generate' failed")
