from PasswordCardGenerator import PasswordCard

if __name__ == '__main__':
    card1 = PasswordCard(500)
    print(card1)
    print(card1.get_password("EinSehrLangesPassword.MalSehenWieLangeDasBraucht.LulSoGutWieWenigerAlsNullSekunden"))
    print(card1.get_password("VerySafe"))
    print(card1.get_password("abcdefghijklmnopqrstuvxyz."))
    card1.save("test_card.png")
    card1.save("test_card.txt", txt=True)
