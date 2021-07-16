from PasswordCardGenerator import PasswordCard

if __name__ == '__main__':
    keyword = "VerySafeKeyword"

    card1 = PasswordCard(len(keyword))
    print(card1)
    print(card1.get_password(keyword))

    card1.save("test_card.png")
    card1.save("test_card.txt", txt=True)

    # rows, columns
    print(card1[".", 15])
    print(card1[1, 1])
