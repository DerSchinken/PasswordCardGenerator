from PasswordCardGenerator import PasswordCard

if __name__ == '__main__':
    keyword = "VerySafe"  # ''.join([str(i)[0] for i in range(82)])

    # print(len(keyword), keyword)

    card1 = PasswordCard(len(keyword))
    print(card1)
    # print(card1.get_password("EinSehrLangesPassword.MalSehenWieLangeDasBraucht.LulSoGutWieWenigerAlsNullSekunden"))
    print(card1.get_password(keyword))
    # print(card1.get_password("abcdefghijklmnopqrstuvxyz."))

    card1.save("test_card.png")
    card1.save("test_card.txt", txt=True)
