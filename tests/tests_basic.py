from PasswordCardGenerator import PasswordCard

if __name__ == '__main__':
    keyword = "VerySafeKeyword"

    card = PasswordCard(keyword)
    print(card)
    print(card.get_password(keyword))

    card.save("test_card.png")
    card.save("test_card.png", background="black", font_color="white")
    card.save("test_card.png", background="transparent", font_color="white")
    card.save("test_card.txt", txt=True)

    # rows, columns
    print(card[".", 15])
    print(card[1, 1])
    print(card[1])
    print(card["."])

    print(card.raw())
