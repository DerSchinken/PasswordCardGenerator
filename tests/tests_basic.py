from PasswordCardGenerator import PasswordCard, save_card, load_card

if __name__ == '__main__':
    keyword = "VerySafeKeyword"

    card = PasswordCard(keyword)
    print(card)
    print(card.get_password(keyword))

    card.save_png("test_card.png")
    card.save_png("test_card.png", background="black", font_color="white")
    card.save_png("test_card.png", background="transparent", font_color="white")
    card.save_text("test_card.txt")

    # rows, columns
    print(card[".", 15])
    print(card[1, 1])
    print(card[1])
    print(card["."])

    print(card.raw)

    save_card(card, "test.card")
    x = load_card("test.card")
    print(x.get_password("abx"))
    print(card.get_password("abx"))

    print(repr(x))  # this is weird
    print(repr(card))
