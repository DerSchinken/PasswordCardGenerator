from string import ascii_lowercase as al, ascii_uppercase as au, digits as d
from PIL import Image, ImageDraw, ImageFont
from random import choices
from tabulate import tabulate


class PasswordCard:
    """
    Generates a Password Card

    Functions:
      get_password: gets the password for [Keyword]
      save: creates an image containing the table
    """
    def __init__(self, keyword_length: int, segment_length: int = 3):
        self.card, printable = [["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "CWX", "ZY", "."]], al + au + d + "{%}?!.,_;\\'[]#"
        for i in range(keyword_length):
            self.card.append([''.join(choices(printable, k=segment_length + i - i)) for i in range(10)])

    def get_password(self, keyword: str):
        password, o = "", 1
        for char in keyword.upper():
            # get position of keyword char
            pos = None
            for i in range(len(self.card[0])):
                if char in self.card[0][i]:
                    pos = i
                    break
            if pos is None:
                raise NameError("Invalid Keyword!")

            password += self.card[o][pos]
            o += 1

        return password

    def save(self, filename: str, font: str = "courbi", font_size: int = 15):
        text = tabulate(
            self.card,
            headers="firstrow",
            showindex="always",
            tablefmt="github"
        )

        # load font
        font = ImageFont.truetype(font.lower(), font_size)

        # determine the size that the image should have
        size, lines = {"x": 0, "y": 0}, []
        for line in text.split("\n"):
            lines.append(font.getsize(line)[0]+20)
        size["x"] = max(lines)
        size["y"] = len(text.split("\n"))*font.getsize(text)[1]

        # create image
        img = Image.new("RGB", tuple(size.values()), color="white")

        # write text
        pen = ImageDraw.Draw(img)
        pen.text(
            (10, 10),
            text,
            fill=(0, 0, 0),
            font=font,
        )

        # save image
        img.save(filename)

        # in case you need a filename generator:
        """
        filename = f"card_{randint(1000, 100000000)}.png"
        while True:
            if path.exists(f"{filename}"):
                filename = f"card_{randint(1000, 100000000)}.png"
            else:
                break
        """

    def __str__(self) -> str:
        return tabulate(
            self.card,
            headers="firstrow",
            showindex="always",
            tablefmt="github"
        )


if __name__ == '__main__':
    # Stress testing the Generator
    card1 = PasswordCard(500)
    print(card1)
    print(card1.get_password("EinSehrLangesPassword.MalSehenWieLangeDasBraucht.LulSoGutWieWenigerAlsNullSekunden"))
    card1.save("test_card.png")
